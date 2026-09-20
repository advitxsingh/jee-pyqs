import sqlite3
import re
from collections import Counter

conn = sqlite3.connect('data/jee_pyqs.db')
cur = conn.cursor()

cur.execute("SELECT slug, title, subject FROM chapters WHERE slug LIKE 'kcet-%' ORDER BY subject, slug")
chapters = cur.fetchall()

print(f"Analyzing {len(chapters)} KCET chapters...\n")

for slug, title, subject in chapters:
    cur.execute("SELECT question_text, explanation_text FROM questions WHERE chapter_slug = ?", (slug,))
    rows = cur.fetchall()
    if not rows:
        continue
    
    text = " ".join([f"{r[0]} {r[1]}" for r in rows]).lower()
    
    # Extract math symbols and keywords
    words = re.findall(r'[a-zA-Z]{4,}', text)
    stopwords = {
        'which', 'following', 'value', 'given', 'with', 'from', 'then', 'when', 'that', 'this',
        'have', 'each', 'will', 'what', 'where', 'also', 'statement', 'correct', 'incorrect',
        'both', 'option', 'true', 'false', 'same', 'equal', 'between', 'respect', 'find', 'calculate'
    }
    filtered = [w for w in words if w not in stopwords]
    top_words = [w for w, c in Counter(filtered).most_common(10)]
    
    # Formulas / math cues
    math_tokens = re.findall(r'\\[a-zA-Z]+', text)
    top_math = [m for m, c in Counter(math_tokens).most_common(6) if m not in {r'\frac', r'\text', r'\le', r'\ge', r'\times', r'\cdot'}]
    
    print(f"[{subject[:4].upper()}] {slug} ({len(rows)} Qs):")
    print(f"  Keywords: {', '.join(top_words[:6])}")
    if top_math:
        print(f"  Math cues: {', '.join(top_math[:4])}")
    print()
