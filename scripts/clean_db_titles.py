import sqlite3
import re

def clean_title(title: str) -> str:
    t = re.sub(r'^KCET\s*[:-]?\s*', '', title, flags=re.IGNORECASE)
    t = re.sub(r'\s*\d{4}\s+\d+\s+questions?.*$', '', t, flags=re.IGNORECASE)
    t = re.sub(r'\s*[\d\.]+% weightage.*$', '', t, flags=re.IGNORECASE)
    t = re.sub(r'\s*[\u2191\u2193\?].*$', '', t)
    return t.strip()

conn = sqlite3.connect('data/jee_pyqs.db')
cur = conn.cursor()

cur.execute("SELECT id, slug, title FROM chapters")
rows = cur.fetchall()

updated = 0
for cid, slug, title in rows:
    cl = clean_title(title)
    if cl != title:
        cur.execute("UPDATE chapters SET title = ? WHERE id = ?", (cl, cid))
        updated += 1

conn.commit()
conn.close()
print(f"Successfully cleaned titles for {updated} chapters in SQLite database!")
