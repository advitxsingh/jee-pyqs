"""
Static Site & JSON Dataset Exporter for GitHub Pages and Vercel.
Exports all crawled chapters, concept matrixes, PYQs, and downloadable PDF/Word booklets
into a standalone static web distribution in `dist/` for zero-server hosting and phone access.
"""

import os
import sys
import json
import shutil
from pathlib import Path

# Ensure utf-8 output on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Add project root to sys.path
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

from app.db.database import (
    get_all_chapters,
    get_chapter,
    get_questions_by_chapter,
    get_concepts_by_chapter,
    get_chapter_synthesis,
    get_question_count_by_chapter
)


def export_static_site(output_dir: str = "dist"):
    out_path = BASE_DIR / output_dir
    api_dir = out_path / "data" / "api"
    exports_dir = out_path / "exports"

    # Ensure clean directory structure
    api_dir.mkdir(parents=True, exist_ok=True)
    exports_dir.mkdir(parents=True, exist_ok=True)

    print(f"🚀 Building static web distribution for Vercel / GitHub Pages at: {out_path}")

    # 1. Export All Chapters List
    chapters = get_all_chapters()
    chapters_data = []
    for ch in chapters:
        d = ch.model_dump()
        d["stored_questions"] = get_question_count_by_chapter(ch.slug)
        chapters_data.append(d)

    with open(api_dir / "chapters.json", "w", encoding="utf-8") as f:
        json.dump(chapters_data, f, indent=2, ensure_ascii=False)
    print(f"  ✓ Exported {len(chapters_data)} chapters to data/api/chapters.json")

    total_exported_questions = 0
    total_exported_concepts = 0

    # 2. Export per-chapter details and questions
    for ch in chapters:
        slug = ch.slug
        concepts = get_concepts_by_chapter(slug)
        synthesis = get_chapter_synthesis(slug)
        questions = get_questions_by_chapter(slug, limit=5000)

        # Check export files
        has_docx = (BASE_DIR / "data" / "exports" / f"{slug}_revision_notes.docx").exists()
        has_pdf = (BASE_DIR / "data" / "exports" / f"{slug}_revision_notes.pdf").exists()

        # Chapter details JSON
        chapter_payload = {
            "chapter": ch.model_dump(),
            "concepts": [c.model_dump() for c in concepts],
            "synthesis": synthesis.model_dump() if synthesis else None,
            "total_questions": len(questions),
            "has_docx": has_docx,
            "has_pdf": has_pdf
        }

        with open(api_dir / f"chapter_{slug}.json", "w", encoding="utf-8") as f:
            json.dump(chapter_payload, f, indent=2, ensure_ascii=False)

        # Questions JSON
        questions_payload = {
            "chapter_slug": slug,
            "total": len(questions),
            "questions": [q.model_dump() for q in questions]
        }

        with open(api_dir / f"questions_{slug}.json", "w", encoding="utf-8") as f:
            json.dump(questions_payload, f, indent=2, ensure_ascii=False)

        total_exported_questions += len(questions)
        total_exported_concepts += len(concepts)
        if len(questions) > 0:
            print(f"  ✓ Chapter [{slug}]: {len(questions)} PYQs, {len(concepts)} concepts exported")

    # 3. Copy Exported PDF and DOCX Booklets
    src_exports = BASE_DIR / "data" / "exports"
    if src_exports.exists():
        copied_count = 0
        for item in src_exports.glob("*.*"):
            if item.suffix.lower() in [".pdf", ".docx", ".md"]:
                shutil.copy2(item, exports_dir / item.name)
                copied_count += 1
        print(f"  ✓ Copied {copied_count} printable revision booklets (.pdf, .docx) to dist/exports/")

    # 4. Copy index.html as main entry point
    src_html = BASE_DIR / "app" / "web" / "templates" / "index.html"
    if src_html.exists():
        shutil.copy2(src_html, out_path / "index.html")
        print(f"  ✓ Bundled standalone index.html (Dark Mode + KaTeX enabled)")

    # 5. Generate vercel.json for 1-click Vercel Deployment
    vercel_config = {
        "version": 2,
        "cleanUrls": True,
        "trailingSlash": False,
        "headers": [
            {
                "source": "/(.*)",
                "headers": [
                    {"key": "Access-Control-Allow-Origin", "value": "*"},
                    {"key": "X-Content-Type-Options", "value": "nosniff"}
                ]
            }
        ]
    }
    with open(out_path / "vercel.json", "w", encoding="utf-8") as f:
        json.dump(vercel_config, f, indent=2)
    print(f"  ✓ Generated vercel.json for instant 1-click Vercel deployment")

    print("\n" + "="*70)
    print("🎉 STATIC BUNDLE READY FOR GITHUB / VERCEL DEPLOYMENT!")
    print(f"  • Total Questions: {total_exported_questions}")
    print(f"  • Core Concepts:   {total_exported_concepts}")
    print(f"  • Destination:     {out_path}")
    print("="*70)
    print("How to deploy:")
    print("  1. Push this repository to GitHub.")
    print("  2. On Vercel: Import repo -> Set Root Directory to 'dist' -> Deploy!")
    print("  3. Or on GitHub Pages: Settings -> Pages -> Deploy from 'dist' folder or gh-pages branch.")
    print("="*70 + "\n")


if __name__ == "__main__":
    export_static_site()
