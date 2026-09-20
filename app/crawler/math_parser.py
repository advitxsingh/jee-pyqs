"""
Robust MathJax SVG to LaTeX Converter for ExamSIDE JEE Main Questions.
ExamSIDE SSR embeds MathJax formulas where SVG <use> elements have data-c
containing hexadecimal Unicode characters and <g> elements have data-mml-node.
"""

import re
from typing import Tuple, Optional
from bs4 import BeautifulSoup, Tag, NavigableString


# Comprehensive mapping of Greek characters
GREEK_LOWER = [
    r'\alpha', r'\beta', r'\gamma', r'\delta', r'\epsilon', r'\zeta',
    r'\eta', r'\theta', r'\iota', r'\kappa', r'\lambda', r'\mu',
    r'\nu', r'\xi', 'o', r'\pi', r'\rho', r'\varsigma',
    r'\sigma', r'\tau', r'\upsilon', r'\phi', r'\chi', r'\psi', r'\omega'
]

GREEK_UPPER = {
    0x0391: r'A', 0x0392: r'B',
    0x0393: r'\Gamma', 0x0394: r'\Delta', 0x0395: r'E', 0x0396: r'Z',
    0x0397: r'H', 0x0398: r'\Theta', 0x0399: r'I', 0x039A: r'K',
    0x039B: r'\Lambda', 0x039C: r'M', 0x039D: r'N', 0x039E: r'\Xi',
    0x039F: r'O', 0x03A0: r'\Pi', 0x03A1: r'P', 0x03A3: r'\Sigma',
    0x03A4: r'T', 0x03A5: r'\Upsilon', 0x03A6: r'\Phi', 0x03A7: r'X',
    0x03A8: r'\Psi', 0x03A9: r'\Omega'
}

SPECIAL_MATH_SYMBOLS = {
    0x2296: r'^{\circ}',          # ⊖ (standard state circ)
    0x00B0: r'^{\circ}',          # ° (degree)
    0x2218: r'^{\circ}',          # ∘ ring operator / degree
    0x2212: '-',                  # − (minus sign)
    0x00D7: r' \times ',          # ×
    0x00F7: r' \div ',            # ÷
    0x00B1: r' \pm ',             # ±
    0x2213: r' \mp ',             # ∓
    0x2192: r' \rightarrow ',     # →
    0x2190: r' \leftarrow ',      # ←
    0x21D2: r' \Rightarrow ',     # ⇒
    0x21CC: r' \rightleftharpoons ', # ⇌ (chemical equilibrium)
    0x2264: r' \le ',             # ≤
    0x2265: r' \ge ',             # ≥
    0x2260: r' \ne ',             # ≠
    0x2248: r' \approx ',         # ≈
    0x2261: r' \equiv ',          # ≡
    0x221E: r'\infty',            # ∞
    0x22C5: r' \cdot ',           # ⋅
    0x00B7: r' \cdot ',           # ·
    0x02C6: r'\hat{}',            # ˆ
    0x0302: r'\hat{}',            # ̂
    0x20D7: r'\vec{}',            # Combining vector arrow
    0x2061: '',                   # Function application invisible glyph
    0x2223: '|',                  # ∣ vertical bar
    0x2234: r' \therefore ',      # ∴
    0x2235: r' \because ',        # ∵
    0x2208: r' \in ',             # ∈
    0x27F6: r' \longrightarrow ', # ⟶
    0x2113: r'\ell',              # ℓ
    0x2227: r' \wedge ',          # ∧
    0x2013: '-',                  # – en-dash
    0x2014: '-',                  # — em-dash
    0x2032: "'",                  # ′ prime
    0x2026: r'\dots',             # …
    0x22EF: r'\cdots',            # ⋯
    0x2202: r'\partial',          # ∂
    0x2207: r'\nabla',            # ∇
    0x222B: r'\int ',             # ∫
    0x2211: r'\sum ',             # ∑
    0x220F: r'\prod ',            # ∏
    0x221A: r'\sqrt',             # √
    0x22A5: r'\perp',             # ⊥
    0x2225: r'\parallel',         # ∥
    0x2220: r'\angle',            # ∠
    0x00C5: r'\text{Å}',          # Å (Angstrom)
    0x212B: r'\text{Å}',          # Å (Angstrom sign)
    0x03BC: r'\mu',               # µ (micro)
    0x03C9: r'\omega',            # ω
    0x03A9: r'\Omega',            # Ω (Ohm)
}

GREEK_VARIANTS = {
    0x1D715: r'\partial',
    0x1D716: r'\epsilon',
    0x1D717: r'\theta',
    0x1D718: r'\kappa',
    0x1D719: r'\phi',
    0x1D71A: r'\rho',
    0x1D71B: r'\pi',
}


def decode_c_hex(c_hex: str) -> str:
    """Decode a hex code from data-c to clean LaTeX or Unicode character."""
    if not c_hex:
        return ''
    try:
        val = int(c_hex, 16)
    except ValueError:
        return ''

    # Special mapped symbols
    if val in SPECIAL_MATH_SYMBOLS:
        return SPECIAL_MATH_SYMBOLS[val]

    # Greek uppercase
    if val in GREEK_UPPER:
        return GREEK_UPPER[val]

    # Mathematical alphanumeric symbols in Unicode (0x1D400 - 0x1D7FF)
    # Math bold capital (0x1D400 - 0x1D419)
    if 0x1D400 <= val <= 0x1D419:
        return chr(ord('A') + val - 0x1D400)
    # Math bold small (0x1D41A - 0x1D433)
    if 0x1D41A <= val <= 0x1D433:
        return chr(ord('a') + val - 0x1D41A)
    # Math italic capital (0x1D434 - 0x1D44D)
    if 0x1D434 <= val <= 0x1D44D:
        return chr(ord('A') + val - 0x1D434)
    # Math italic small (0x1D44E - 0x1D467)
    if 0x1D44E <= val <= 0x1D467:
        # Note: 0x1D455 is absent in some tables, but general formula holds
        return chr(ord('a') + val - 0x1D44E)
    # Math bold italic capital (0x1D468 - 0x1D481)
    if 0x1D468 <= val <= 0x1D481:
        return chr(ord('A') + val - 0x1D468)
    # Math bold italic small (0x1D482 - 0x1D49B)
    if 0x1D482 <= val <= 0x1D49B:
        return chr(ord('a') + val - 0x1D482)
    # Math double-struck / blackboard bold (0x1D538 - 0x1D551)
    if 0x1D538 <= val <= 0x1D551:
        return chr(ord('A') + val - 0x1D538)

    # Mathematical Greek symbols (0x1D6A8 - 0x1D7CB)
    # Mathematical italic capital Greek (0x1D6E2 - 0x1D6FA)
    if 0x1D6E2 <= val <= 0x1D6FA:
        cap_val = 0x0391 + (val - 0x1D6E2)
        if cap_val in GREEK_UPPER:
            return GREEK_UPPER[cap_val]

    # Mathematical italic Greek lowercase (0x1D6FC - 0x1D714)
    if 0x1D6FC <= val <= 0x1D714:
        idx = val - 0x1D6FC
        if idx < len(GREEK_LOWER):
            return GREEK_LOWER[idx]

    # Mathematical italic Greek variants (0x1D715 - 0x1D71B)
    if val in GREEK_VARIANTS:
        return GREEK_VARIANTS[val]

    if val == 0x1D705:
        return r'\kappa'
    if val == 0x1D706:
        return r'\lambda'

    # Standard Greek lowercase (0x03B1 - 0x03C9)
    if 0x03B1 <= val <= 0x03C9:
        idx = val - 0x03B1
        if idx < len(GREEK_LOWER):
            return GREEK_LOWER[idx]

    # Standard ASCII printable
    if 0x20 <= val <= 0x7E:
        return chr(val)

    # Fallback to standard Unicode chr
    try:
        return chr(val)
    except Exception:
        return ''


def parse_mml_ast(node: Tag) -> str:
    """Recursively parse a MathML AST node from MathJax SVG into LaTeX."""
    if not node:
        return ''

    # Base case: <use data-c="...">
    if node.name == 'use':
        c_hex = node.get('data-c')
        return decode_c_hex(c_hex)

    # Base case: <text> tag
    if node.name == 'text':
        return node.get_text()

    mml = node.get('data-mml-node')

    # Fraction: \frac{numerator}{denominator}
    if mml == 'mfrac':
        children = [c for c in node.children if isinstance(c, Tag)]
        if len(children) >= 2:
            num = parse_mml_ast(children[0]).strip()
            den = parse_mml_ast(children[1]).strip()
            return f'\\frac{{{num}}}{{{den}}}'

    # Superscript: base^{sup}
    elif mml == 'msup':
        children = [c for c in node.children if isinstance(c, Tag)]
        if len(children) >= 2:
            base = parse_mml_ast(children[0]).strip()
            sup = parse_mml_ast(children[1]).strip()
            return f'{base}^{{{sup}}}'

    # Subscript: base_{sub}
    elif mml == 'msub':
        children = [c for c in node.children if isinstance(c, Tag)]
        if len(children) >= 2:
            base = parse_mml_ast(children[0]).strip()
            sub = parse_mml_ast(children[1]).strip()
            return f'{base}_{{{sub}}}'

    # Subscript + Superscript: base_{sub}^{sup}
    elif mml == 'msubsup':
        children = [c for c in node.children if isinstance(c, Tag)]
        if len(children) >= 3:
            base = parse_mml_ast(children[0]).strip()
            # MathJax distinguishes sub vs sup by transform translateY
            t1 = children[1].get('transform', '')
            m_trans = re.search(r'translate\([^,]+,\s*([-\d\.]+)\)', t1)
            y1 = float(m_trans.group(1)) if m_trans else 0.0
            if y1 > 0:  # y > 0 is superscript in MathJax flipped SVG
                sup = parse_mml_ast(children[1]).strip()
                sub = parse_mml_ast(children[2]).strip()
            else:
                sub = parse_mml_ast(children[1]).strip()
                sup = parse_mml_ast(children[2]).strip()
            return f'{base}_{{{sub}}}^{{{sup}}}'

    # Square root: \sqrt{radicand}
    elif mml == 'msqrt':
        rad_parts = []
        for c in node.children:
            if not isinstance(c, Tag):
                continue
            # Filter out the radical symbol glyph (0x221A) which is part of the SVG surd drawing
            if c.name == 'use' and c.get('data-c', '').upper() == '221A':
                continue
            if c.get('data-mml-node') == 'mo' and all(u.get('data-c', '').upper() == '221A' for u in c.find_all('use')):
                continue
            rad_parts.append(parse_mml_ast(c))
        inner = ''.join(rad_parts).strip()
        # Clean any leading \sqrt if a surd slipped through
        inner = re.sub(r'^\\sqrt\s*', '', inner)
        return f'\\sqrt{{{inner}}}'

    # N-th root: \sqrt[index]{radicand}
    elif mml == 'mroot':
        children = [c for c in node.children if isinstance(c, Tag)]
        if len(children) >= 2:
            rad = parse_mml_ast(children[0]).strip()
            rad = re.sub(r'^\\sqrt\s*', '', rad)
            idx = parse_mml_ast(children[1]).strip()
            return f'\\sqrt[{idx}]{{{rad}}}'

    # Over element: vectors (\vec), hats (\hat), bars (\bar), or \overset
    elif mml == 'mover':
        children = [c for c in node.children if isinstance(c, Tag)]
        if len(children) >= 2:
            base = parse_mml_ast(children[0]).strip()
            accent = parse_mml_ast(children[1]).strip()
            accent_raw = str(children[1])
            if any(s in accent for s in ['\u20d7', '→', r'\rightarrow', '⃗']) or any(h in accent_raw.upper() for h in ['2192', '20D7']):
                return f'\\vec{{{base}}}'
            elif any(s in accent for s in ['ˆ', '^']) or any(h in accent_raw.upper() for h in ['2C6', '302', '02C6']):
                return f'\\hat{{{base}}}'
            elif any(s in accent for s in ['¯', '-', '‾']) or any(h in accent_raw.upper() for h in ['00AF', '0304', '0305', 'AF']):
                return f'\\bar{{{base}}}'
            elif accent:
                # Remove combining arrow / marks if any remain
                accent_clean = re.sub(r'[\u20d0-\u20ff]', '', accent).strip()
                if accent_clean:
                    return f'\\overset{{{accent_clean}}}{{{base}}}'
            return base

    # Under element: \underset
    elif mml == 'munder':
        children = [c for c in node.children if isinstance(c, Tag)]
        if len(children) >= 2:
            base = parse_mml_ast(children[0]).strip()
            sub = parse_mml_ast(children[1]).strip()
            return f'\\underset{{{sub}}}{{{base}}}'

    # Under-Over element: \sum_{sub}^{sup} or \int_{sub}^{sup}
    elif mml == 'munderover':
        children = [c for c in node.children if isinstance(c, Tag)]
        if len(children) >= 3:
            base = parse_mml_ast(children[0]).strip()
            sub = parse_mml_ast(children[1]).strip()
            sup = parse_mml_ast(children[2]).strip()
            return f'{base}_{{{sub}}}^{{{sup}}}'

    # Table / Matrices / Aligned equations
    elif mml == 'mtable':
        rows = []
        mtr_list = [t for t in node.find_all(lambda t: t.name == 'g' and t.get('data-mml-node') == 'mtr', recursive=False)]
        if not mtr_list:
            mtr_list = [t for t in node.children if isinstance(t, Tag) and t.get('data-mml-node') == 'mtr']
        for r in mtr_list:
            cells = []
            mtd_list = [t for t in r.find_all(lambda t: t.name == 'g' and t.get('data-mml-node') == 'mtd', recursive=False)]
            if not mtd_list:
                mtd_list = [t for t in r.children if isinstance(t, Tag) and t.get('data-mml-node') == 'mtd']
            for d in mtd_list:
                cell_content = ''.join(parse_mml_ast(c) for c in d.children if isinstance(c, Tag)).strip()
                cells.append(cell_content)
            rows.append(' & '.join(cells))
        if rows:
            return '\\begin{aligned} ' + ' \\\\ '.join(rows) + ' \\end{aligned}'

    # Text element within math
    elif mml == 'mtext':
        txt = node.get_text().strip()
        if txt:
            return f'\\text{{{txt}}}'
        return ''

    # Generic traverse for compound containers like math, mstyle, TeXAtom, mrow
    res = []
    for c in node.children:
        if isinstance(c, Tag):
            res.append(parse_mml_ast(c))
    return ''.join(res)


def decode_mathjax_container(container: Tag) -> str:
    """Convert an <mjx-container> element to clean LaTeX string."""
    if not container:
        return ''
    math_g = container.find('g', attrs={'data-mml-node': 'math'})
    if not math_g:
        return ''
    tex = parse_mml_ast(math_g).strip()
    # Normalize LaTeX spacing and artifact cleanups
    tex = re.sub(r'\s+', ' ', tex)
    # Fix doubled sqrt artifacts: \sqrt{\sqrt{...}} -> \sqrt{...} or \sqrt{\sqrt... -> \sqrt{...}
    tex = re.sub(r'\\sqrt\{\\sqrt\s*', r'\\sqrt{', tex)
    # Fix doubled circ like ^{^{\circ}} -> ^{\circ}
    tex = re.sub(r'\^\{\^\{\\circ\}\}', r'^{\\circ}', tex)
    tex = re.sub(r'\_\{\}', '', tex)
    tex = re.sub(r'\^\{\}', '', tex)
    # Fix missing spaces after LaTeX command names when followed by Latin letters, digits, or backslash:
    # e.g. \omegat -> \omega t, \lambda\hat -> \lambda \hat, \DeltaG -> \Delta G, \piL -> \pi L, \muF -> \mu F, \sqrtR -> \sqrt R
    tex = re.sub(
        r'(\\(?:alpha|beta|gamma|delta|epsilon|zeta|eta|theta|iota|kappa|lambda|mu|nu|xi|pi|rho|sigma|tau|upsilon|phi|chi|psi|omega|Gamma|Delta|Theta|Lambda|Xi|Pi|Sigma|Upsilon|Phi|Psi|Omega|cdot|times|pm|mp|le|ge|ne|approx|equiv|partial|nabla|ell|sqrt))([a-zA-Z0-9\\])',
        r'\1 \2',
        tex
    )
    # Remove invisible math characters
    tex = tex.replace('\u2061', '').replace('\u200b', '')
    return tex


def clean_html_with_math(html_or_element) -> Tuple[str, str]:
    """
    Process HTML content containing MathJax SVG containers:
    1. Produces a clean text version with $LaTeX$ inline math.
    2. Produces a sanitized HTML string with math marked in KaTeX/MathJax friendly spans.
    
    Returns:
        Tuple of (clean_text, clean_html)
    """
    if not html_or_element:
        return ('', '')

    html_str = str(html_or_element)
    soup = BeautifulSoup(html_str, 'html.parser')

    # Convert each mjx-container
    containers = soup.find_all('mjx-container')
    for m in containers:
        tex = decode_mathjax_container(m)
        if tex:
            # Check if display math or inline
            is_display = 'overflow' in m.get('class', []) and ('begin{aligned}' in tex or len(tex) > 60)
            delim = '$$' if is_display else '$'
            # Create replacement text node
            m.replace_with(f' {delim}{tex}{delim} ')
        else:
            m.decompose()

    # Clean text representation
    raw_text = soup.get_text(separator=' ', strip=True)
    clean_text = re.sub(r'[ \t]+', ' ', raw_text)
    clean_text = re.sub(r'\n{3,}', '\n\n', clean_text)
    clean_text = clean_text.strip()

    # For HTML output: wrap math expressions in KaTeX-compatible spans
    # and strip redundant empty tags
    for p in soup.find_all(['p', 'div']):
        if not p.get_text(strip=True) and not p.find('img'):
            p.decompose()

    clean_html = str(soup).strip()
    return (clean_text, clean_html)
