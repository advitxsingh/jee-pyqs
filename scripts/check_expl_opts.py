import sqlite3
import re
import json

conn = sqlite3.connect('data/jee_pyqs.db')
cur = conn.cursor()
cur.execute('SELECT qid, options_json, explanation_text FROM questions')
opt_f = []
expl_f = []

for qid, opts_str, expl in cur.fetchall():
    if opts_str:
        try:
            opts = json.loads(opts_str)
            for opt in opts:
                txt = opt.get('text', '').strip()
                if re.match(r'^f\s+[\$\w]', txt) or txt.startswith('f$') or txt.startswith('f '):
                    opt_f.append((qid, txt[:80]))
        except Exception:
            pass
    if expl:
        e_txt = expl.strip()
        if re.match(r'^f\s+[\$\w]', e_txt) or e_txt.startswith('f$') or e_txt.startswith('f '):
            expl_f.append((qid, e_txt[:80]))

print('Options starting with f:', len(opt_f))
for item in opt_f[:10]:
    print('  opt:', item)

print('Explanations starting with f:', len(expl_f))
for item in expl_f[:10]:
    print('  expl:', item)
