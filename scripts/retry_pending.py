"""
Resilient Crawler and Analyzer for any remaining pending JEE / KCET chapters.
Features exponential backoff retries on network blips and full static export upon completion.
"""

import sys
import os
import time
import asyncio
import logging
from pathlib import Path
from typing import List, Set

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

import httpx
from app.crawler.page_parser import parse_chapter_page, parse_question_batch_page
from app.db.database import (
    init_db, upsert_chapter, upsert_question, get_all_chapters,
    get_question_count_by_chapter, DB_PATH
)
from app.db.models import ChapterModel
from app.analyzer.analyzer_service import analyze_chapter
from app.exporter.docx_exporter import generate_chapter_docx
from app.exporter.pdf_exporter import generate_chapter_pdf
from export_static import export_static_site

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("retry_crawler")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}
BASE_URL = "https://questions.examside.com"


async def fetch_with_retry(client: httpx.AsyncClient, url: str, max_retries: int = 4, backoff: float = 1.5) -> httpx.Response:
    for attempt in range(max_retries):
        try:
            resp = await client.get(url, timeout=35.0)
            if resp.status_code == 200:
                return resp
            logger.warning(f"Fetch {url} HTTP {resp.status_code}, attempt {attempt + 1}/{max_retries}")
        except Exception as e:
            logger.warning(f"Fetch {url} error: {e}, attempt {attempt + 1}/{max_retries}")
        await asyncio.sleep(backoff * (attempt + 1))
    return None


async def crawl_and_analyze_single(client: httpx.AsyncClient, semaphore: asyncio.Semaphore, chapter: ChapterModel) -> int:
    slug = chapter.slug
    subject = chapter.subject
    url = chapter.url
    exam = "KCET" if slug.startswith("kcet-") else "JEE Main"

    async with semaphore:
        t0 = time.time()
        logger.info(f"[{exam}] Processing: '{chapter.title}' ({slug})")

        resp = await fetch_with_retry(client, url)
        if not resp:
            logger.error(f"[{slug}] Failed overview after retries.")
            return 0

        ch_data = parse_chapter_page(resp.text, url)
        all_links = ch_data.get("all_links", [])
        total_links = len(all_links)
        logger.info(f"[{slug}] Found {total_links} question links.")

        if total_links == 0:
            chapter.status = "analyzed"
            chapter.total_questions_site = 0
            upsert_chapter(chapter, db_path=DB_PATH)
            return 0

        batch_urls = []
        for i, link in enumerate(all_links):
            if i % 4 == 0 or i == total_links - 1:
                u = f"{BASE_URL}{link}" if link.startswith('/') else link
                batch_urls.append(u)

        tasks = [fetch_with_retry(client, bu) for bu in batch_urls]
        batch_resps = await asyncio.gather(*tasks, return_exceptions=True)

        saved_qids: Set[str] = set()
        saved_count = 0
        for r, bu in zip(batch_resps, batch_urls):
            if r and isinstance(r, httpx.Response) and r.status_code == 200:
                try:
                    questions, _ = parse_question_batch_page(r.text, bu, slug, subject)
                    for q in questions:
                        if q.qid not in saved_qids:
                            q.chapter_slug = slug
                            q.subject = subject
                            q.exam = exam
                            upsert_question(q, db_path=DB_PATH)
                            saved_qids.add(q.qid)
                            saved_count += 1
                except Exception as e:
                    logger.debug(f"[{slug}] Parse error for {bu}: {e}")

        chapter.total_questions_site = max(total_links, saved_count)
        chapter.status = "crawled"
        upsert_chapter(chapter, db_path=DB_PATH)
        logger.info(f"[{slug}] Crawled {saved_count} questions in {time.time() - t0:.1f}s.")

        if saved_count > 0:
            try:
                await asyncio.to_thread(analyze_chapter, slug, db_path=DB_PATH)
                await asyncio.to_thread(generate_chapter_docx, slug, db_path=DB_PATH)
                await asyncio.to_thread(generate_chapter_pdf, slug, db_path=DB_PATH)
            except Exception as e:
                logger.error(f"[{slug}] Analysis/export error: {e}")

        logger.info(f"[{slug}] ✓ Finished in {time.time() - t0:.1f}s.")
        return saved_count


async def run_retry_loop(exam_scope: str = "jee", max_passes: int = 5, concurrency: int = 4):
    init_db(DB_PATH)
    semaphore = asyncio.Semaphore(concurrency)
    limits = httpx.Limits(max_connections=25, max_keepalive_connections=12)

    for pass_num in range(1, max_passes + 1):
        all_chs = get_all_chapters(db_path=DB_PATH)
        pending = [
            c for c in all_chs
            if c.status != "analyzed" and (
                (exam_scope == "jee" and not c.slug.startswith("kcet-")) or
                (exam_scope == "kcet" and c.slug.startswith("kcet-")) or
                (exam_scope == "all")
            )
        ]

        if not pending:
            logger.info(f"🎉 Pass {pass_num}: Zero pending chapters remaining! All done.")
            break

        logger.info(f"🔁 Pass {pass_num}/{max_passes}: {len(pending)} pending chapters remaining.")

        async with httpx.AsyncClient(headers=HEADERS, timeout=35.0, limits=limits) as client:
            batch_size = 6
            for i in range(0, len(pending), batch_size):
                chunk = pending[i:i + batch_size]
                tasks = [crawl_and_analyze_single(client, semaphore, ch) for ch in chunk]
                await asyncio.gather(*tasks, return_exceptions=True)
                await asyncio.sleep(0.5)

    # Final export
    logger.info("Regenerating static distribution...")
    export_static_site()
    logger.info("✅ All done!")


if __name__ == "__main__":
    exam = sys.argv[1] if len(sys.argv) > 1 else "jee"
    asyncio.run(run_retry_loop(exam_scope=exam))
