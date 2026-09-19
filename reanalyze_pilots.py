import sqlite3
from app.analyzer.analyzer_service import analyze_chapter
from app.exporter.docx_exporter import generate_chapter_docx
from app.exporter.pdf_exporter import generate_chapter_pdf

conn = sqlite3.connect('data/jee_pyqs.db')
conn.execute("UPDATE chapters SET subject='mathematics' WHERE slug='vector-algebra'")
conn.execute("UPDATE questions SET subject='mathematics' WHERE chapter_slug='vector-algebra'")
conn.commit()
conn.close()

for slug in ['electrochemistry', 'electromagnetic-induction', 'alternating-current', 'vector-algebra']:
    print(f"Re-analyzing {slug}...")
    res = analyze_chapter(slug, db_path='data/jee_pyqs.db')
    docx_p = generate_chapter_docx(slug, db_path='data/jee_pyqs.db')
    pdf_p = generate_chapter_pdf(slug, db_path='data/jee_pyqs.db')
    print(f"  -> Analyzed {res['questions_analyzed']} Qs, {res['concepts_count']} concepts. DOCX & PDF generated.")

print("All 4 chapters re-analyzed and exported successfully!")
