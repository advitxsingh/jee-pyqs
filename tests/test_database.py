"""
Unit tests for database models and operations.
"""

import os
import unittest
from app.db.database import (
    init_db, upsert_chapter, get_chapter, upsert_question,
    get_questions_by_chapter, save_concepts_for_chapter, get_concepts_by_chapter,
    upsert_chapter_synthesis, get_chapter_synthesis, get_question_count_by_chapter
)
from app.db.models import (
    ChapterModel, QuestionModel, OptionItem, ConceptModel,
    ConceptPYQLinkModel, ChapterSynthesisModel
)

TEST_DB = "data/test_jee.db"


class TestDatabase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        if os.path.exists(TEST_DB):
            os.remove(TEST_DB)
        init_db(TEST_DB)

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(TEST_DB):
            os.remove(TEST_DB)

    def test_chapter_upsert_and_get(self):
        ch = ChapterModel(
            subject="physics",
            slug="test-chapter",
            title="Test Chapter",
            url="https://questions.examside.com/test",
            status="pending"
        )
        upsert_chapter(ch, db_path=TEST_DB)
        retrieved = get_chapter("test-chapter", db_path=TEST_DB)
        self.assertIsNotNone(retrieved)
        self.assertEqual(retrieved.title, "Test Chapter")
        self.assertEqual(retrieved.subject, "physics")

    def test_question_upsert_and_query(self):
        q = QuestionModel(
            qid="test_qid_1",
            chapter_slug="test-chapter",
            subject="physics",
            url="https://questions.examside.com/q1",
            year=2026,
            paper_name="JEE Main 2026 8th April Evening Shift",
            shift="Evening Shift",
            question_index=1,
            question_type="MCQ",
            question_text="Find value of $x$ in $x^2 = 4$.",
            options=[OptionItem(label="A", text="2"), OptionItem(label="B", text="-2")],
            correct_answer="A",
            explanation_text="Since $x^2=4$, $x=\\pm 2$. Option A is positive root.",
            difficulty="Easy",
            key_formulas=["x^2 = 4"],
            key_concepts=["Algebra"]
        )
        upsert_question(q, db_path=TEST_DB)
        count = get_question_count_by_chapter("test-chapter", db_path=TEST_DB)
        self.assertEqual(count, 1)

        qs = get_questions_by_chapter("test-chapter", year=2026, db_path=TEST_DB)
        self.assertEqual(len(qs), 1)
        self.assertEqual(qs[0].qid, "test_qid_1")
        self.assertEqual(qs[0].correct_answer, "A")
        self.assertEqual(len(qs[0].options), 2)

    def test_concepts_and_synthesis(self):
        c = ConceptModel(
            chapter_slug="test-chapter",
            name="Quadratic Equations",
            category="Core Algebra",
            summary="Roots of ax^2+bx+c=0",
            standard_formulas="x = \\frac{-b \\pm \\sqrt{b^2-4ac}}{2a}",
            exam_frequency=5,
            frequency_tier="High"
        )
        save_concepts_for_chapter("test-chapter", [c], [], db_path=TEST_DB)
        concepts = get_concepts_by_chapter("test-chapter", db_path=TEST_DB)
        self.assertEqual(len(concepts), 1)
        self.assertEqual(concepts[0].name, "Quadratic Equations")

        synth = ChapterSynthesisModel(
            chapter_slug="test-chapter",
            title="Test Chapter Synthesis",
            summary_markdown="# Test Summary",
            formula_sheet_markdown="# Formula Sheet",
            high_yield_patterns="Pattern 1",
            traps_and_pitfalls="Trap 1"
        )
        upsert_chapter_synthesis(synth, db_path=TEST_DB)
        ret_synth = get_chapter_synthesis("test-chapter", db_path=TEST_DB)
        self.assertIsNotNone(ret_synth)
        self.assertEqual(ret_synth.title, "Test Chapter Synthesis")


if __name__ == '__main__':
    unittest.main()
