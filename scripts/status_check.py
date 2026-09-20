import sqlite3

def check_status():
    conn = sqlite3.connect('data/jee_pyqs.db')
    c = conn.cursor()
    c.execute('SELECT slug, status FROM chapters')
    all_ch = c.fetchall()
    kcet = [ch for ch in all_ch if ch[0].startswith('kcet-')]
    jee = [ch for ch in all_ch if not ch[0].startswith('kcet-')]
    print(f"KCET: {len(kcet)} total, {sum(1 for _, s in kcet if s in ['crawled', 'analyzed'])} analyzed, {sum(1 for _, s in kcet if s == 'pending')} pending")
    print(f"JEE:  {len(jee)} total, {sum(1 for _, s in jee if s in ['crawled', 'analyzed'])} analyzed, {sum(1 for _, s in jee if s == 'pending')} pending")
    
    c.execute("SELECT exam, count(*) FROM questions GROUP BY exam")
    for row in c.fetchall():
        print(f"  Stored Questions [{row[0]}]: {row[1]}")
    conn.close()

if __name__ == '__main__':
    check_status()
