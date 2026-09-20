"""
SQLite Database manager for JEE PYQs Analyzer.
"""

import json
import sqlite3
import os
from datetime import datetime
from typing import List, Optional, Dict, Any
from pathlib import Path

from app.db.models import (
    ChapterModel, QuestionModel, OptionItem, ConceptModel,
    ConceptPYQLinkModel, ChapterSynthesisModel, CrawlerTaskModel
)

DB_PATH = os.environ.get("JEE_DB_PATH", "data/jee_pyqs.db")


def get_db_connection(db_path: str = DB_PATH) -> sqlite3.Connection:
    """Returns a SQLite connection with dict-like row factory and WAL mode."""
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path, timeout=30.0)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode = WAL;")
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def init_db(db_path: str = DB_PATH) -> None:
    """Initialize SQLite database tables and indexes."""
    conn = get_db_connection(db_path)
    cur = conn.cursor()

    cur.executescript("""
    CREATE TABLE IF NOT EXISTS chapters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject TEXT NOT NULL,
        slug TEXT NOT NULL UNIQUE,
        title TEXT NOT NULL,
        url TEXT NOT NULL,
        total_questions_site INTEGER DEFAULT 0,
        status TEXT DEFAULT 'pending',
        crawled_at TEXT,
        analyzed_at TEXT
    );

    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        qid TEXT NOT NULL UNIQUE,
        chapter_slug TEXT NOT NULL,
        subject TEXT NOT NULL,
        url TEXT NOT NULL,
        exam TEXT DEFAULT 'JEE Main',
        year INTEGER NOT NULL,
        paper_name TEXT NOT NULL,
        exam_date TEXT,
        shift TEXT,
        question_index INTEGER DEFAULT 0,
        question_type TEXT DEFAULT 'MCQ',
        question_text TEXT NOT NULL,
        question_html TEXT,
        options_json TEXT,
        correct_answer TEXT,
        explanation_text TEXT,
        explanation_html TEXT,
        has_image INTEGER DEFAULT 0,
        image_urls_json TEXT,
        topic_tag TEXT,
        difficulty TEXT DEFAULT 'Medium',
        key_formulas_json TEXT,
        key_concepts_json TEXT,
        crawled_at TEXT,
        FOREIGN KEY (chapter_slug) REFERENCES chapters (slug) ON DELETE CASCADE
    );

    CREATE INDEX IF NOT EXISTS idx_questions_chapter ON questions (chapter_slug);
    CREATE INDEX IF NOT EXISTS idx_questions_year ON questions (year);
    CREATE INDEX IF NOT EXISTS idx_questions_type ON questions (question_type);
    CREATE INDEX IF NOT EXISTS idx_questions_qid ON questions (qid);

    CREATE TABLE IF NOT EXISTS concepts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chapter_slug TEXT NOT NULL,
        name TEXT NOT NULL,
        category TEXT DEFAULT 'Core Concept',
        summary TEXT NOT NULL,
        standard_formulas TEXT,
        exam_frequency INTEGER DEFAULT 0,
        frequency_tier TEXT DEFAULT 'High',
        common_traps TEXT,
        tips_and_tricks TEXT,
        FOREIGN KEY (chapter_slug) REFERENCES chapters (slug) ON DELETE CASCADE
    );

    CREATE INDEX IF NOT EXISTS idx_concepts_chapter ON concepts (chapter_slug);

    CREATE TABLE IF NOT EXISTS concept_pyq_links (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        concept_id INTEGER NOT NULL,
        question_id INTEGER NOT NULL,
        relevance_note TEXT,
        UNIQUE(concept_id, question_id),
        FOREIGN KEY (concept_id) REFERENCES concepts (id) ON DELETE CASCADE,
        FOREIGN KEY (question_id) REFERENCES questions (id) ON DELETE CASCADE
    );

    CREATE INDEX IF NOT EXISTS idx_link_concept ON concept_pyq_links (concept_id);
    CREATE INDEX IF NOT EXISTS idx_link_question ON concept_pyq_links (question_id);

    CREATE TABLE IF NOT EXISTS chapter_syntheses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chapter_slug TEXT NOT NULL UNIQUE,
        title TEXT NOT NULL,
        summary_markdown TEXT NOT NULL,
        formula_sheet_markdown TEXT NOT NULL,
        high_yield_patterns TEXT,
        traps_and_pitfalls TEXT,
        benchmark_pyq_ids_json TEXT,
        updated_at TEXT,
        FOREIGN KEY (chapter_slug) REFERENCES chapters (slug) ON DELETE CASCADE
    );

    CREATE TABLE IF NOT EXISTS crawler_tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chapter_slug TEXT NOT NULL,
        status TEXT DEFAULT 'queued',
        progress_pct REAL DEFAULT 0.0,
        message TEXT,
        started_at TEXT,
        completed_at TEXT
    );
    """)

    conn.commit()
    conn.close()


# --- Chapters Operations ---

def upsert_chapter(chapter: ChapterModel, db_path: str = DB_PATH) -> int:
    """Insert or update a chapter record."""
    conn = get_db_connection(db_path)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO chapters (subject, slug, title, url, total_questions_site, status, crawled_at, analyzed_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(slug) DO UPDATE SET
            title = excluded.title,
            url = excluded.url,
            total_questions_site = CASE WHEN excluded.total_questions_site > 0 THEN excluded.total_questions_site ELSE total_questions_site END,
            status = excluded.status,
            crawled_at = COALESCE(excluded.crawled_at, crawled_at),
            analyzed_at = COALESCE(excluded.analyzed_at, analyzed_at)
    """, (
        chapter.subject, chapter.slug, chapter.title, chapter.url,
        chapter.total_questions_site, chapter.status, chapter.crawled_at, chapter.analyzed_at
    ))
    conn.commit()
    chapter_id = cur.lastrowid
    conn.close()
    return chapter_id


def get_chapter(slug: str, db_path: str = DB_PATH) -> Optional[ChapterModel]:
    """Retrieve chapter by slug."""
    conn = get_db_connection(db_path)
    row = conn.execute("SELECT * FROM chapters WHERE slug = ?", (slug,)).fetchone()
    conn.close()
    if not row:
        return None
    return ChapterModel(**dict(row))


def get_all_chapters(subject: Optional[str] = None, exam: Optional[str] = None, db_path: str = DB_PATH) -> List[ChapterModel]:
    """Retrieve all chapters, optionally filtered by subject and/or exam."""
    conn = get_db_connection(db_path)
    query = "SELECT * FROM chapters WHERE 1=1"
    params = []
    if subject:
        query += " AND subject = ?"
        params.append(subject)
    if exam:
        if exam.lower() == "kcet":
            query += " AND slug LIKE 'kcet-%'"
        elif exam.lower() in ["jee", "jee-main"]:
            query += " AND slug NOT LIKE 'kcet-%'"
    query += " ORDER BY subject, title"
    rows = conn.execute(query, params).fetchall()
    conn.close()
    return [ChapterModel(**dict(r)) for r in rows]


# --- Questions Operations ---

def upsert_question(q: QuestionModel, db_path: str = DB_PATH) -> int:
    """Insert or update a question record."""
    conn = get_db_connection(db_path)
    cur = conn.cursor()
    options_json = json.dumps([opt.model_dump() for opt in q.options])
    image_urls_json = json.dumps(q.image_urls)
    key_formulas_json = json.dumps(q.key_formulas)
    key_concepts_json = json.dumps(q.key_concepts)
    now_str = q.crawled_at or datetime.now().isoformat()

    cur.execute("""
        INSERT INTO questions (
            qid, chapter_slug, subject, url, exam, year, paper_name,
            exam_date, shift, question_index, question_type, question_text,
            question_html, options_json, correct_answer, explanation_text,
            explanation_html, has_image, image_urls_json, topic_tag,
            difficulty, key_formulas_json, key_concepts_json, crawled_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(qid) DO UPDATE SET
            question_text = excluded.question_text,
            question_html = excluded.question_html,
            options_json = excluded.options_json,
            correct_answer = excluded.correct_answer,
            explanation_text = excluded.explanation_text,
            explanation_html = excluded.explanation_html,
            has_image = excluded.has_image,
            image_urls_json = excluded.image_urls_json,
            topic_tag = COALESCE(excluded.topic_tag, topic_tag),
            difficulty = COALESCE(excluded.difficulty, difficulty),
            key_formulas_json = excluded.key_formulas_json,
            key_concepts_json = excluded.key_concepts_json
    """, (
        q.qid, q.chapter_slug, q.subject, q.url, q.exam, q.year, q.paper_name,
        q.exam_date, q.shift, q.question_index, q.question_type, q.question_text,
        q.question_html, options_json, q.correct_answer, q.explanation_text,
        q.explanation_html, 1 if q.has_image else 0, image_urls_json, q.topic_tag,
        q.difficulty, key_formulas_json, key_concepts_json, now_str
    ))
    conn.commit()
    row_id = cur.lastrowid
    conn.close()
    return row_id


def _row_to_question(row: sqlite3.Row) -> QuestionModel:
    d = dict(row)
    options_raw = json.loads(d.pop("options_json") or "[]")
    d["options"] = [OptionItem(**opt) for opt in options_raw]
    d["image_urls"] = json.loads(d.pop("image_urls_json") or "[]")
    d["key_formulas"] = json.loads(d.pop("key_formulas_json") or "[]")
    d["key_concepts"] = json.loads(d.pop("key_concepts_json") or "[]")
    d["has_image"] = bool(d.get("has_image", 0))
    return QuestionModel(**d)


def get_questions_by_chapter(
    chapter_slug: str,
    year: Optional[int] = None,
    qtype: Optional[str] = None,
    difficulty: Optional[str] = None,
    search: Optional[str] = None,
    limit: int = 500,
    offset: int = 0,
    db_path: str = DB_PATH
) -> List[QuestionModel]:
    """Retrieve questions for a chapter with optional filtering."""
    conn = get_db_connection(db_path)
    query = "SELECT * FROM questions WHERE chapter_slug = ?"
    params: List[Any] = [chapter_slug]

    if year:
        query += " AND year = ?"
        params.append(year)
    if qtype:
        query += " AND question_type = ?"
        params.append(qtype)
    if difficulty:
        query += " AND difficulty = ?"
        params.append(difficulty)
    if search:
        query += " AND (question_text LIKE ? OR explanation_text LIKE ?)"
        params.extend([f"%{search}%", f"%{search}%"])

    query += " ORDER BY year DESC, question_index ASC LIMIT ? OFFSET ?"
    params.extend([limit, offset])

    rows = conn.execute(query, params).fetchall()
    conn.close()
    return [_row_to_question(r) for r in rows]


def get_question_by_id(qid_or_id: str, db_path: str = DB_PATH) -> Optional[QuestionModel]:
    """Retrieve question by integer ID or qid string."""
    conn = get_db_connection(db_path)
    if qid_or_id.isdigit():
        row = conn.execute("SELECT * FROM questions WHERE id = ?", (int(qid_or_id),)).fetchone()
    else:
        row = conn.execute("SELECT * FROM questions WHERE qid = ?", (qid_or_id,)).fetchone()
    conn.close()
    if not row:
        return None
    return _row_to_question(row)


def get_question_count_by_chapter(chapter_slug: str, db_path: str = DB_PATH) -> int:
    """Return total questions stored for a chapter."""
    conn = get_db_connection(db_path)
    row = conn.execute("SELECT COUNT(*) as cnt FROM questions WHERE chapter_slug = ?", (chapter_slug,)).fetchone()
    conn.close()
    return row["cnt"] if row else 0


# --- Concepts & Links Operations ---

def save_concepts_for_chapter(
    chapter_slug: str,
    concepts: List[ConceptModel],
    links: Optional[List[ConceptPYQLinkModel]] = None,
    db_path: str = DB_PATH
) -> Dict[str, int]:
    """Replace concepts for a chapter and return a map of concept_name -> concept_id."""
    conn = get_db_connection(db_path)
    cur = conn.cursor()

    # Clear previous concepts for this chapter
    cur.execute("DELETE FROM concepts WHERE chapter_slug = ?", (chapter_slug,))

    concept_name_to_id: Dict[str, int] = {}
    for c in concepts:
        cur.execute("""
            INSERT INTO concepts (
                chapter_slug, name, category, summary, standard_formulas,
                exam_frequency, frequency_tier, common_traps, tips_and_tricks
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            chapter_slug, c.name, c.category, c.summary, c.standard_formulas,
            c.exam_frequency, c.frequency_tier, c.common_traps, c.tips_and_tricks
        ))
        concept_name_to_id[c.name] = cur.lastrowid

    if links:
        for l in links:
            cur.execute("""
                INSERT OR IGNORE INTO concept_pyq_links (concept_id, question_id, relevance_note)
                VALUES (?, ?, ?)
            """, (l.concept_id, l.question_id, l.relevance_note))

    conn.commit()
    conn.close()
    return concept_name_to_id


def save_concept_pyq_links(links: List[ConceptPYQLinkModel], db_path: str = DB_PATH) -> int:
    """Insert concept <-> PYQ links into database."""
    if not links:
        return 0
    conn = get_db_connection(db_path)
    cur = conn.cursor()
    cur.executemany("""
        INSERT OR IGNORE INTO concept_pyq_links (concept_id, question_id, relevance_note)
        VALUES (?, ?, ?)
    """, [(l.concept_id, l.question_id, l.relevance_note) for l in links])
    conn.commit()
    inserted = cur.rowcount
    conn.close()
    return inserted


def get_concepts_by_chapter(chapter_slug: str, db_path: str = DB_PATH) -> List[ConceptModel]:
    """Retrieve all concepts with linked PYQ IDs for a chapter."""
    conn = get_db_connection(db_path)
    rows = conn.execute("SELECT * FROM concepts WHERE chapter_slug = ? ORDER BY exam_frequency DESC", (chapter_slug,)).fetchall()
    concepts: List[ConceptModel] = []

    for r in rows:
        c_dict = dict(r)
        cid = c_dict["id"]
        # Fetch linked question IDs
        link_rows = conn.execute("SELECT question_id FROM concept_pyq_links WHERE concept_id = ?", (cid,)).fetchall()
        c_dict["pyq_ids"] = [lr["question_id"] for lr in link_rows]
        concepts.append(ConceptModel(**c_dict))

    conn.close()
    return concepts


def get_pyqs_for_concept(concept_id: int, db_path: str = DB_PATH) -> List[Dict[str, Any]]:
    """Retrieve question summaries linked to a specific concept."""
    conn = get_db_connection(db_path)
    cur = conn.cursor()
    rows = cur.execute("""
        SELECT q.id, q.qid, q.year, q.paper_name, q.question_type, q.question_text,
               q.correct_answer, q.difficulty, l.relevance_note
        FROM concept_pyq_links l
        JOIN questions q ON l.question_id = q.id
        WHERE l.concept_id = ?
        ORDER BY q.year DESC
    """, (concept_id,)).fetchall()
    conn.close()
    return [dict(r) for r in rows]


# --- Chapter Synthesis Operations ---

def upsert_chapter_synthesis(s: ChapterSynthesisModel, db_path: str = DB_PATH) -> None:
    """Save synthesized notes for a chapter."""
    conn = get_db_connection(db_path)
    cur = conn.cursor()
    now_str = s.updated_at or datetime.now().isoformat()
    cur.execute("""
        INSERT INTO chapter_syntheses (
            chapter_slug, title, summary_markdown, formula_sheet_markdown,
            high_yield_patterns, traps_and_pitfalls, benchmark_pyq_ids_json, updated_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(chapter_slug) DO UPDATE SET
            title = excluded.title,
            summary_markdown = excluded.summary_markdown,
            formula_sheet_markdown = excluded.formula_sheet_markdown,
            high_yield_patterns = excluded.high_yield_patterns,
            traps_and_pitfalls = excluded.traps_and_pitfalls,
            benchmark_pyq_ids_json = excluded.benchmark_pyq_ids_json,
            updated_at = excluded.updated_at
    """, (
        s.chapter_slug, s.title, s.summary_markdown, s.formula_sheet_markdown,
        s.high_yield_patterns, s.traps_and_pitfalls, json.dumps(s.benchmark_pyq_ids), now_str
    ))
    conn.commit()
    conn.close()


def get_chapter_synthesis(chapter_slug: str, db_path: str = DB_PATH) -> Optional[ChapterSynthesisModel]:
    """Retrieve synthesized notes for a chapter."""
    conn = get_db_connection(db_path)
    row = conn.execute("SELECT * FROM chapter_syntheses WHERE chapter_slug = ?", (chapter_slug,)).fetchone()
    conn.close()
    if not row:
        return None
    d = dict(row)
    d["benchmark_pyq_ids"] = json.loads(d.pop("benchmark_pyq_ids_json") or "[]")
    return ChapterSynthesisModel(**d)


# --- Task Tracking Operations ---

def update_task_progress(chapter_slug: str, status: str, progress_pct: float, message: str, db_path: str = DB_PATH) -> None:
    """Update background task status."""
    conn = get_db_connection(db_path)
    cur = conn.cursor()
    now_str = datetime.now().isoformat()
    cur.execute("""
        INSERT INTO crawler_tasks (chapter_slug, status, progress_pct, message, started_at)
        VALUES (?, ?, ?, ?, ?)
    """, (chapter_slug, status, progress_pct, message, now_str))
    conn.commit()
    conn.close()


def get_latest_task_status(chapter_slug: Optional[str] = None, db_path: str = DB_PATH) -> List[Dict[str, Any]]:
    """Get recent crawler task updates."""
    conn = get_db_connection(db_path)
    if chapter_slug:
        rows = conn.execute("""
            SELECT * FROM crawler_tasks WHERE chapter_slug = ? ORDER BY id DESC LIMIT 1
        """, (chapter_slug,)).fetchall()
    else:
        rows = conn.execute("""
            SELECT * FROM crawler_tasks ORDER BY id DESC LIMIT 20
        """).fetchall()
    conn.close()
    return [dict(r) for r in rows]
