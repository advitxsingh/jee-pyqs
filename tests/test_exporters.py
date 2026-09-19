"""
Unit tests for DOCX and PDF exporters.
"""

import os
import unittest
from app.db.database import (
    init_db, upsert_chapter, upsert_question, save_concepts_for_chapter,
    upsert_chapter_synthesis
)
from app.db.models import (
    ChapterModel, QuestionModel, OptionItem, ConceptModel, ChapterSynthesisModel
)
from app.exporter.docx_exporter import generate_chapter_docx
from app.exporter.pdf_exporter import generate_chapter_pdf

TEST_DB = "data/test_exporter.db"


class TestExporters(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        if os.path.exists(TEST_DB):
            os.remove(TEST_DB)
        init_db(TEST_DB)

        ch = ChapterModel(
            subject="physics",
            slug="exporter-test",
            title="Exporter Test Chapter",
            url="http://test.com",
            status="analyzed"
        )
        upsert_chapter(ch, db_path=TEST_DB)

        q = QuestionModel(
            qid="exp_q1",
            chapter_slug="exporter-test",
            subject="physics",
            url="http://test.com/q1",
            year=2026,
            paper_name="JEE Main 2026 8th April Evening Shift",
            shift="Evening Shift",
            question_index=1,
            question_type="MCQ",
            question_text=r"Calculate the resonance frequency $\omega_0 = \frac{1}{\sqrt{LC}}$ for $L=10\text{ mH}, C=1\mu\text{F}$.",
            options=[
                OptionItem(label="A", text=r"$10^4\text{ rad/s}$"),
                OptionItem(label="B", text=r"$10^5\text{ rad/s}$")
            ],
            correct_answer="A",
            explanation_text=r"At resonance, $\omega_0 = \frac{1}{\sqrt{LC}} = \frac{1}{\sqrt{10\times 10^{-3}\times 10^{-6}}} = 10^4\text{ rad/s}$. Option (A) is correct.",
            difficulty="Medium",
            key_formulas=[r"\omega_0 = \frac{1}{\sqrt{LC}}"],
            key_concepts=["Resonance in AC Circuits"]
        )
        upsert_question(q, db_path=TEST_DB)

        c = ConceptModel(
            chapter_slug="exporter-test",
            name="Resonance in AC Circuits",
            category="Circuits",
            summary="Conditions where inductive reactance balances capacitive reactance.",
            standard_formulas=r"\omega_0 = \frac{1}{\sqrt{LC}}, \quad Z = R",
            exam_frequency=12,
            frequency_tier="Very High",
            common_traps="Do not assume voltage across L and C is zero at resonance; it is magnified by Q.",
            tips_and_tricks="Quality factor Q = (1/R)*sqrt(L/C)."
        )
        save_concepts_for_chapter("exporter-test", [c], [], db_path=TEST_DB)

        syn = ChapterSynthesisModel(
            chapter_slug="exporter-test",
            title="Exporter Test Chapter Concept Synthesis",
            summary_markdown="# Exporter Summary\nDetails here.",
            formula_sheet_markdown="# Formula Sheet\n$Z=R$",
            high_yield_patterns="Pattern details",
            traps_and_pitfalls="Trap details",
            benchmark_pyq_ids=[1]
        )
        upsert_chapter_synthesis(syn, db_path=TEST_DB)

    @classmethod
    def tearDownClass(cls):
        for path in [
            TEST_DB,
            "data/exports/test_notes.docx",
            "data/exports/test_notes.pdf"
        ]:
            if os.path.exists(path):
                try:
                    os.remove(path)
                except Exception:
                    pass

    def test_generate_docx(self):
        out_path = "data/exports/test_notes.docx"
        res = generate_chapter_docx("exporter-test", output_path=out_path, db_path=TEST_DB)
        self.assertTrue(os.path.exists(res))
        self.assertGreater(os.path.getsize(res), 5000)

    def test_generate_pdf(self):
        out_path = "data/exports/test_notes.pdf"
        res = generate_chapter_pdf("exporter-test", output_path=out_path, db_path=TEST_DB)
        self.assertTrue(os.path.exists(res))
        self.assertGreater(os.path.getsize(res), 3000)


if __name__ == '__main__':
    unittest.main()
