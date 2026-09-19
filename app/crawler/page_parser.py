"""
HTML page parsers for ExamSIDE chapter pages and question batch pages.
"""

import re
from typing import List, Dict, Any, Optional, Tuple
from bs4 import BeautifulSoup, Tag

from app.crawler.math_parser import clean_html_with_math
from app.db.models import QuestionModel, OptionItem


def parse_chapter_page(html_str: str, page_url: str) -> Dict[str, Any]:
    """
    Parse a chapter overview page to discover all question links grouped by MCQ and Numerical.
    """
    soup = BeautifulSoup(html_str, 'html.parser')
    
    # Extract chapter title
    h1 = soup.find('h1')
    title = h1.get_text(strip=True) if h1 else ""
    if not title:
        title_tag = soup.find('title')
        title = title_tag.get_text().split('|')[0].strip() if title_tag else "JEE Main Chapter"

    # Determine subject and chapter slug from URL
    # e.g. /past-years/jee/jee-main/chemistry/electrochemistry
    url_parts = page_url.strip('/').split('/')
    subject = "physics"
    slug = "chapter"
    for i, p in enumerate(url_parts):
        if p in ["physics", "chemistry", "mathematics"]:
            subject = p
            if i + 1 < len(url_parts):
                slug = url_parts[i + 1]
            break

    mcq_links: List[str] = []
    num_links: List[str] = []

    # Find section groups (ExamSIDE uses section.cp-group)
    for group in soup.find_all(lambda t: t.name == 'section' and 'cp-group' in t.get('class', [])):
        group_text = group.get_text()
        links = [a['href'] for a in group.find_all('a', href=True) if '/question/' in a['href']]
        # deduplicate while preserving order
        unique_links = list(dict.fromkeys(links))
        if 'MCQ' in group_text:
            mcq_links.extend(unique_links)
        elif 'Numerical' in group_text:
            num_links.extend(unique_links)
        else:
            mcq_links.extend(unique_links)

    # Fallback if groups were not structured
    if not mcq_links and not num_links:
        all_q_links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith('/past-years/jee/question/')]
        mcq_links = list(dict.fromkeys(all_q_links))

    all_links = list(dict.fromkeys(mcq_links + num_links))

    return {
        "title": title,
        "subject": subject,
        "slug": slug,
        "url": page_url,
        "mcq_links": mcq_links,
        "num_links": num_links,
        "all_links": all_links,
        "total_questions": len(all_links)
    }


def extract_correct_answer(ans_box: Tag, q_type: str) -> Optional[str]:
    """
    Extract the correct answer key from when-answered element.
    Works for both MCQs (A, B, C, D) and Numerical answers (numbers).
    """
    if not ans_box:
        return None

    raw_text = ans_box.get_text(separator=' ', strip=True)

    if q_type == "Numerical":
        # Numerical format: "Correct answer is 15" or "Answer Correct answer is 120"
        m_num = re.search(r'(?:Correct\s+answer\s+is|Answer[:\s]+)\s*([-+]?\d+(?:\.\d+)?)', raw_text, re.IGNORECASE)
        if m_num:
            return m_num.group(1).strip()
        m_fallback = re.search(r'is\s*([-+]?\d+(?:\.\d+)?)', raw_text, re.IGNORECASE)
        if m_fallback:
            return m_fallback.group(1).strip()
        return None

    # MCQ formats
    # 1. "Option (B) is correct" or "Option (B) is the correct answer"
    m_opt = re.search(r'Option\s*[\(\[]?([A-D])[\)\]]?\s*is\s*(?:the\s*)?correct', raw_text, re.IGNORECASE)
    if m_opt:
        return m_opt.group(1).upper()

    # 2. "Correct option is (B)" or "Correct answer is Option B"
    m_corr = re.search(r'Correct\s*(?:option|answer)\s*(?:is)?\s*(?:option\s*)?[:\s]*[\(\[]?([A-D])[\)\]]?', raw_text, re.IGNORECASE)
    if m_corr:
        return m_corr.group(1).upper()

    # 3. "Ans. (B)" or "Answer: B"
    m_ans = re.search(r'\bAns(?:wer)?\s*[:\.]?\s*\(?([A-D])\)?\b', raw_text, re.IGNORECASE)
    if m_ans:
        return m_ans.group(1).upper()

    # 4. Check for tag-correct in options container
    for tag in ans_box.find_all(class_='tag-correct'):
        parent_opt = tag.find_parent(class_='option')
        if parent_opt:
            badge = parent_opt.find(class_='option-badge')
            if badge:
                return badge.get_text(strip=True).upper()

    return None


def parse_question_batch_page(
    html_str: str,
    page_url: str,
    chapter_slug: str,
    subject: str
) -> Tuple[List[QuestionModel], Optional[str]]:
    """
    Parse a question batch page (typically containing 4 questions).
    Returns list of QuestionModel and the next page URL (if any).
    """
    soup = BeautifulSoup(html_str, 'html.parser')
    qcs = soup.find_all(class_='question-component')
    questions: List[QuestionModel] = []

    for qc in qcs:
        qid = qc.get('data-qid')
        if not qid:
            # Fallback to id or hash
            continue

        raw_type = qc.get('data-type', 'mcq').lower()
        chip_type_el = qc.find(class_='q-chip-type')
        chip_type_str = chip_type_el.get_text(strip=True) if chip_type_el else ""
        if "numerical" in chip_type_str.lower() or raw_type in ["integer", "numerical"]:
            q_type = "Numerical"
        else:
            q_type = "MCQ"

        # Question Index
        idx_el = qc.find(class_='q-index')
        try:
            q_index = int(idx_el.get_text(strip=True)) if idx_el else 0
        except ValueError:
            q_index = 0

        # Paper details
        paper_el = qc.find(class_='q-paper')
        paper_name = paper_el.get_text(strip=True) if paper_el else "JEE Main"

        # Parse year
        m_year = re.search(r'\b((?:19|20)\d{2})\b', paper_name)
        year = int(m_year.group(1)) if m_year else 2026

        # Parse shift and date
        m_shift = re.search(r'(Morning Shift|Evening Shift|Shift \d+)', paper_name, re.IGNORECASE)
        shift = m_shift.group(1).title() if m_shift else None

        m_date = re.search(r'(\d+(?:st|nd|rd|th)?\s+[A-Za-z]+)', paper_name)
        exam_date = m_date.group(1) if m_date else None

        # Question body
        body_el = qc.find(class_='q-body')
        if not body_el:
            body_el = qc.find(class_='question')
        
        q_text, q_html = clean_html_with_math(body_el) if body_el else ("", "")

        # Extract images
        image_urls: List[str] = []
        if body_el:
            for img in body_el.find_all('img'):
                src = img.get('src') or img.get('data-orsrc')
                if src:
                    image_urls.append(src)

        # Extract options (if MCQ)
        options: List[OptionItem] = []
        opts_container = qc.find(class_='options')
        if opts_container:
            for opt_div in opts_container.find_all(class_='option'):
                badge_el = opt_div.find(class_='option-badge')
                label = badge_el.get_text(strip=True).upper() if badge_el else "A"
                content_el = opt_div.find(class_='option-content')
                opt_text, opt_html = clean_html_with_math(content_el) if content_el else ("", "")
                # Clean out option badge text from content if duplicated
                opt_text = re.sub(r'^(?:[A-D]\b|Correct|Your answer)+', '', opt_text).strip()
                options.append(OptionItem(label=label, text=opt_text, html=opt_html))

        # Explanation and answer
        ans_box = qc.find(class_='when-answered')
        correct_ans = extract_correct_answer(ans_box, q_type)

        explanation_text = ""
        explanation_html = ""
        if ans_box:
            # Find explanation section
            expl_title = ans_box.find(lambda t: t.name in ['h2', 'h3'] and 'Explanation' in t.get_text())
            if expl_title:
                expl_section = expl_title.find_next_sibling()
                explanation_text, explanation_html = clean_html_with_math(expl_section)
            else:
                explanation_text, explanation_html = clean_html_with_math(ans_box)
            
            # Clean explanation text: remove "Option (B) is correct" redundant header if desired or keep
            for img in ans_box.find_all('img'):
                src = img.get('src') or img.get('data-orsrc')
                if src and src not in image_urls:
                    image_urls.append(src)

        has_image = len(image_urls) > 0

        question = QuestionModel(
            qid=qid,
            chapter_slug=chapter_slug,
            subject=subject,
            url=page_url,
            exam="JEE Main",
            year=year,
            paper_name=paper_name,
            exam_date=exam_date,
            shift=shift,
            question_index=q_index,
            question_type=q_type,
            question_text=q_text,
            question_html=q_html,
            options=options,
            correct_answer=correct_ans,
            explanation_text=explanation_text,
            explanation_html=explanation_html,
            has_image=has_image,
            image_urls=image_urls
        )
        questions.append(question)

    # Find next batch link
    next_url: Optional[str] = None
    next_btn = None
    for a in soup.find_all('a', href=True):
        classes = ' '.join(a.get('class', []))
        if 'q-pager-btn' in classes and 'Next' in a.get_text():
            next_btn = a
            break
    if next_btn and next_btn.get('href'):
        href = next_btn['href']
        if href.startswith('http'):
            next_url = href
        else:
            next_url = f"https://questions.examside.com{href}"

    return (questions, next_url)
