import sqlite3
import re

conn = sqlite3.connect('data/jee_pyqs.db')
cur = conn.cursor()
cur.execute('SELECT qid, chapter_slug, question_text, explanation_text FROM questions')
rows = cur.fetchall()
print(f'Total questions in DB: {len(rows)}')

issues_f_dollar = []
issues_start_lower = []
for qid, ch, text, expl in rows:
    if not text:
        continue
    # Check if text starts with f followed by space or dollar
    if re.match(r'^f\s*[\$\\]', text) or text.startswith('f '):
        issues_f_dollar.append((qid, ch, text[:100]))
    elif re.match(r'^[a-z]\s*[\$]', text):
        issues_start_lower.append((qid, ch, text[:100]))

print(f'Issues starting with f $ or f: {len(issues_f_dollar)}')
for item in issues_f_dollar:
    print("  ", item)

print(f'\nOther issues starting with single lowercase + $: {len(issues_start_lower)}')
for item in issues_start_lower[:30]:
    print("  ", item)
