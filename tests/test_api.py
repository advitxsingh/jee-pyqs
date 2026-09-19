"""
Integration tests for FastAPI REST API and Dashboard.
"""

import unittest
from fastapi.testclient import TestClient
from app.web.app import app


class TestAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    def test_dashboard_homepage(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)
        self.assertIn("JEE Main PYQs Concept Studio", resp.text)

    def test_get_chapters(self):
        resp = self.client.get("/api/chapters")
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        
        # Check pilot chapters exist
        slugs = [c["slug"] for c in data]
        self.assertIn("electrochemistry", slugs)
        self.assertIn("vector-algebra", slugs)
        self.assertIn("alternating-current", slugs)
        self.assertIn("electromagnetic-induction", slugs)

    def test_get_chapter_detail(self):
        resp = self.client.get("/api/chapter/electrochemistry")
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertEqual(data["chapter"]["slug"], "electrochemistry")
        self.assertEqual(data["total_questions"], 226)
        self.assertGreater(len(data["concepts"]), 0)
        self.assertIsNotNone(data["synthesis"])
        self.assertTrue(data["has_docx"])
        self.assertTrue(data["has_pdf"])

    def test_get_chapter_questions(self):
        resp = self.client.get("/api/chapter/electrochemistry/questions?limit=10")
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertEqual(data["total"], 226)
        self.assertEqual(len(data["questions"]), 10)
        q0 = data["questions"][0]
        self.assertIn("qid", q0)
        self.assertIn("question_text", q0)
        self.assertIn("correct_answer", q0)

    def test_get_concept_pyqs(self):
        # Fetch chapter concepts first
        c_resp = self.client.get("/api/chapter/electrochemistry")
        concepts = c_resp.json()["concepts"]
        self.assertGreater(len(concepts), 0)
        cid = concepts[0]["id"]
        
        resp = self.client.get(f"/api/concept/{cid}/pyqs")
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertIn("pyqs", data)
        self.assertGreater(len(data["pyqs"]), 0)

    def test_export_docx_endpoint(self):
        resp = self.client.get("/api/export/electrochemistry/docx")
        self.assertEqual(resp.status_code, 200)
        self.assertIn("application/vnd.openxmlformats-officedocument", resp.headers["content-type"])
        self.assertGreater(len(resp.content), 10000)

    def test_export_pdf_endpoint(self):
        resp = self.client.get("/api/export/electrochemistry/pdf")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.headers["content-type"], "application/pdf")
        self.assertGreater(len(resp.content), 5000)

    def test_trigger_crawl_endpoint(self):
        resp = self.client.post("/api/crawl/electrochemistry")
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertEqual(data["status"], "enqueued")
        self.assertEqual(data["chapter"], "electrochemistry")

    def test_trigger_crawl_all_endpoint(self):
        resp = self.client.post("/api/crawl-all")
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertEqual(data["status"], "enqueued")
        self.assertIn("pending_chapters_count", data)


if __name__ == '__main__':
    unittest.main()
