"""
Async Crawler Engine for ExamSIDE JEE Main.
Handles chapter discovery, concurrent question batch fetching,
progress tracking, and database synchronization.
"""

import asyncio
import logging
from typing import List, Dict, Any, Optional, Callable, Set, Tuple
from datetime import datetime
import httpx
from bs4 import BeautifulSoup

from app.crawler.page_parser import parse_chapter_page, parse_question_batch_page
from app.db.database import (
    upsert_chapter, get_chapter, upsert_question,
    update_task_progress, get_all_chapters, DB_PATH
)
from app.db.models import ChapterModel, QuestionModel
from app.analyzer.analyzer_service import analyze_chapter
from app.exporter.docx_exporter import generate_chapter_docx
from app.exporter.pdf_exporter import generate_chapter_pdf

logger = logging.getLogger("jee_crawler")

ROOT_URL = "https://questions.examside.com/past-years/jee/jee-main"
BASE_URL = "https://questions.examside.com"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

# The 4 pilot chapters requested by the user
PILOT_CHAPTERS = [
    {
        "subject": "chemistry",
        "slug": "electrochemistry",
        "title": "Electrochemistry",
        "url": "https://questions.examside.com/past-years/jee/jee-main/chemistry/electrochemistry"
    },
    {
        "subject": "physics",
        "slug": "electromagnetic-induction",
        "title": "Electromagnetic Induction",
        "url": "https://questions.examside.com/past-years/jee/jee-main/physics/electromagnetic-induction"
    },
    {
        "subject": "physics",
        "slug": "alternating-current",
        "title": "Alternating Current",
        "url": "https://questions.examside.com/past-years/jee/jee-main/physics/alternating-current"
    },
    {
        "subject": "mathematics",
        "slug": "vector-algebra",
        "title": "Vector Algebra",
        "url": "https://questions.examside.com/past-years/jee/jee-main/mathematics/vector-algebra"
    }
]


class CrawlerEngine:
    def __init__(self, db_path: str = DB_PATH, max_concurrency: int = 5):
        self.db_path = db_path
        self.semaphore = asyncio.Semaphore(max_concurrency)
        self.client: Optional[httpx.AsyncClient] = None
        self._is_running = False
        self._queue: asyncio.Queue = asyncio.Queue()
        self._current_task_info: Dict[str, Any] = {}

    async def get_client(self) -> httpx.AsyncClient:
        if self.client is None or self.client.is_closed:
            self.client = httpx.AsyncClient(
                headers=HEADERS,
                timeout=30.0,
                follow_redirects=True,
                limits=httpx.Limits(max_connections=20, max_keepalive_connections=10)
            )
        return self.client

    async def close(self):
        if self.client and not self.client.is_closed:
            await self.client.aclose()
            self.client = None

    async def discover_all_chapters(self) -> List[ChapterModel]:
        """
        Crawl the main JEE Main page to discover all chapters across Physics,
        Chemistry, and Mathematics.
        """
        client = await self.get_client()
        resp = await client.get(ROOT_URL)
        if resp.status_code != 200:
            logger.error(f"Failed to fetch root URL: {resp.status_code}")
            return []

        soup = BeautifulSoup(resp.text, 'html.parser')
        discovered: List[ChapterModel] = []

        # Find all links to subject chapters: /past-years/jee/jee-main/{subject}/{slug}
        seen_slugs: Set[str] = set()
        for a in soup.find_all('a', href=True):
            href = a['href']
            if href.startswith('/past-years/jee/jee-main/') and href.count('/') == 5:
                parts = href.strip('/').split('/')
                subject = parts[3].lower()
                slug = parts[4].lower()
                if slug in seen_slugs:
                    continue
                seen_slugs.add(slug)

                # Extract clean title by stripping numbers and badges
                raw_text = a.get_text(separator=' ', strip=True)
                title = raw_text.split('2026')[0].split('2025')[0].strip()
                if not title:
                    title = slug.replace('-', ' ').title()

                full_url = f"{BASE_URL}{href}" if href.startswith('/') else href
                chapter = ChapterModel(
                    subject=subject,
                    slug=slug,
                    title=title,
                    url=full_url,
                    status="pending"
                )
                upsert_chapter(chapter, db_path=self.db_path)
                discovered.append(chapter)

        # Make sure our pilot chapters are registered
        for p in PILOT_CHAPTERS:
            upsert_chapter(ChapterModel(**p), db_path=self.db_path)

        logger.info(f"Discovered {len(discovered)} chapters on ExamSIDE.")
        return discovered

    async def _fetch_batch_url(
        self,
        batch_url: str,
        chapter_slug: str,
        subject: str
    ) -> Tuple[List[QuestionModel], Optional[str]]:
        """Fetch a single question batch URL with rate limiting and retries."""
        async with self.semaphore:
            client = await self.get_client()
            for attempt in range(3):
                try:
                    resp = await client.get(batch_url)
                    if resp.status_code == 200:
                        await asyncio.sleep(0.02)  # polite pause
                        return parse_question_batch_page(resp.text, batch_url, chapter_slug, subject)
                    elif resp.status_code == 429:
                        await asyncio.sleep(1.0 * (attempt + 1))
                    else:
                        logger.warning(f"Batch URL returned status {resp.status_code}: {batch_url}")
                        return ([], None)
                except Exception as e:
                    if attempt == 2:
                        logger.error(f"Error fetching batch URL {batch_url}: {e}")
                        return ([], None)
                    await asyncio.sleep(0.5 * (attempt + 1))
            return ([], None)

    async def crawl_chapter(
        self,
        chapter_slug: str,
        progress_callback: Optional[Callable[[float, str], None]] = None
    ) -> int:
        """
        Crawl all questions for a specific chapter and save them to SQLite.
        Uses concurrent pagination chains (MCQ and Numerical) to ensure 100% coverage.
        """
        update_task_progress(chapter_slug, "in_progress", 5.0, "Fetching chapter overview...", db_path=self.db_path)
        if progress_callback:
            progress_callback(5.0, "Fetching chapter overview...")

        chapter_record = get_chapter(chapter_slug, db_path=self.db_path)
        if not chapter_record:
            # Check pilot chapters
            match = next((p for p in PILOT_CHAPTERS if p["slug"] == chapter_slug), None)
            if match:
                chapter_record = ChapterModel(**match)
                upsert_chapter(chapter_record, db_path=self.db_path)
            else:
                # Try auto-discovery
                await self.discover_all_chapters()
                chapter_record = get_chapter(chapter_slug, db_path=self.db_path)
                if not chapter_record:
                    raise ValueError(f"Chapter '{chapter_slug}' not found.")

        chapter_url = chapter_record.url
        subject = chapter_record.subject

        client = await self.get_client()
        resp = await client.get(chapter_url)
        if resp.status_code != 200:
            err_msg = f"Failed to load chapter overview: HTTP {resp.status_code}"
            update_task_progress(chapter_slug, "failed", 0.0, err_msg, db_path=self.db_path)
            if progress_callback:
                progress_callback(0.0, err_msg)
            return 0

        ch_data = parse_chapter_page(resp.text, chapter_url)
        total_questions = ch_data["total_questions"]
        chapter_record.total_questions_site = total_questions
        chapter_record.title = ch_data["title"] or chapter_record.title
        upsert_chapter(chapter_record, db_path=self.db_path)

        mcq_links = ch_data["mcq_links"]
        num_links = ch_data["num_links"]
        all_links = ch_data.get("all_links", [])

        update_task_progress(
            chapter_slug, "in_progress", 10.0,
            f"Found {total_questions} questions ({len(mcq_links)} MCQ, {len(num_links)} Numerical). Starting crawl...",
            db_path=self.db_path
        )
        if progress_callback:
            progress_callback(10.0, f"Found {total_questions} questions. Starting download...")

        saved_qids: Set[str] = set()
        saved_count = 0
        lock = asyncio.Lock()

        async def crawl_chain(start_url: str):
            nonlocal saved_count
            curr_url: Optional[str] = start_url
            while curr_url:
                questions, next_url = await self._fetch_batch_url(curr_url, chapter_slug, subject)
                if not questions and not next_url:
                    break
                async with lock:
                    for q in questions:
                        if q.qid not in saved_qids:
                            upsert_question(q, db_path=self.db_path)
                            saved_qids.add(q.qid)
                            saved_count += 1
                    denom = max(total_questions, 1)
                    pct = min(10.0 + (saved_count / denom) * 85.0, 95.0)
                    msg = f"Crawled {saved_count}/{total_questions} questions ({pct:.1f}%)..."
                    update_task_progress(chapter_slug, "in_progress", pct, msg, db_path=self.db_path)
                    if progress_callback:
                        progress_callback(pct, msg)
                curr_url = next_url

        # Launch chains for MCQ and Numerical groups concurrently
        chains = []
        if mcq_links:
            u = f"{BASE_URL}{mcq_links[0]}" if mcq_links[0].startswith('/') else mcq_links[0]
            chains.append(crawl_chain(u))
        if num_links:
            u = f"{BASE_URL}{num_links[0]}" if num_links[0].startswith('/') else num_links[0]
            chains.append(crawl_chain(u))
        if not chains and all_links:
            u = f"{BASE_URL}{all_links[0]}" if all_links[0].startswith('/') else all_links[0]
            chains.append(crawl_chain(u))

        if chains:
            await asyncio.gather(*chains)

        # Mark chapter as crawled
        chapter_record.status = "crawled"
        chapter_record.crawled_at = datetime.now().isoformat()
        chapter_record.total_questions_site = max(total_questions, saved_count)
        upsert_chapter(chapter_record, db_path=self.db_path)

        final_msg = f"Completed crawl: {saved_count} questions indexed."
        update_task_progress(chapter_slug, "completed", 100.0, final_msg, db_path=self.db_path)
        if progress_callback:
            progress_callback(100.0, final_msg)

        logger.info(f"Chapter '{chapter_slug}' crawled successfully with {saved_count} questions.")
        return saved_count

    async def enqueue_chapter_crawl(self, chapter_slug: str):
        """Add a chapter slug to the background crawl queue."""
        await self._queue.put(chapter_slug)
        update_task_progress(chapter_slug, "queued", 0.0, "Queued for background crawl", db_path=self.db_path)

    async def run_background_worker(self):
        """Worker loop that continuously processes queued chapters with analysis and notes generation."""
        self._is_running = True
        logger.info("Background crawler worker started.")
        while self._is_running:
            try:
                chapter_slug = await asyncio.wait_for(self._queue.get(), timeout=2.0)
                try:
                    logger.info(f"Starting background processing for {chapter_slug}")
                    await self.crawl_chapter(chapter_slug)

                    # Run concept analysis
                    update_task_progress(chapter_slug, "in_progress", 92.0, "Analyzing concepts and linking PYQs...", db_path=self.db_path)
                    await asyncio.to_thread(analyze_chapter, chapter_slug, db_path=self.db_path)

                    # Generate revision notes (.docx & .pdf)
                    update_task_progress(chapter_slug, "in_progress", 96.0, "Generating Word and PDF notes...", db_path=self.db_path)
                    await asyncio.to_thread(generate_chapter_docx, chapter_slug, db_path=self.db_path)
                    await asyncio.to_thread(generate_chapter_pdf, chapter_slug, db_path=self.db_path)

                    update_task_progress(chapter_slug, "completed", 100.0, "Analysis and revision notes complete.", db_path=self.db_path)
                    logger.info(f"Background processing for {chapter_slug} finished successfully.")
                except Exception as e:
                    logger.error(f"Error processing chapter {chapter_slug}: {e}", exc_info=True)
                    update_task_progress(chapter_slug, "failed", 0.0, f"Error: {str(e)}", db_path=self.db_path)
                finally:
                    self._queue.task_done()
            except asyncio.TimeoutError:
                continue
            except asyncio.CancelledError:
                break
        logger.info("Background crawler worker stopped.")

    def stop_background_worker(self):
        self._is_running = False
