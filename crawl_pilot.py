"""
CLI Pilot Crawler & Analyzer for JEE Main Target Chapters:
1. Electrochemistry (Chemistry)
2. Electromagnetic Induction (Physics)
3. Alternating Current (Physics)
4. Vector Algebra (Mathematics)

Crawls all questions, decodes MathJax formulas, extracts concepts, links PYQs,
and generates print-ready Word (.docx) and PDF revision booklets.
"""

import sys
import os
import asyncio
import time
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn

# Ensure project root is in PYTHONPATH
sys.path.insert(0, os.path.abspath('.'))

try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

from app.db.database import init_db, get_chapter, get_question_count_by_chapter, get_concepts_by_chapter
from app.crawler.crawler import CrawlerEngine, PILOT_CHAPTERS
from app.analyzer.analyzer_service import analyze_chapter
from app.exporter.docx_exporter import generate_chapter_docx
from app.exporter.pdf_exporter import generate_chapter_pdf

console = Console(force_terminal=True, highlight=False)


async def run_pilot_pipeline():
    console.print("\n[bold cyan]===========================================================[/bold cyan]")
    console.print("[bold cyan]       JEE MAIN PYQS ANALYZER & CONCEPT SYNTHESIZER       [/bold cyan]")
    console.print("[bold cyan]===========================================================[/bold cyan]\n")

    # 1. Initialize Database
    init_db("data/jee_pyqs.db")
    console.print("[green][OK][/green] Database initialized at [bold]data/jee_pyqs.db[/bold]")

    crawler = CrawlerEngine(db_path="data/jee_pyqs.db", max_concurrency=6)

    # 2. Discover all chapters for background indexing
    console.print("[yellow][*] Discovering JEE Main syllabus chapters on ExamSIDE...[/yellow]")
    all_ch = await crawler.discover_all_chapters()
    console.print(f"[green][OK][/green] Discovered {len(all_ch)} total chapters across Physics, Chemistry, and Mathematics.\n")

    # 3. Process the 4 Pilot Chapters
    results = []

    for pilot in PILOT_CHAPTERS:
        slug = pilot["slug"]
        title = pilot["title"]
        subject = pilot["subject"]

        console.print(f"\n[bold blue]-----------------------------------------------------------[/bold blue]")
        console.print(f"[bold white][>] Processing Pilot Chapter:[/bold white] [bold yellow]{title}[/bold yellow] ({subject.title()})")
        console.print(f"[bold blue]-----------------------------------------------------------[/bold blue]")

        t0 = time.time()

        # Step A: Crawl Questions
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TimeElapsedColumn(),
            console=console
        ) as progress:
            task = progress.add_task(f"Downloading & decoding {title} PYQs...", total=100)

            def progress_cb(pct, msg):
                progress.update(task, completed=pct, description=f"{title}: {msg}")

            q_count = await crawler.crawl_chapter(slug, progress_callback=progress_cb)

        console.print(f"[green][OK][/green] Crawled and parsed [bold]{q_count}[/bold] questions with MathJax SVG decoding.")

        # Step B: Analyze Concepts & Link PYQs
        console.print(f"[yellow][*] Analyzing concepts, formulas, difficulty, and linking PYQs...[/yellow]")
        an_res = analyze_chapter(slug, db_path="data/jee_pyqs.db")
        concepts = get_concepts_by_chapter(slug, db_path="data/jee_pyqs.db")
        console.print(f"[green][OK][/green] Extracted [bold]{len(concepts)}[/bold] core concepts with empirical frequency mapping.")

        # Step C: Export Notes (.docx and .pdf)
        console.print(f"[yellow][*] Generating print-ready Word (.docx) and PDF revision booklets...[/yellow]")
        docx_path = generate_chapter_docx(slug, db_path="data/jee_pyqs.db")
        pdf_path = generate_chapter_pdf(slug, db_path="data/jee_pyqs.db")
        console.print(f"[green][OK][/green] Word Notes: [bold]{docx_path}[/bold]")
        console.print(f"[green][OK][/green] PDF Notes:  [bold]{pdf_path}[/bold]")

        elapsed = time.time() - t0
        results.append({
            "chapter": title,
            "subject": subject.title(),
            "questions": q_count,
            "concepts": len(concepts),
            "docx": docx_path,
            "pdf": pdf_path,
            "time": f"{elapsed:.1f}s"
        })

    await crawler.close()

    # Summary Table
    console.print("\n[bold green]===========================================================[/bold green]")
    console.print("[bold green]             PILOT CHAPTERS PROCESSING SUMMARY             [/bold green]")
    console.print("[bold green]===========================================================[/bold green]\n")

    table = Table(title="Processed JEE Main Pilot Chapters")
    table.add_column("Chapter", style="cyan", no_wrap=True)
    table.add_column("Subject", style="magenta")
    table.add_column("PYQs", justify="right", style="green")
    table.add_column("Concepts", justify="right", style="yellow")
    table.add_column("Word Export (.docx)", style="blue")
    table.add_column("PDF Export (.pdf)", style="red")
    table.add_column("Elapsed", justify="right", style="white")

    total_pyqs = 0
    total_concepts = 0

    for r in results:
        table.add_row(
            r["chapter"], r["subject"], str(r["questions"]),
            str(r["concepts"]), r["docx"], r["pdf"], r["time"]
        )
        total_pyqs += r["questions"]
        total_concepts += r["concepts"]

    console.print(table)
    console.print(f"\n[bold]Total Questions Indexed:[/bold] [bold green]{total_pyqs}[/bold green]")
    console.print(f"[bold]Total Concepts Synthesized:[/bold] [bold yellow]{total_concepts}[/bold yellow]")
    console.print(f"[bold green]Ready to run web dashboard![/bold green]\n")


if __name__ == "__main__":
    asyncio.run(run_pilot_pipeline())
