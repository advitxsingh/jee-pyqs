import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent / "app" / "analyzer" / "taxonomies"

for fname in ["physics_taxonomy.py", "chemistry_taxonomy.py", "math_taxonomy.py"]:
    p = BASE / fname
    text = p.read_text(encoding="utf-8")
    # Replace lines like: "key": "...\...":
    lines = text.splitlines()
    new_lines = []
    for line in lines:
        if '\\' in line and not line.strip().startswith('#'):
            # Match "..." that don't have r in front
            # E.g. "summary": "..."
            line = re.sub(r':\s*"([^"]*?\\[^"]*?)"', r': r"\1"', line)
            line = re.sub(r'\[\s*"([^"]*?\\[^"]*?)"', r'[r"\1"', line)
            line = re.sub(r',\s*"([^"]*?\\[^"]*?)"', r', r"\1"', line)
        new_lines.append(line)
    p.write_text("\n".join(new_lines) + "\n", encoding="utf-8")

print("Successfully sanitized taxonomy escape sequences!")
