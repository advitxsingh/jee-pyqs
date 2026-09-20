"""
Re-analyze all 186 JEE Main and KCET chapters using the enriched Master Taxonomy.
Extracts multiple authentic concepts per chapter, links questions,
synthesizes revision notes, regenerates DOCX/PDF booklets, and exports static distribution.
"""

import sys
import time
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

from app.db.database import get_all_chapters, DB_PATH
from app.analyzer.analyzer_service import analyze_chapter
from app.exporter.docx_exporter import generate_chapter_docx
from app.exporter.pdf_exporter import generate_chapter_pdf
from export_static import export_static_site


def run_full_reanalysis():
    chapters = get_all_chapters(db_path=DB_PATH)
    total = len(chapters)
    print(f"🚀 Starting comprehensive concept re-analysis for all {total} chapters...")

    t0 = time.time()
    success_count = 0
    total_concepts = 0

    kcet_chapters_with_multi_concepts = 0
    jee_chapters_with_multi_concepts = 0

    for i, ch in enumerate(chapters, 1):
        slug = ch.slug
        try:
            res = analyze_chapter(slug, db_path=DB_PATH)
            concept_count = res.get("concepts_count", 0)
            total_concepts += concept_count
            success_count += 1

            if concept_count > 1:
                if slug.startswith("kcet-"):
                    kcet_chapters_with_multi_concepts += 1
                else:
                    jee_chapters_with_multi_concepts += 1

            # Regenerate docx and pdf exports
            try:
                generate_chapter_docx(slug, db_path=DB_PATH)
                generate_chapter_pdf(slug, db_path=DB_PATH)
            except Exception as exp_err:
                print(f"  [Warning] Export error for {slug}: {exp_err}")

            if i % 15 == 0 or i == total:
                elapsed = time.time() - t0
                print(f"  [{i}/{total}] Processed '{ch.title}' -> {concept_count} concepts ({elapsed:.1f}s)")

        except Exception as e:
            print(f"  [Error] Failed to analyze '{slug}': {e}")

    print("\n" + "="*70)
    print(f"🎉 All {success_count}/{total} chapters successfully analyzed!")
    print(f"  • Total Core Concepts Extracted: {total_concepts}")
    print(f"  • KCET Multi-Concept Chapters: {kcet_chapters_with_multi_concepts}/95")
    print(f"  • JEE Multi-Concept Chapters:  {jee_chapters_with_multi_concepts}/91")
    print("="*70)

    print("\n📦 Regenerating static site bundle...")
    export_static_site()
    print("✅ Full re-analysis and static site generation complete!")


if __name__ == "__main__":
    run_full_reanalysis()
