import os
import sqlite3

conn = sqlite3.connect('data/jee_pyqs.db')
cur = conn.cursor()

chapters = cur.execute("SELECT slug, title, subject, status, total_questions_site FROM chapters WHERE status='analyzed'").fetchall()
print("=== ANALYZED CHAPTERS ===")
for ch in chapters:
    q_cnt = cur.execute("SELECT COUNT(*) FROM questions WHERE chapter_slug=?", (ch[0],)).fetchone()[0]
    c_cnt = cur.execute("SELECT COUNT(*) FROM concepts WHERE chapter_slug=?", (ch[0],)).fetchone()[0]
    l_cnt = cur.execute("SELECT COUNT(*) FROM concept_pyq_links l JOIN concepts c ON l.concept_id=c.id WHERE c.chapter_slug=?", (ch[0],)).fetchone()[0]
    print(f"{ch[1]} ({ch[2]}): {q_cnt} questions stored | {c_cnt} concepts | {l_cnt} concept-PYQ links")

total_q = cur.execute("SELECT COUNT(*) FROM questions").fetchone()[0]
total_c = cur.execute("SELECT COUNT(*) FROM concepts").fetchone()[0]
print(f"\nTotal Questions in DB: {total_q}")
print(f"Total Concepts in DB: {total_c}")
conn.close()

print("\n=== EXPORT FILES IN data/exports ===")
for f in sorted(os.listdir('data/exports')):
    fp = os.path.join('data/exports', f)
    print(f"{f} -> {os.path.getsize(fp):,} bytes")
