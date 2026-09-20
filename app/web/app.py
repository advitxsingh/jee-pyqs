"""
FastAPI Web Dashboard for JEE Main PYQ Concept Analyzer.
Provides REST APIs for chapters, questions, concepts, exports, and live crawler control.
"""

import os
import asyncio
from typing import Optional, List, Dict, Any
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.db.database import (
    init_db, get_all_chapters, get_chapter, get_questions_by_chapter,
    get_question_by_id, get_concepts_by_chapter, get_pyqs_for_concept,
    get_chapter_synthesis, get_latest_task_status, get_question_count_by_chapter,
    upsert_chapter, DB_PATH
)
from app.db.models import ChapterModel
from app.crawler.crawler import CrawlerEngine, PILOT_CHAPTERS
from app.analyzer.analyzer_service import analyze_chapter
from app.exporter.docx_exporter import generate_chapter_docx
from app.exporter.pdf_exporter import generate_chapter_pdf

# Global crawler instance
crawler_engine = CrawlerEngine(db_path=DB_PATH, max_concurrency=5)
background_worker_task: Optional[asyncio.Task] = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    init_db(DB_PATH)
    # Ensure pilot chapters exist in DB
    for p in PILOT_CHAPTERS:
        existing = get_chapter(p["slug"], db_path=DB_PATH)
        if not existing:
            upsert_chapter(ChapterModel(**p), db_path=DB_PATH)
    # Start crawler background queue worker
    global background_worker_task
    background_worker_task = asyncio.create_task(crawler_engine.run_background_worker())
    yield
    # Shutdown
    crawler_engine.stop_background_worker()
    if background_worker_task:
        background_worker_task.cancel()
    await crawler_engine.close()


app = FastAPI(
    title="JEE Main PYQs Concept Studio",
    description="Analyze JEE Main PYQs, extract core concepts, link PYQs, and generate revision notes.",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure exports directory exists
os.makedirs("data/exports", exist_ok=True)
os.makedirs("app/web/static", exist_ok=True)
app.mount("/static", StaticFiles(directory="app/web/static"), name="static")


# --- API Endpoints ---

@app.get("/api/chapters")
async def list_chapters(subject: Optional[str] = None, exam: Optional[str] = None):
    """List all chapters with their question counts and status."""
    chapters = get_all_chapters(subject=subject, exam=exam, db_path=DB_PATH)
    res = []
    for ch in chapters:
        d = ch.model_dump()
        d["stored_questions"] = get_question_count_by_chapter(ch.slug, db_path=DB_PATH)
        d["exam"] = "kcet" if ch.slug.startswith("kcet-") else "jee-main"
        res.append(d)
    return res


@app.get("/api/chapter/{slug}")
async def get_chapter_detail(slug: str):
    """Retrieve chapter details, concepts, and synthesized notes."""
    chapter = get_chapter(slug, db_path=DB_PATH)
    if not chapter:
        raise HTTPException(status_code=404, detail="Chapter not found")

    concepts = get_concepts_by_chapter(slug, db_path=DB_PATH)
    synthesis = get_chapter_synthesis(slug, db_path=DB_PATH)
    question_count = get_question_count_by_chapter(slug, db_path=DB_PATH)

    # Check if exports exist
    docx_file = f"data/exports/{slug}_revision_notes.docx"
    pdf_file = f"data/exports/{slug}_revision_notes.pdf"

    return {
        "chapter": chapter.model_dump(),
        "total_questions": question_count,
        "concepts": [c.model_dump() for c in concepts],
        "synthesis": synthesis.model_dump() if synthesis else None,
        "has_docx": os.path.exists(docx_file),
        "has_pdf": os.path.exists(pdf_file)
    }


@app.get("/api/chapter/{slug}/questions")
async def list_chapter_questions(
    slug: str,
    year: Optional[int] = Query(None),
    qtype: Optional[str] = Query(None),
    difficulty: Optional[str] = Query(None),
    search: Optional[str] = Query(None),
    concept: Optional[str] = Query(None),
    limit: int = Query(50, le=200),
    offset: int = Query(0)
):
    """List questions for a chapter with filtering."""
    questions = get_questions_by_chapter(
        slug,
        year=year,
        qtype=qtype,
        difficulty=difficulty,
        search=search,
        limit=5000,  # fetch full chapter questions to filter accurately
        offset=0,
        db_path=DB_PATH
    )

    if concept:
        questions = [q for q in questions if concept.lower() in [c.lower() for c in q.key_concepts]]

    total_count = len(questions)
    paged = questions[offset:offset + limit]

    return {
        "total": total_count,
        "limit": limit,
        "offset": offset,
        "questions": [q.model_dump() for q in paged]
    }


@app.get("/api/question/{qid_or_id}")
async def get_question(qid_or_id: str):
    """Retrieve full details of a single question."""
    q = get_question_by_id(qid_or_id, db_path=DB_PATH)
    if not q:
        raise HTTPException(status_code=404, detail="Question not found")
    return q.model_dump()


@app.get("/api/concept/{concept_id}/pyqs")
async def get_concept_pyqs(concept_id: int):
    """Retrieve all PYQs linked to a specific concept."""
    pyqs = get_pyqs_for_concept(concept_id, db_path=DB_PATH)
    return {"concept_id": concept_id, "pyqs": pyqs}


@app.post("/api/crawl/{slug}")
async def trigger_crawl(slug: str):
    """Enqueue background crawling for a chapter."""
    chapter = get_chapter(slug, db_path=DB_PATH)
    if not chapter:
        raise HTTPException(status_code=404, detail="Chapter not found")

    await crawler_engine.enqueue_chapter_crawl(slug)
    return {"status": "enqueued", "chapter": slug, "message": f"Crawling and analysis queued for {slug}"}


@app.post("/api/crawl-all")
async def trigger_crawl_all():
    """Enqueue crawling for all pending chapters."""
    chapters = get_all_chapters(db_path=DB_PATH)
    pending = [c.slug for c in chapters if c.status == "pending"]

    for s in pending:
        await crawler_engine.enqueue_chapter_crawl(s)

    return {"status": "enqueued", "pending_chapters_count": len(pending)}


@app.get("/api/tasks")
async def get_tasks(slug: Optional[str] = None):
    """Get recent crawler tasks and progress."""
    return get_latest_task_status(chapter_slug=slug, db_path=DB_PATH)


@app.get("/api/export/{slug}/docx")
async def download_docx(slug: str):
    """Download Word document notes for a chapter."""
    filepath = f"data/exports/{slug}_revision_notes.docx"
    if not os.path.exists(filepath):
        generate_chapter_docx(slug, db_path=DB_PATH)
    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail="DOCX not found")
    return FileResponse(
        filepath,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        filename=f"{slug}_JEE_Main_Revision_Notes.docx"
    )


@app.get("/api/export/{slug}/pdf")
async def download_pdf(slug: str):
    """Download PDF notes for a chapter."""
    filepath = f"data/exports/{slug}_revision_notes.pdf"
    if not os.path.exists(filepath):
        generate_chapter_pdf(slug, db_path=DB_PATH)
    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail="PDF not found")
    return FileResponse(
        filepath,
        media_type="application/pdf",
        filename=f"{slug}_JEE_Main_Revision_Notes.pdf"
    )


@app.post("/api/export/{slug}/generate")
async def regenerate_exports(slug: str):
    """Force re-generation of DOCX and PDF export files."""
    docx_p = generate_chapter_docx(slug, db_path=DB_PATH)
    pdf_p = generate_chapter_pdf(slug, db_path=DB_PATH)
    return {
        "status": "success",
        "docx_path": docx_p,
        "pdf_path": pdf_p
    }


# --- Dashboard HTML Page ---

@app.get("/", response_class=HTMLResponse)
async def dashboard_page():
    """Serve the interactive web dashboard."""
    template_path = os.path.join(os.path.dirname(__file__), "templates", "index.html")
    if os.path.exists(template_path):
        with open(template_path, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    return HTMLResponse(content="<h1>JEE Main PYQs Concept Studio</h1><p>Template loading...</p>")
