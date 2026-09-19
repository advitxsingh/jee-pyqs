"""
Unit tests for concept extraction and notes synthesis.
"""

import unittest
from app.db.models import QuestionModel
from app.analyzer.concept_extractor import (
    extract_formulas_from_text, estimate_difficulty, analyze_chapter_questions
)
from app.analyzer.chapter_synthesizer import synthesize_chapter_notes


class TestAnalyzer(unittest.TestCase):

    def test_extract_formulas_from_text(self):
        text = r"Given cell potential $E_{cell} = E^\circ - \frac{0.0591}{n}\log Q$ and $\Delta G = -nFE$."
        formulas = extract_formulas_from_text(text)
        self.assertTrue(len(formulas) >= 1)
        self.assertTrue(any("0.0591" in f or "nFE" in f for f in formulas))

    def test_estimate_difficulty(self):
        # Simple question
        q_easy = QuestionModel(
            qid="q_easy",
            chapter_slug="electrochemistry",
            subject="chemistry",
            url="http://test.com",
            year=2024,
            paper_name="JEE Main",
            question_type="MCQ",
            question_text="What is the unit of conductance?",
            explanation_text="Unit of conductance is Siemens (S)."
        )
        self.assertEqual(estimate_difficulty(q_easy), "Easy")

        # Multi-step complex question
        q_hard = QuestionModel(
            qid="q_hard",
            chapter_slug="electrochemistry",
            subject="chemistry",
            url="http://test.com",
            year=2024,
            paper_name="JEE Main",
            question_type="Numerical",
            question_text="Calculate the equilibrium constant $K_{eq}$ for a concentration cell involving simultaneous quadratic dissociation where $\\Delta G = -nFE$ and $\\Lambda_m = \\frac{1000\\kappa}{M}$.",
            explanation_text="Step 1: Set up the differential equation. Step 2: Solve quadratic equation for alpha. Step 3: Compute Gibbs free energy $\\Delta G = -nFE$. Step 4: Substitute $\\log K = \\frac{nE}{0.0591}$. Step 5: Final numerical evaluation gives 42." * 3
        )
        self.assertEqual(estimate_difficulty(q_hard), "Hard")

    def test_analyze_and_synthesize(self):
        q = QuestionModel(
            qid="q1",
            chapter_slug="electrochemistry",
            subject="chemistry",
            url="http://test.com",
            year=2025,
            paper_name="JEE Main 2025 29th Jan Morning",
            question_index=1,
            question_type="MCQ",
            question_text="Calculate Nernst cell potential $E_{cell}$ when $[Zn^{2+}]=0.1$ M and $[Cu^{2+}]=1$ M.",
            explanation_text=r"Using Nernst equation: $E_{cell} = E^\circ - \frac{0.0591}{2}\log Q$. Option (B) is correct.",
            correct_answer="B"
        )
        enriched_qs, concepts, _ = analyze_chapter_questions([q], "electrochemistry")
        self.assertTrue(len(concepts) >= 1)
        
        # Verify Nernst Equation concept was matched
        nernst_c = next((c for c in concepts if "Nernst" in c.name), None)
        self.assertIsNotNone(nernst_c)
        self.assertGreater(nernst_c.exam_frequency, 0)

        # Verify synthesis
        synthesis = synthesize_chapter_notes(
            chapter_slug="electrochemistry",
            chapter_title="Electrochemistry",
            subject="chemistry",
            questions=enriched_qs,
            concepts=concepts
        )
        self.assertIn("Electrochemistry", synthesis.title)
        self.assertIn("Nernst", synthesis.summary_markdown)
        self.assertIn("Master Formula Sheet", synthesis.formula_sheet_markdown)


if __name__ == '__main__':
    unittest.main()
