import sqlite3
from app.analyzer.taxonomies.kcet_taxonomy import KCET_TAXONOMY, get_kcet_taxonomy

conn = sqlite3.connect('data/jee_pyqs.db')
cur = conn.cursor()
cur.execute("SELECT slug FROM chapters WHERE slug LIKE 'kcet-%' ORDER BY slug")
db_slugs = [r[0] for r in cur.fetchall()]

print(f"Total DB KCET chapters: {len(db_slugs)}")
print(f"Total in KCET_TAXONOMY: {len(KCET_TAXONOMY)}")

missing = [s for s in db_slugs if not get_kcet_taxonomy(s)]
print(f"Missing taxonomies count: {len(missing)}")
if missing:
    print("Missing:", missing)
else:
    print("SUCCESS: 100% of all 95 KCET chapters have dedicated KCET concept taxonomies!")

total_concepts = sum(len(c) for c in KCET_TAXONOMY.values())
print(f"Total dedicated KCET concepts defined: {total_concepts}")
