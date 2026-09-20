import sqlite3
import re
import json

conn = sqlite3.connect('data/jee_pyqs.db')
cur = conn.cursor()

print("1. Updating m9duqdpi...")
new_q_text = r'If $\vec{a}=2\hat{i}+\lambda\hat{j}+\hat{k}$ and $\vec{b}=\hat{i}+2\hat{j}+3\hat{k}$ are orthogonal, then value of $\lambda$ is'
new_expl = r'$\begin{aligned} & \text{We have,} \\ & \begin{aligned} \vec{a} & =2\hat{i}+\lambda\hat{j}+\hat{k} \\ \text{and} \; \vec{b} & =\hat{i}+2\hat{j}+3\hat{k} \end{aligned} \end{aligned}$ Since $\vec{a}$ and $\vec{b}$ are orthogonal, $\vec{a} \cdot \vec{b} = 0$: $\begin{aligned} \Rightarrow & (2\hat{i}+\lambda\hat{j}+\hat{k}) \cdot (\hat{i}+2\hat{j}+3\hat{k})=0 \\ \Rightarrow & 2(1) + \lambda(2) + 1(3) = 0 \\ \Rightarrow & 2\lambda+5=0 \\ \Rightarrow & \lambda=-\frac{5}{2} \end{aligned}$'
new_formulas = json.dumps([r"\vec{a}=2\hat{i}+\lambda\hat{j}+\hat{k}", r"\vec{b}=\hat{i}+2\hat{j}+3\hat{k}", r"\vec{a} \cdot \vec{b} = 0"])

cur.execute("""
    UPDATE questions 
    SET question_text = ?, explanation_text = ?, correct_answer = 'D', key_formulas_json = ?
    WHERE qid = 'm9duqdpi'
""", (new_q_text, new_expl, new_formulas))

print("2. Fixing other vector questions where a=... or b=... should have vector notation or $ missing...")
# Fix XLd4i0VsYtBkRaHaQmAcd
cur.execute("UPDATE questions SET question_text = REPLACE(question_text, 'n $-$ digit', '$n$-digit') WHERE qid = 'XLd4i0VsYtBkRaHaQmAcd'")

# Check other questions in vector algebra with unvectorized a = or b =
cur.execute("SELECT qid, question_text FROM questions WHERE chapter_slug LIKE '%vector%' AND question_text LIKE '%$a=%'")
rows = cur.fetchall()
print(f"Found {len(rows)} vector questions with $a=...")
for qid, txt in rows:
    new_t = re.sub(r'(^|\s)\$a=', r'\1$\\vec{a}=', txt)
    new_t = re.sub(r'(^|\s)and\s+b=', r'\1and $\\vec{b}=', new_t)
    new_t = re.sub(r'(^|\s)\$b=', r'\1$\\vec{b}=', new_t)
    new_t = re.sub(r'(^|\s)\$c=', r'\1$\\vec{c}=', new_t)
    cur.execute("UPDATE questions SET question_text = ? WHERE qid = ?", (new_t, qid))

print("3. Fixing \\t tabs in concepts...")
cur.execute("SELECT id, summary, standard_formulas, common_traps, tips_and_tricks FROM concepts WHERE summary LIKE '%\t%' OR standard_formulas LIKE '%\t%' OR common_traps LIKE '%\t%' OR tips_and_tricks LIKE '%\t%'")
c_rows = cur.fetchall()
print(f"Found {len(c_rows)} concepts with tab characters")

def fix_tabs(s):
    if not s:
        return s
    # Map tabs followed by command fragments:
    # \tan -> \t + an
    s = s.replace('\tan', r'\tan')
    s = s.replace('\text', r'\text')
    s = s.replace('\theta', r'\theta')
    s = s.replace('\tau', r'\tau')
    s = s.replace('\times', r'\times')
    s = s.replace('\to', r'\to')
    # Any remaining raw tab replace with space
    s = s.replace('\t', ' ')
    return s

for cid, sm, sf, ct, tt in c_rows:
    cur.execute("""
        UPDATE concepts 
        SET summary = ?, standard_formulas = ?, common_traps = ?, tips_and_tricks = ?
        WHERE id = ?
    """, (fix_tabs(sm), fix_tabs(sf), fix_tabs(ct), fix_tabs(tt), cid))

print("4. Fixing \\ufffd in chapter_syntheses...")
cur.execute("SELECT id, title, summary_markdown FROM chapter_syntheses WHERE title LIKE '%\ufffd%' OR summary_markdown LIKE '%\ufffd%'")
s_rows = cur.fetchall()
print(f"Found {len(s_rows)} syntheses with \\ufffd")
for sid, title, sm in s_rows:
    t_fixed = title.replace('\ufffd', '—').replace('  ', ' ')
    sm_fixed = sm.replace('\ufffd', '—')
    cur.execute("UPDATE chapter_syntheses SET title = ?, summary_markdown = ? WHERE id = ?", (t_fixed, sm_fixed, sid))

conn.commit()
conn.close()
print("All database cleaning completed successfully!")
