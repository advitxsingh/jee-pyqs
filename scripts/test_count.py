import os
import json
import sqlite3

conn = sqlite3.connect('data/jee_pyqs.db')
cur = conn.cursor()

cur.execute("SELECT slug, title, subject FROM chapters WHERE slug LIKE 'kcet-%' ORDER BY slug")
all_kcet_chapters = cur.fetchall()
print(f"Total KCET chapters to build in taxonomy: {len(all_kcet_chapters)}")
