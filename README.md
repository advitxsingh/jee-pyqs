# JEE Main PYQs Concept Studio & Revision Engine

An intelligent, autonomous system for crawling, parsing, analyzing, and synthesizing Previous Year Questions (PYQs) from **ExamSIDE** for **JEE Main**.

The system extracts core concepts, formulas, and recurring pitfalls from every question, links concepts directly back to their originating PYQs, generates structured chapter concept sheets, and produces print-ready **Word (.docx)** and **PDF** revision booklets.

---

## 🌟 Key Features

1. **Autonomous SSR HTML Crawler with MathJax SVG Decoding**:
   - Accurately converts ExamSIDE Server-Side Rendered (SSR) MathJax SVGs (`data-c` hex Unicode characters and MathML AST nodes: `msup`, `msub`, `msubsup`, `mfrac`, `msqrt`, `mover`, `mtable`) into clean LaTeX expressions (`$E^\circ$`, `$\vec{a}\times\vec{b}$`, `$\frac{1}{\sqrt{LC}}$`).
   - High-throughput async batch striding (fetching 4 questions per request concurrently).
   - Extracts complete problem statements, options (A-D), marking schemes, answer keys, step-by-step explanations, and diagram URLs.

2. **Domain-Specific Concept Extractor & Empiric Frequency Mapper**:
   - Maps each question to syllabus topics and formula archetypes.
   - Computes empirical question frequency and assigns yield priority tiers (`Very High`, `High`, `Moderate`).
   - Identifies recurring JEE traps (sign conventions, unit conversions, limiting boundary conditions) and speed tricks.

3. **Concept <-> PYQ Bidirectional Linking**:
   - Every concept is linked to the exact JEE Main PYQs that test it (indexed with Year, Shift, Question Text snippet, and Answer Key).
   - In the dashboard, click any concept to filter and view all matching PYQs.

4. **Print-Ready Word (.docx) & PDF Exporters**:
   - **Word Document (.docx)**: Professional typography (Calibri/Cambria Math), priority matrix tables, shaded caution callout boxes for traps, and benchmark illustrative questions with complete solutions.
   - **PDF Booklet (.pdf)**: Built with ReportLab, featuring custom `NumberedCanvas` ("Page X of Y"), title banners, styled formula tables, and high-contrast STEM styling.

5. **Modern Local Web Dashboard (FastAPI + KaTeX)**:
   - Real-time client-side math rendering using KaTeX.
   - Subject switcher (Chemistry, Physics, Mathematics).
   - Interactive Concept Matrix, Markdown Chapter Notes, Filterable PYQ Bank (filter by Year, Type, Difficulty, Concept, or Keyword), and Syllabus Crawler Manager.

---

## 🚀 Processed Pilot Chapters (Ready to Use)

| Chapter | Subject | PYQs Indexed | Core Concepts | Word Export (.docx) | Printable PDF (.pdf) |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **Electrochemistry** | Chemistry | **226** | 7 | [Word Notes](file:///X:/code/jee-pyqs/data/exports/electrochemistry_revision_notes.docx) | [PDF Booklet](file:///X:/code/jee-pyqs/data/exports/electrochemistry_revision_notes.pdf) |
| **Electromagnetic Induction** | Physics | **153** | 6 | [Word Notes](file:///X:/code/jee-pyqs/data/exports/electromagnetic-induction_revision_notes.docx) | [PDF Booklet](file:///X:/code/jee-pyqs/data/exports/electromagnetic-induction_revision_notes.pdf) |
| **Alternating Current** | Physics | **191** | 7 | [Word Notes](file:///X:/code/jee-pyqs/data/exports/alternating-current_revision_notes.docx) | [PDF Booklet](file:///X:/code/jee-pyqs/data/exports/alternating-current_revision_notes.pdf) |
| **Vector Algebra** | Mathematics | **282** | 7 | [Word Notes](file:///X:/code/jee-pyqs/data/exports/vector-algebra_revision_notes.docx) | [PDF Booklet](file:///X:/code/jee-pyqs/data/exports/vector-algebra_revision_notes.pdf) |
| **Total** | | **852** | **27** | | |

---

## 💻 How to Run

### 1. Launch the Local Web Dashboard
```bash
python run.py
```
Open your browser at **[http://localhost:8000](http://localhost:8000)**.

### 2. Crawl & Re-Analyze Chapters via CLI
To re-run the pilot crawler pipeline:
```bash
python crawl_pilot.py
```

### 3. Run Automated Tests
```bash
python -m unittest discover tests
```

---

## 📁 Repository Structure

```
jee-pyqs/
├── app/
│   ├── crawler/
│   │   ├── math_parser.py       # Robust MathJax SVG -> LaTeX & clean text engine
│   │   ├── page_parser.py       # HTML parser for ExamSIDE chapter & question pages
│   │   └── crawler.py           # Async crawler with batch striding & queue worker
│   ├── db/
│   │   ├── models.py            # Pydantic data models
│   │   └── database.py          # SQLite schema, WAL mode, queries & indexing
│   ├── analyzer/
│   │   ├── concept_extractor.py # Topic taxonomies, formula & trap extraction
│   │   ├── chapter_synthesizer.py # Synthesizes chapter concept pages & formulas
│   │   └── analyzer_service.py  # Orchestrates extraction, linking & exports
│   ├── exporter/
│   │   ├── docx_exporter.py     # python-docx revision booklet generator
│   │   └── pdf_exporter.py      # ReportLab printable PDF generator
│   └── web/
│       ├── app.py               # FastAPI server & REST API
│       └── templates/
│           └── index.html       # Single-page dashboard with KaTeX math rendering
├── data/
│   ├── jee_pyqs.db              # SQLite database (845+ questions, 27+ concepts)
│   └── exports/                 # Generated .docx and .pdf revision booklets
├── tests/
│   ├── test_math_parser.py      # MathJax AST & Unicode decoding tests
│   ├── test_page_parser.py      # Question & chapter HTML parser tests
│   ├── test_database.py         # SQLite models & linking tests
│   ├── test_analyzer.py         # Concept extraction & synthesis tests
│   ├── test_exporters.py        # DOCX & PDF generation tests
│   └── test_api.py              # FastAPI REST endpoint integration tests
├── run.py                       # Main application launcher
├── crawl_pilot.py               # Pilot chapters CLI crawler
└── README.md                    # System documentation
```
