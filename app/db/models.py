"""
Data models for JEE PYQs Analyzer.
"""

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class ChapterModel(BaseModel):
    id: Optional[int] = None
    subject: str
    slug: str
    title: str
    url: str
    total_questions_site: int = 0
    status: str = "pending"  # pending, crawling, crawled, analyzed
    crawled_at: Optional[str] = None
    analyzed_at: Optional[str] = None


class OptionItem(BaseModel):
    label: str  # A, B, C, D
    text: str
    html: Optional[str] = ""


class QuestionModel(BaseModel):
    id: Optional[int] = None
    qid: str  # Unique ExamSIDE question ID (e.g. 'mnsik71l' or slug hash)
    chapter_slug: str
    subject: str
    url: str
    exam: str = "JEE Main"
    year: int
    paper_name: str
    exam_date: Optional[str] = None
    shift: Optional[str] = None
    question_index: int = 0
    question_type: str = "MCQ"  # MCQ or Numerical
    question_text: str
    question_html: Optional[str] = ""
    options: List[OptionItem] = Field(default_factory=list)
    correct_answer: Optional[str] = None  # "A", "B", "C", "D", or "15"
    explanation_text: Optional[str] = ""
    explanation_html: Optional[str] = ""
    has_image: bool = False
    image_urls: List[str] = Field(default_factory=list)
    topic_tag: Optional[str] = None
    difficulty: Optional[str] = "Medium"  # Easy, Medium, Hard
    key_formulas: List[str] = Field(default_factory=list)
    key_concepts: List[str] = Field(default_factory=list)
    crawled_at: Optional[str] = None


class ConceptModel(BaseModel):
    id: Optional[int] = None
    chapter_slug: str
    name: str
    category: str = "Core Concept"
    summary: str
    standard_formulas: str = ""
    exam_frequency: int = 0
    frequency_tier: str = "High"  # Very High, High, Moderate
    common_traps: str = ""
    tips_and_tricks: str = ""
    pyq_ids: List[int] = Field(default_factory=list)


class ConceptPYQLinkModel(BaseModel):
    id: Optional[int] = None
    concept_id: int
    question_id: int
    relevance_note: str = ""


class ChapterSynthesisModel(BaseModel):
    id: Optional[int] = None
    chapter_slug: str
    title: str
    summary_markdown: str
    formula_sheet_markdown: str
    high_yield_patterns: str
    traps_and_pitfalls: str
    benchmark_pyq_ids: List[int] = Field(default_factory=list)
    updated_at: Optional[str] = None


class CrawlerTaskModel(BaseModel):
    id: Optional[int] = None
    chapter_slug: str
    status: str = "queued"  # queued, in_progress, completed, failed
    progress_pct: float = 0.0
    message: str = ""
    started_at: Optional[str] = None
    completed_at: Optional[str] = None
