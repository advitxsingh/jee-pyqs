"""
Unit tests for HTML page parsers and answer extractors.
"""

import unittest
from bs4 import BeautifulSoup
from app.crawler.page_parser import extract_correct_answer, parse_chapter_page


class TestPageParser(unittest.TestCase):

    def test_extract_correct_answer_mcq_standard(self):
        html = '<div class="when-answered"><div class="question q-prose">Option (B) is correct</div></div>'
        soup = BeautifulSoup(html, 'html.parser')
        ans = extract_correct_answer(soup.find('div'), 'MCQ')
        self.assertEqual(ans, 'B')

    def test_extract_correct_answer_mcq_answer_is(self):
        html = '<div class="when-answered"><p>Correct answer is Option (D)</p></div>'
        soup = BeautifulSoup(html, 'html.parser')
        ans = extract_correct_answer(soup.find('div'), 'MCQ')
        self.assertEqual(ans, 'D')

    def test_extract_correct_answer_mcq_ans_dot(self):
        html = '<div class="when-answered"><p>Ans. (A)</p></div>'
        soup = BeautifulSoup(html, 'html.parser')
        ans = extract_correct_answer(soup.find('div'), 'MCQ')
        self.assertEqual(ans, 'A')

    def test_extract_correct_answer_numerical_standard(self):
        html = '<div class="when-answered"><div class="question q-prose">Correct answer is 15</div></div>'
        soup = BeautifulSoup(html, 'html.parser')
        ans = extract_correct_answer(soup.find('div'), 'Numerical')
        self.assertEqual(ans, '15')

    def test_extract_correct_answer_numerical_float(self):
        html = '<div class="when-answered"><section><h2 class="q-section-title">Answer</h2><div class="question q-prose">Correct answer is -2.5</div></section></div>'
        soup = BeautifulSoup(html, 'html.parser')
        ans = extract_correct_answer(soup.find('div'), 'Numerical')
        self.assertEqual(ans, '-2.5')

    def test_parse_chapter_page_structure(self):
        mock_html = """
        <html>
            <head><title>Alternating Current | Physics | JEE Main - ExamSIDE.Com</title></head>
            <body>
                <h1>Alternating Current</h1>
                <section class="cp-group">
                    <h2>MCQ (Single Correct Answer)</h2>
                    <a href="/past-years/jee/question/q1-slug">Q1</a>
                    <a href="/past-years/jee/question/q2-slug">Q2</a>
                </section>
                <section class="cp-group">
                    <h2>Numerical</h2>
                    <a href="/past-years/jee/question/q3-slug">Q3</a>
                </section>
            </body>
        </html>
        """
        ch = parse_chapter_page(mock_html, "/past-years/jee/jee-main/physics/alternating-current")
        self.assertEqual(ch['title'], "Alternating Current")
        self.assertEqual(ch['subject'], "physics")
        self.assertEqual(ch['slug'], "alternating-current")
        self.assertEqual(len(ch['mcq_links']), 2)
        self.assertEqual(len(ch['num_links']), 1)
        self.assertEqual(ch['total_questions'], 3)


if __name__ == '__main__':
    unittest.main()
