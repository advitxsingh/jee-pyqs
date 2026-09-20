"""Fixes syntax warnings in kcet taxonomy files."""
import re

files = [
    "app/analyzer/taxonomies/kcet_physics.py",
    "app/analyzer/taxonomies/kcet_chemistry.py",
    "app/analyzer/taxonomies/kcet_math.py"
]

for fpath in files:
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace invalid escape patterns in regular strings:
    # \circ -> \\circ, \theta -> \\theta, \Delta -> \\Delta, \% -> %, \sin -> \\sin, \cos -> \\cos, \cap -> \\cap
    replacements = [
        (r'(?<!\\)\\circ', r'\\\\circ'),
        (r'(?<!\\)\\theta', r'\\\\theta'),
        (r'(?<!\\)\\Delta', r'\\\\Delta'),
        (r'(?<!\\)\\%', r'%'),
        (r'(?<!\\)\\sin', r'\\\\sin'),
        (r'(?<!\\)\\cos', r'\\\\cos'),
        (r'(?<!\\)\\cap', r'\\\\cap'),
    ]
    for pattern, rep in replacements:
        content = re.sub(pattern, rep, content)

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Fixed escapes in {fpath}")
