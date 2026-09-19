"""
Analyzer Service orchestrating question enrichment, concept linking,
chapter synthesis, and export generation.
"""

import logging
from typing import Dict, Any, Optional
from datetime import datetime

from app.db.database import (
    get_chapter, get_questions_by_chapter, upsert_question,
    save_concepts_for_chapter, save_concept_pyq_links, upsert_chapter_synthesis,
    upsert_chapter, get_concepts_by_chapter, DB_PATH
)
from app.analyzer.concept_extractor import analyze_chapter_questions
from app.analyzer.chapter_synthesizer import synthesize_chapter_notes
from app.db.models import ConceptPYQLinkModel

logger = logging.getLogger("jee_analyzer")


def analyze_chapter(chapter_slug: str, db_path: str = DB_PATH) -> Dict[str, Any]:
    """
    Perform full concept extraction, question enrichment, linking,
    and notes synthesis for a chapter.
    """
    chapter = get_chapter(chapter_slug, db_path=db_path)
    if not chapter:
        raise ValueError(f"Chapter '{chapter_slug}' not found in database.")

    # 1. Fetch all questions
    questions = get_questions_by_chapter(chapter_slug, limit=1000, db_path=db_path)
    if not questions:
        logger.warning(f"No questions found for chapter '{chapter_slug}' to analyze.")
        return {"status": "no_questions", "count": 0}

    logger.info(f"Analyzing {len(questions)} questions for '{chapter.title}' ({chapter_slug})...")

    # 2. Extract concepts & enrich questions
    enriched_questions, concepts, _ = analyze_chapter_questions(questions, chapter_slug)

    # 3. Update questions in database with formulas, difficulty, tags
    for eq in enriched_questions:
        upsert_question(eq, db_path=db_path)

    # 4. Save concepts to database and obtain generated IDs
    concept_map = save_concepts_for_chapter(chapter_slug, concepts, db_path=db_path)

    # Re-fetch persisted concepts with their IDs
    persisted_concepts = get_concepts_by_chapter(chapter_slug, db_path=db_path)
    concept_map = {c.name: c.id for c in persisted_concepts if c.id is not None}

    # Now create exact concept <-> PYQ links
    links: list[ConceptPYQLinkModel] = []
    for q in enriched_questions:
        if q.id:
            for cname in q.key_concepts:
                cid = concept_map.get(cname)
                if cid:
                    links.append(ConceptPYQLinkModel(
                        concept_id=cid,
                        question_id=q.id,
                        relevance_note=f"Tests {cname} in {q.year}"
                    ))
    save_concept_pyq_links(links, db_path=db_path)

    # 5. Synthesize chapter revision sheet & formulas
    synthesis = synthesize_chapter_notes(
        chapter_slug=chapter_slug,
        chapter_title=chapter.title,
        subject=chapter.subject,
        questions=enriched_questions,
        concepts=persisted_concepts
    )
    upsert_chapter_synthesis(synthesis, db_path=db_path)

    # 6. Update chapter status
    chapter.status = "analyzed"
    chapter.analyzed_at = datetime.now().isoformat()
    upsert_chapter(chapter, db_path=db_path)

    logger.info(f"Successfully analyzed '{chapter.title}': {len(persisted_concepts)} concepts extracted.")
    return {
        "status": "success",
        "chapter": chapter_slug,
        "questions_analyzed": len(enriched_questions),
        "concepts_count": len(persisted_concepts)
    }
