import sqlite3
import re

conn = sqlite3.connect('data/jee_pyqs.db')
cur = conn.cursor()

print("--- 1. Checking for truncated leading words in questions ---")
cur.execute("SELECT qid, chapter_slug, question_text FROM questions")
q_rows = cur.fetchall()

leading_patterns = [
    (r'^f\s+[\$\w]', "If -> f"),
    (r'^hen\s+[\$\w]', "Then -> hen"),
    (r'^et\s+[\$\w]', "Let -> et"),
    (r'^onsider\s+[\$\w]', "Consider -> onsider"),
    (r'^uppose\s+[\$\w]', "Suppose -> uppose"),
    (r'^ind\s+[\$\w]', "Find -> ind"),
    (r'^hich\s+[\$\w]', "Which -> hich"),
    (r'^hat\s+[\$\w]', "What -> hat"),
    (r'^alculate\s+[\$\w]', "Calculate -> alculate"),
    (r'^[a-z]\s+\$', "single letter lowercase + $"),
]

for pat, desc in leading_patterns:
    matches = [r for r in q_rows if re.search(pat, r[2])]
    print(f"Pattern '{desc}': {len(matches)} matches")
    for m in matches[:5]:
        print(f"   [{m[0]}] in [{m[1]}]: {m[2][:80]}")

print("\n--- 2. Checking for \\t (tab character) in questions and concepts ---")
cur.execute("SELECT qid, question_text FROM questions WHERE question_text LIKE '%\t%'")
tab_q = cur.fetchall()
print(f"Questions with \\t: {len(tab_q)}")
for m in tab_q[:5]:
    print(f"   [{m[0]}]: {repr(m[1][:80])}")

cur.execute("SELECT id, name, summary, standard_formulas FROM concepts WHERE summary LIKE '%\t%' OR standard_formulas LIKE '%\t%'")
tab_c = cur.fetchall()
print(f"Concepts with \\t: {len(tab_c)}")
for m in tab_c[:10]:
    print(f"   [{m[0]} - {m[1]}]: {repr(m[2][:60])} | {repr(m[3][:60])}")

print("\n--- 3. Checking for replacement character  across all tables ---")
for table, col in [('questions', 'question_text'), ('questions', 'explanation_text'), 
                   ('concepts', 'summary'), ('concepts', 'standard_formulas'),
                   ('chapter_syntheses', 'title'), ('chapter_syntheses', 'summary_markdown')]:
    cur.execute(f"SELECT COUNT(*) FROM {table} WHERE {col} LIKE '%%'")
    cnt = cur.fetchone()[0]
    print(f"  {table}.{col} with : {cnt}")

print("\n--- 4. Checking questions year ranges ---")
cur.execute("SELECT DISTINCT exam, year, count(*) FROM questions GROUP BY exam, year ORDER BY exam, year")
for r in cur.fetchall():
    if r[1] > 2026 or r[1] < 2000:
        print(f"  Suspicious year: {r}")

print("\n--- 5. Checking for question order indices ---")
cur.execute("SELECT question_index, count(*) FROM questions GROUP BY question_index ORDER BY count(*) DESC LIMIT 10")
print("Top question_index values:", cur.fetchall())
