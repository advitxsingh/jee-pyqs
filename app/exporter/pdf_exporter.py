"""
PDF Exporter for JEE PYQ Concept Sheets & Revision Notes using ReportLab.
Generates a print-ready, high-contrast revision booklet with page numbers.
"""

import os
import re
from typing import Optional, List
from datetime import datetime

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

from app.db.database import (
    get_chapter, get_chapter_synthesis, get_concepts_by_chapter,
    get_questions_by_chapter, get_question_by_id, DB_PATH
)


class NumberedCanvas(canvas.Canvas):
    """Custom canvas that tracks total pages to render 'Page X of Y'."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count: int):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#718096"))

        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(54, 750, "JEE Main PYQs Concept Revision Sheet")
            self.setStrokeColor(colors.HexColor("#CBD5E0"))
            self.setLineWidth(0.5)
            self.line(54, 744, 558, 744)

        # Footer
        footer_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(558, 36, footer_text)
        self.drawString(54, 36, f"Generated for JEE Mains | {datetime.now().strftime('%b %Y')}")
        self.setStrokeColor(colors.HexColor("#CBD5E0"))
        self.setLineWidth(0.5)
        self.line(54, 48, 558, 48)

        self.restoreState()


def format_math_for_print(text: str) -> str:
    """
    Format LaTeX expressions into clean, legible typographic notation for print documents.
    """
    if not text:
        return ""

    def _clean_formula(tex: str) -> str:
        s = tex.strip()
        s = re.sub(r'\\begin\{(?:aligned|matrix|array|cases)\}', '', s)
        s = re.sub(r'\\end\{(?:aligned|matrix|array|cases)\}', '', s)
        s = s.replace('&', ' ').replace(r'\\', '\n')
        s = re.sub(r'\\text\{([^}]*)\}', r'\1', s)
        s = re.sub(r'\\mathrm\{([^}]*)\}', r'\1', s)
        s = re.sub(r'\\mathbf\{([^}]*)\}', r'\1', s)

        for _ in range(3):
            s = re.sub(r'\\frac\{([^{}]+)\}\{([^{}]+)\}', r'(\1 / \2)', s)

        s = re.sub(r'\\sqrt\[([^]]+)\]\{([^}]+)\}', r'\1√(\2)', s)
        s = re.sub(r'\\sqrt\{([^}]+)\}', r'√(\1)', s)
        s = re.sub(r'\\sqrt\s*([a-zA-Z0-9])', r'√\1', s)

        s = re.sub(r'\\vec\{([^}]+)\}', r'vec(\1)', s)
        s = re.sub(r'\\hat\{([^}]+)\}', r'\1̂', s)
        s = re.sub(r'\\bar\{([^}]+)\}', r'bar(\1)', s)
        s = re.sub(r'\\overset\{[^}]*\}\{([^}]+)\}', r'vec(\1)', s)

        s = s.replace(r'^{\circ}', '°').replace(r'^\circ', '°')
        s = re.sub(r'\^\{([0-9\+\-]+)\}', r'^\1', s)
        s = re.sub(r'\^([0-9])', r'^\1', s)
        s = re.sub(r'\_\{([^}]+)\}', r'_(\1)', s)

        GREEK_MAP = {
            r'\alpha': 'α', r'\beta': 'β', r'\gamma': 'γ', r'\delta': 'δ',
            r'\epsilon': 'ε', r'\zeta': 'ζ', r'\eta': 'η', r'\theta': 'θ',
            r'\iota': 'ι', r'\kappa': 'κ', r'\lambda': 'λ', r'\mu': 'μ',
            r'\nu': 'ν', r'\xi': 'ξ', r'\pi': 'π', r'\rho': 'ρ',
            r'\sigma': 'σ', r'\tau': 'τ', r'\upsilon': 'υ', r'\phi': 'ϕ',
            r'\chi': 'χ', r'\psi': 'ψ', r'\omega': 'ω',
            r'\Gamma': 'Γ', r'\Delta': 'Δ', r'\Theta': 'Θ', r'\Lambda': 'Λ',
            r'\Xi': 'Ξ', r'\Pi': 'Π', r'\Sigma': 'Σ', r'\Upsilon': 'Υ',
            r'\Phi': 'Φ', r'\Psi': 'Ψ', r'\Omega': 'Ω',
        }
        for k, v in GREEK_MAP.items():
            s = re.sub(re.escape(k) + r'(?![a-zA-Z])', v, s)

        SYM_MAP = {
            r'\times': '×', r'\cdot': '·', r'\div': '÷', r'\pm': '±', r'\mp': '∓',
            r'\longrightarrow': '→', r'\rightarrow': '→', r'\leftarrow': '←',
            r'\Rightarrow': '⇒', r'\rightleftharpoons': '⇌',
            r'\le': '≤', r'\ge': '≥', r'\ne': '≠', r'\approx': '≈',
            r'\equiv': '≡', r'\in': '∈', r'\perp': '⊥', r'\parallel': '∥',
            r'\infty': '∞', r'\int': '∫', r'\sum': '∑', r'\partial': '∂',
            r'\nabla': '∇', r'\ell': 'ℓ', r'\therefore': '∴', r'\because': '∵',
            r'\dots': '...', r'\cdots': '...',
            r'\log': 'log', r'\ln': 'ln', r'\sin': 'sin', r'\cos': 'cos', r'\tan': 'tan',
            r'\quad': ' ', r'\qquad': '  ', r'\,': ' ', r'\;': ' ', r'\!': ''
        }
        for k, v in SYM_MAP.items():
            s = re.sub(re.escape(k) + r'(?![a-zA-Z])', v, s)

        s = s.replace('{', '').replace('}', '')
        return re.sub(r'\s+', ' ', s).strip()

    res = re.sub(r'\$\$([^\$]+)\$\$', lambda m: _clean_formula(m.group(1)), text)
    res = re.sub(r'\$([^\$]+)\$', lambda m: _clean_formula(m.group(1)), res)
    return res.replace('\u2061', '').replace('\u200b', '')


def clean_math_for_pdf(text: str) -> str:
    """Format LaTeX math strings into clean readable notation and XML escape for ReportLab Paragraphs."""
    if not text:
        return ""
    # Format math to clean readable Unicode notation
    clean_text = format_math_for_print(text)
    # XML escape
    return clean_text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def generate_chapter_pdf(chapter_slug: str, output_path: Optional[str] = None, db_path: str = DB_PATH) -> str:
    """
    Generate a high-quality PDF revision booklet for the specified chapter.
    Returns the generated PDF file path.
    """
    chapter = get_chapter(chapter_slug, db_path=db_path)
    if not chapter:
        raise ValueError(f"Chapter '{chapter_slug}' not found.")

    synthesis = get_chapter_synthesis(chapter_slug, db_path=db_path)
    concepts = get_concepts_by_chapter(chapter_slug, db_path=db_path)
    questions = get_questions_by_chapter(chapter_slug, limit=1000, db_path=db_path)

    if not output_path:
        os.makedirs("data/exports", exist_ok=True)
        output_path = f"data/exports/{chapter_slug}_revision_notes.pdf"

    temp_target = f"data/exports/.tmp_{chapter_slug}_{os.getpid()}_revision_notes.pdf"

    doc = SimpleDocTemplate(
        temp_target,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    # Custom typography styles
    style_title = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#1A365D"),
        spaceAfter=4
    )

    style_subtitle = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#4A5568"),
        spaceAfter=14
    )

    style_h1 = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=colors.HexColor("#1A365D"),
        spaceBefore=12,
        spaceAfter=8,
        keepWithNext=True
    )

    style_h2 = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor("#2B6CB0"),
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )

    style_body = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#2D3748")
    )

    style_callout_trap = ParagraphStyle(
        'CalloutTrap',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#742A2A")
    )

    style_callout_trick = ParagraphStyle(
        'CalloutTrick',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#22543D")
    )

    story = []

    # Document Header
    story.append(Paragraph(f"JEE MAIN REVISION MASTER: {chapter.title.upper()}", style_title))
    story.append(Paragraph(
        f"<b>Subject:</b> {chapter.subject.title()} &nbsp;|&nbsp; <b>Target Scope:</b> JEE Main Previous Years &nbsp;|&nbsp; <b>Empirical Base:</b> {len(questions)} Analyzed PYQs",
        style_subtitle
    ))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1A365D"), spaceBefore=0, spaceAfter=12))

    # --- Section 1: Concept Priority Matrix Table ---
    story.append(Paragraph("1. High-Yield Concept Priority Matrix", style_h1))
    
    table_data = [
        [
            Paragraph("<b>Priority Tier</b>", style_body),
            Paragraph("<b>Concept Name</b>", style_body),
            Paragraph("<b>Frequency</b>", style_body),
            Paragraph("<b>Category</b>", style_body)
        ]
    ]

    # Order concepts: High/Very High curated concepts first, fallback at end
    def _concept_sort_key(c):
        is_fallback = c.name.endswith("Core Application")
        tier_weight = {"Very High": 4, "High": 3, "Moderate": 2, "Standard": 1}.get(c.frequency_tier, 0)
        return (1 if is_fallback else 0, -tier_weight, -c.exam_frequency)

    sorted_concepts = sorted(concepts, key=_concept_sort_key)

    for c in sorted_concepts:
        tier_color = "#C53030" if c.frequency_tier == "Very High" else ("#2B6CB0" if c.frequency_tier == "High" else "#718096")
        table_data.append([
            Paragraph(f"<font color='{tier_color}'><b>{c.frequency_tier}</b></font>", style_body),
            Paragraph(f"<b>{c.name}</b>", style_body),
            Paragraph(f"{c.exam_frequency} PYQs", style_body),
            Paragraph(c.category, style_body)
        ])

    t_matrix = Table(table_data, colWidths=[1.2*inch, 2.8*inch, 1.1*inch, 1.9*inch])
    t_matrix.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1A365D")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
        ('TOPPADDING', (0, 0), (-1, 0), 6),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor("#F7FAFC"), colors.white]),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#E2E8F0")),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 1), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 4),
    ]))
    # Format header text color in table cells
    for col_idx in range(4):
        t_matrix._cellvalues[0][col_idx] = Paragraph(f"<font color='white'><b>{['Priority Tier', 'Concept Name', 'Frequency', 'Category'][col_idx]}</b></font>", style_body)

    story.append(t_matrix)
    story.append(Spacer(1, 14))

    # --- Section 2: Master Formula Reference Card ---
    story.append(Paragraph("2. Master Formula Reference Card", style_h1))
    
    formula_data = [
        [
            Paragraph("<font color='white'><b>Concept / Topic</b></font>", style_body),
            Paragraph("<font color='white'><b>Mathematical Formulation &amp; Governing Equations</b></font>", style_body)
        ]
    ]

    for c in sorted_concepts:
        if c.standard_formulas and not c.name.endswith("Core Application"):
            clean_f = clean_math_for_pdf(c.standard_formulas)
            formula_data.append([
                Paragraph(f"<b>{c.name}</b>", style_body),
                Paragraph(clean_f, style_body)
            ])

    t_formula = Table(formula_data, colWidths=[2.2*inch, 4.8*inch])
    t_formula.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#2B6CB0")),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
        ('TOPPADDING', (0, 0), (-1, 0), 6),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor("#F7FAFC"), colors.white]),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E0")),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 1), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 5),
    ]))
    story.append(t_formula)
    story.append(Spacer(1, 14))

    # --- Section 3: Detailed Concepts & Linked PYQs ---
    story.append(Paragraph("3. Deep-Dive Concepts & Linked PYQ Evidence", style_h1))

    for idx, c in enumerate(sorted_concepts, 1):
        concept_elements = []
        concept_elements.append(Paragraph(f"3.{idx} {c.name} ({c.frequency_tier} Yield — {c.exam_frequency} PYQs)", style_h2))
        concept_elements.append(Paragraph(f"<b>Core Principle:</b> {clean_math_for_pdf(c.summary)}", style_body))
        concept_elements.append(Spacer(1, 4))

        # Traps callout box
        if c.common_traps:
            clean_trap = clean_math_for_pdf(c.common_traps)
            trap_table = Table(
                [[Paragraph(f"<b>⚠️ Caution / JEE Pitfall:</b> {clean_trap}", style_callout_trap)]],
                colWidths=[7.0*inch]
            )
            trap_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#FFF5F5")),
                ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#FEB2B2")),
                ('TOPPADDING', (0, 0), (-1, -1), 4),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
                ('LEFTPADDING', (0, 0), (-1, -1), 8),
                ('RIGHTPADDING', (0, 0), (-1, -1), 8),
            ]))
            concept_elements.append(trap_table)
            concept_elements.append(Spacer(1, 4))

        # Tricks callout box
        if c.tips_and_tricks:
            clean_trick = clean_math_for_pdf(c.tips_and_tricks)
            trick_table = Table(
                [[Paragraph(f"<b>💡 Speed Trick:</b> {clean_trick}", style_callout_trick)]],
                colWidths=[7.0*inch]
            )
            trick_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#F0FFF4")),
                ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#9AE6B4")),
                ('TOPPADDING', (0, 0), (-1, -1), 4),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
                ('LEFTPADDING', (0, 0), (-1, -1), 8),
                ('RIGHTPADDING', (0, 0), (-1, -1), 8),
            ]))
            concept_elements.append(trick_table)
            concept_elements.append(Spacer(1, 4))

        # Linked PYQs list
        matched_qs = [q for q in questions if c.name in q.key_concepts or q.topic_tag == c.name][:3]
        if not matched_qs:
            matched_qs = questions[:2]

        concept_elements.append(Paragraph("<b>Representative Source PYQs:</b>", style_body))
        for mq in matched_qs:
            clean_q = clean_math_for_pdf(mq.question_text[:140])
            ans_str = f"<b>[Ans: {mq.correct_answer or 'N/A'}]</b>"
            line = f"• <b>[{mq.year} {mq.shift or 'Shift'}] Q#{mq.question_index} ({mq.question_type})</b>: <i>\"{clean_q}...\"</i> {ans_str}"
            concept_elements.append(Paragraph(line, style_body))
            concept_elements.append(Spacer(1, 2))

        concept_elements.append(Spacer(1, 8))
        story.append(KeepTogether(concept_elements))

    # --- Section 4: Benchmark PYQs ---
    story.append(Paragraph("4. Benchmark Illustrative PYQs with Master Solutions", style_h1))

    benchmark_ids = synthesis.benchmark_pyq_ids if synthesis else []
    benchmarks = []
    for bid in benchmark_ids:
        b = get_question_by_id(str(bid), db_path=db_path)
        if b:
            benchmarks.append(b)
    if not benchmarks:
        benchmarks = [q for q in questions if len(q.explanation_text or "") > 150][:4]

    for b_idx, bq in enumerate(benchmarks, 1):
        b_elements = []
        b_elements.append(Paragraph(f"<b>Benchmark Problem {b_idx}: {bq.paper_name} (Q#{bq.question_index})</b>", style_h2))
        b_elements.append(Paragraph(clean_math_for_pdf(bq.question_text), style_body))
        b_elements.append(Spacer(1, 4))

        if bq.options:
            for opt in bq.options:
                opt_clean = clean_math_for_pdf(f"({opt.label}) {opt.text}")
                is_correct = opt.label == bq.correct_answer
                tag = " <b>[Correct]</b>" if is_correct else ""
                b_elements.append(Paragraph(f"&nbsp;&nbsp;• {opt_clean}{tag}", style_body))

        b_elements.append(Spacer(1, 4))

        # Solution box
        expl_clean = clean_math_for_pdf(bq.explanation_text[:600])
        sol_content = [
            Paragraph(f"<b>Correct Answer: {bq.correct_answer}</b>", style_body),
            Spacer(1, 2),
            Paragraph(f"<b>Solution Analysis:</b> {expl_clean}", style_body)
        ]
        sol_table = Table([[sol_content]], colWidths=[7.0*inch])
        sol_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#F7FAFC")),
            ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E0")),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('LEFTPADDING', (0, 0), (-1, -1), 8),
            ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ]))
        b_elements.append(sol_table)
        b_elements.append(Spacer(1, 10))

        story.append(KeepTogether(b_elements))

    doc.build(story, canvasmaker=NumberedCanvas)

    try:
        if os.path.exists(output_path):
            try:
                os.replace(temp_target, output_path)
            except OSError:
                alt_path = f"data/exports/{chapter_slug}_notes.pdf"
                os.replace(temp_target, alt_path)
                output_path = alt_path
        else:
            os.replace(temp_target, output_path)
    except Exception:
        output_path = temp_target

    return output_path
