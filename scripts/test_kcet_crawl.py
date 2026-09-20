"""
Test pilot crawl and analysis for KCET chapters.
"""
import asyncio
import time
import httpx
from bs4 import BeautifulSoup
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.crawler.page_parser import parse_chapter_page, parse_question_batch_page
from app.db.database import upsert_question, upsert_chapter, get_chapter, get_question_count_by_chapter
from app.analyzer.analyzer_service import analyze_chapter
from app.exporter.docx_exporter import generate_chapter_docx
from app.exporter.pdf_exporter import generate_chapter_pdf

PILOT_KCET = [
    ("chemistry", "electrochemistry", "kcet-electrochemistry"),
    ("physics", "electromagnetic-induction", "kcet-electromagnetic-induction"),
    ("mathematics", "vector-algebra", "kcet-vector-algebra"),
]

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

async def crawl_kcet_chapter(client: httpx.AsyncClient, subject: str, raw_slug: str, slug: str):
    t0 = time.time()
    url = f"https://questions.examside.com/past-years/jee/kcet/{subject}/{raw_slug}"
    resp = await client.get(url)
    if resp.status_code != 200:
        print(f"[{slug}] Failed to fetch overview: HTTP {resp.status_code}")
        return 0

    ch_data = parse_chapter_page(resp.text, url)
    all_links = ch_data["all_links"]
    print(f"[{slug}] Found {len(all_links)} question links in overview.")

    batch_urls = []
    for i, link in enumerate(all_links):
        if i % 4 == 0 or i == len(all_links) - 1:
            full_u = "https://questions.examside.com" + link if link.startswith('/') else link
            batch_urls.append(full_u)

    tasks = [client.get(u) for u in batch_urls]
    resps = await asyncio.gather(*tasks, return_exceptions=True)

    saved_qids = set()
    saved = 0
    for r, u in zip(resps, batch_urls):
        if isinstance(r, httpx.Response) and r.status_code == 200:
            qs, _ = parse_question_batch_page(r.text, u, slug, subject)
            for q in qs:
                if q.qid not in saved_qids:
                    q.chapter_slug = slug
                    q.subject = subject
                    q.exam = "KCET"
                    upsert_question(q)
                    saved_qids.add(q.qid)
                    saved += 1

    ch = get_chapter(slug)
    if ch:
        ch.status = "crawled"
        ch.total_questions_site = len(all_links)
        upsert_chapter(ch)

    print(f"[{slug}] Crawled and saved {saved} questions in {time.time() - t0:.2f}s.")

    # Run analysis
    t1 = time.time()
    analyze_chapter(slug)
    print(f"[{slug}] Analyzed concepts in {time.time() - t1:.2f}s.")

    # Generate documents
    generate_chapter_docx(slug)
    generate_chapter_pdf(slug)
    print(f"[{slug}] Generated Word and PDF revision notes. Total chapter time: {time.time() - t0:.2f}s.")
    return saved

async def main():
    async with httpx.AsyncClient(headers=HEADERS, timeout=20.0, limits=httpx.Limits(max_connections=20)) as client:
        for subj, raw_slug, slug in PILOT_KCET:
            await crawl_kcet_chapter(client, subj, raw_slug, slug)

if __name__ == "__main__":
    asyncio.run(main())
