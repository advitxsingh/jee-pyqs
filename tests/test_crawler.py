import unittest
import asyncio
import tempfile
import os
from unittest.mock import AsyncMock, patch, MagicMock
from app.crawler.crawler import CrawlerEngine, PILOT_CHAPTERS
from app.db.database import init_db
from app.db.models import ChapterModel


class TestCrawlerEngine(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.temp_dir.name, "test.db")
        init_db(self.db_path)
        self.crawler = CrawlerEngine(db_path=self.db_path, max_concurrency=2)

    async def asyncTearDown(self):
        await self.crawler.close()
        self.temp_dir.cleanup()

    def test_pilot_chapters_defined(self):
        self.assertEqual(len(PILOT_CHAPTERS), 4)
        slugs = [p["slug"] for p in PILOT_CHAPTERS]
        self.assertIn("electrochemistry", slugs)
        self.assertIn("electromagnetic-induction", slugs)
        self.assertIn("alternating-current", slugs)
        self.assertIn("vector-algebra", slugs)

    async def test_enqueue_chapter_crawl(self):
        await self.crawler.enqueue_chapter_crawl("vector-algebra")
        self.assertEqual(self.crawler._queue.qsize(), 1)
        slug = await self.crawler._queue.get()
        self.assertEqual(slug, "vector-algebra")

    async def test_client_lifecycle(self):
        client = await self.crawler.get_client()
        self.assertIsNotNone(client)
        self.assertFalse(client.is_closed)
        await self.crawler.close()
        self.assertIsNone(self.crawler.client)


if __name__ == '__main__':
    unittest.main()
