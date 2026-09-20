"""
Autonomous High-Throughput Crawler and Analyzer for all JEE Main and KCET Syllabus Chapters.
Crawls all ExamSIDE chapters, extracts all questions, options, answers, and explanations,
runs concept analysis, links concepts to PYQs, and generates printable revision booklets.
"""

import sys
import os
import time
import asyncio
import argparse
import logging
from pathlib import Path
from typing import List, Dict, Any, Set, Optional

# Add project root to sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

# Ensure utf-8 output on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

import httpx
from bs4 import BeautifulSoup

from app.crawler.page_parser import parse_chapter_page, parse_question_batch_page
from app.db.database import (
    init_db, get_db_connection, upsert_chapter, get_chapter,
    upsert_question, get_all_chapters, get_question_count_by_chapter,
    DB_PATH
)
from app.db.models import ChapterModel, QuestionModel
from app.analyzer.analyzer_service import analyze_chapter
from app.exporter.docx_exporter import generate_chapter_docx
from app.exporter.pdf_exporter import generate_chapter_pdf
from export_static import export_static_site

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("all_crawler")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

BASE_URL = "https://questions.examside.com"


async def crawl_and_analyze_single_chapter(
    client: httpx.AsyncClient,
    semaphore: asyncio.Semaphore,
    chapter: ChapterModel,
    db_path: str = DB_PATH
) -> int:
    """Crawl a single chapter with concurrent batching and run analysis."""
    slug = chapter.slug
    subject = chapter.subject
    url = chapter.url
    exam = "KCET" if slug.startswith("kcet-") else "JEE Main"

    async with semaphore:
        t0 = time.time()
        logger.info(f"[{exam}] Starting crawl for: '{chapter.title}' ({slug})")

        # 1. Fetch Overview Page
        try:
            resp = await client.get(url)
            if resp.status_code != 200:
                logger.warning(f"[{slug}] Overview returned HTTP {resp.status_code}. Skipping.")
                return 0
        except Exception as e:
            logger.error(f"[{slug}] Overview request failed: {e}")
            return 0

        ch_data = parse_chapter_page(resp.text, url)
        all_links = ch_data.get("all_links", [])
        total_links = len(all_links)
        logger.info(f"[{slug}] Found {total_links} question links on ExamSIDE.")

        if total_links == 0:
            chapter.status = "analyzed"
            chapter.total_questions_site = 0
            upsert_chapter(chapter, db_path=db_path)
            return 0

        # 2. Prepare Batches (ExamSIDE displays 4 questions per batch)
        batch_urls = []
        for i, link in enumerate(all_links):
            if i % 4 == 0 or i == total_links - 1:
                u = f"{BASE_URL}{link}" if link.startswith('/') else link
                batch_urls.append(u)

        # 3. Fetch batches concurrently
        tasks = [client.get(bu) for bu in batch_urls]
        batch_resps = await asyncio.gather(*tasks, return_exceptions=True)

        saved_qids: Set[str] = set()
        saved_count = 0
        for r, bu in zip(batch_resps, batch_urls):
            if isinstance(r, httpx.Response) and r.status_code == 200:
                try:
                    questions, _ = parse_question_batch_page(r.text, bu, slug, subject)
                    for q in questions:
                        if q.qid not in saved_qids:
                            q.chapter_slug = slug
                            q.subject = subject
                            q.exam = exam
                            upsert_question(q, db_path=db_path)
                            saved_qids.add(q.qid)
                            saved_count += 1
                except Exception as e:
                    logger.debug(f"[{slug}] Error parsing batch {bu}: {e}")

        # Update chapter metadata
        chapter.total_questions_site = max(total_links, saved_count)
        chapter.status = "crawled"
        upsert_chapter(chapter, db_path=db_path)
        logger.info(f"[{slug}] Crawled {saved_count} questions in {time.time() - t0:.2f}s.")

        # 4. Run Concept Extraction & Linking
        if saved_count > 0:
            try:
                t_ana = time.time()
                await asyncio.to_thread(analyze_chapter, slug, db_path=db_path)
                logger.info(f"[{slug}] Concepts analyzed in {time.time() - t_ana:.2f}s.")

                # 5. Generate Word & PDF Revision Booklets
                await asyncio.to_thread(generate_chapter_docx, slug, db_path=db_path)
                await asyncio.to_thread(generate_chapter_pdf, slug, db_path=db_path)
            except Exception as e:
                logger.error(f"[{slug}] Analysis/document generation error: {e}")

        logger.info(f"[{slug}] ✓ Finished in {time.time() - t0:.2f}s.")
        return saved_count


async def crawl_all_syllabus(exam_scope: str = "all", concurrency: int = 4):
    """
    Crawls and analyzes all syllabus chapters.
    exam_scope can be 'all', 'kcet', or 'jee'.
    """
    init_db(DB_PATH)
    all_chapters = get_all_chapters(db_path=DB_PATH)

    # Filter chapters based on exam_scope and status
    pending_chapters = []
    for ch in all_chapters:
        is_kcet = ch.slug.startswith("kcet-")
        if exam_scope == "kcet" and not is_kcet:
            continue
        if exam_scope == "jee" and is_kcet:
            continue
        if ch.status != "analyzed":
            pending_chapters.append(ch)

    logger.info(f"🚀 Starting crawl for {len(pending_chapters)} pending chapters (Scope: {exam_scope.upper()}, Concurrency: {concurrency})")

    semaphore = asyncio.Semaphore(concurrency)
    limits = httpx.Limits(max_connections=30, max_keepalive_connections=15)

    async with httpx.AsyncClient(headers=HEADERS, timeout=30.0, limits=limits) as client:
        # Process in batches to balance speed and stability
        batch_size = 8
        for i in range(0, len(pending_chapters), batch_size):
            chunk = pending_chapters[i:i + batch_size]
            tasks = [crawl_and_analyze_single_chapter(client, semaphore, ch) for ch in chunk]
            results = await asyncio.gather(*tasks, return_exceptions=True)
            logger.info(f"Progress: Completed {min(i + batch_size, len(pending_chapters))}/{len(pending_chapters)} chapters.")
            await asyncio.sleep(0.5)

    logger.info("🎉 All pending chapters processed! Regenerating static distribution...")
    export_static_site()
    logger.info("✅ Full crawl, analysis, and static site export complete!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--exam", choices=["all", "kcet", "jee"], default="all", help="Exam scope to crawl")
    parser.add_argument("--concurrency", type=int, default=4, help="Concurrent chapter crawlers")
    args = parser.parse_args()

    asyncio.run(crawl_all_syllabus(exam_scope=args.exam, concurrency=args.concurrency))
