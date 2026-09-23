import os
import sys
import json
import docx
from docx.shared import Inches, Pt, RGBColor

HANDBOOK_SRC = r"D:\Projects\Placement_Master_Handbook\src"
if HANDBOOK_SRC not in sys.path:
    sys.path.insert(0, HANDBOOK_SRC)

from styles import (
    init_document, add_title, add_heading_1, add_heading_2, 
    add_heading_3, add_paragraph, add_bullet, add_callout, add_table, 
    add_code_block, add_checklist, add_tracker_table
)

WEB_ROOT = r"D:\Projects\Placement_Master_Handbook_Web"
CONTENT_DIR = os.path.join(WEB_ROOT, "content")
DAYS_DIR = os.path.join(CONTENT_DIR, "days")
EXPORTS_DIR = os.path.join(WEB_ROOT, "exports", "docx")
os.makedirs(EXPORTS_DIR, exist_ok=True)

OUTPUT_DOCX = os.path.join(EXPORTS_DIR, "Sarthak_30_Day_Placement_Master_Handbook.docx")

def build_master_docx():
    print("==========================================================")
    print("COMPILING 30-DAY MASTER HANDBOOK DOCX FROM CONTENT LAYER")
    print("==========================================================")
    
    doc = init_document()

    # Title Page
    add_title(
        doc,
        main_title="30-DAY PLACEMENT &\nSEMESTER MASTER HANDBOOK",
        subtitle="Complete Self-Contained Textbook, Solved PYQs, Aptitude Engine, Python DSA & Project Defense System",
        author="Sarthak Srivastava (3rd-Year BCA, CSJM University)",
        metadata={
            "Standard": "SGPA >= 9.0 Standard",
            "Edition": "September 2026 Master Edition",
            "Target": "Campus Placement Clearance & Production Readiness"
        }
    )

    doc.add_page_break()

    # Foreword & Architecture
    add_heading_1(doc, "Master Handbook Architecture & Ground Truth")
    add_paragraph(doc, "This master handbook is the offline compilation of the Sarthak 30-Day Placement & Semester Master Web System. It is generated directly from the identical structured content layer that powers the interactive study application.", bold_prefix="Single Source of Truth:")
    add_paragraph(doc, "Every day from Day 1 to Day 30 is a complete, self-contained study chapter containing: 1. Full textbook academic lectures, 2. Verified university PYQ model answers, 3. 4-tier worked aptitude problems with speed drills, 4. Python DSA solutions with line-by-line walks, 5. Core CS lectures with interview Q&As, 6. Real project defenses grounded in D:\\Projects code, and 7. Daily 8-question revision tests.")

    # Loop through all 30 days
    for day_num in range(1, 31):
        day_path = os.path.join(DAYS_DIR, f"day{day_num:02d}.json")
        if not os.path.exists(day_path):
            print(f"[-] Missing day{day_num:02d}.json")
            continue
            
        with open(day_path, "r", encoding="utf-8") as f:
            d = json.load(f)

        doc.add_page_break()
        print(f"--> Rendering Day {day_num:02d}: {d['title']}")
        
        add_heading_1(doc, f"DAY {day_num}: {d['title'].upper()}")
        
        sem = d.get("sem_data", {})
        apt = d.get("apt_data", {})
        
        # Header Info
        add_paragraph(doc, f"Day {day_num} of 30  |  Subject Focus: {sem.get('subject', 'General')}  |  Aptitude: {apt.get('topic', 'General')}  |  Target: SGPA >= 9.0 Standard", italic=True)

        # 1. SEMESTER ACADEMIC STUDY
        add_heading_2(doc, f"1. Semester 5 Deep Academic Lecture: {sem.get('subject', '')}")
        add_paragraph(doc, sem.get('topic', ''), bold_prefix="Syllabus Module:")
        
        for note in sem.get("detailed_notes", []):
            add_paragraph(doc, note)

        if "diagram_ascii" in sem and sem["diagram_ascii"]:
            add_paragraph(doc, "Architectural Block / Data Flow Diagram:", bold_prefix="Architecture:")
            add_code_block(doc, sem["diagram_ascii"], language="text")

        if "comparison_table" in sem and sem["comparison_table"]:
            tbl = sem["comparison_table"]
            headers = tbl.get("headers", [])
            rows = tbl.get("rows", [])
            widths = [Inches(6.5 / len(headers))] * len(headers)
            add_paragraph(doc, "Key Comparative Dimensions:", bold_prefix="Comparative Analysis:")
            add_table(doc, headers, rows, widths)

        # Callouts
        add_callout(doc, f"WHAT TO MEMORIZE (DAY {day_num})", [
            ("Core Definitions & Terminology:", sem.get('memorize', 'Master definitions.'))
        ], box_type="memorize")

        add_callout(doc, f"WHAT TO UNDERSTAND DEEPLY (DAY {day_num})", [
            ("Conceptual Mechanics & Intuition:", sem.get('understand', 'Understand mechanics.'))
        ], box_type="understand")

        if "common_mistakes" in sem and sem["common_mistakes"]:
            add_callout(doc, f"EXAM MISTAKES TO AVOID (DAY {day_num})", [
                ("Common Mark-Losing Errors:", sem['common_mistakes'])
            ], box_type="trap")

        # PYQ Model Answer
        if "pyq_question" in sem and sem["pyq_question"]:
            add_callout(doc, f"UNIVERSITY PYQ ANALYSIS & SCORING RUBRIC (DAY {day_num})", [
                ("University Examination Papers:", sem.get('pyq_year', '')),
                ("Recurrence Frequency:", sem.get('pyq_freq', '')),
                ("Actual University Question:", sem.get('pyq_question', '')),
                ("Examiner Scoring Rubric:", sem.get('pyq_rubric', ''))
            ], box_type="pyq")

            add_heading_3(doc, f"University Model Answer (15/15 Marks Blueprint)")
            for heading, body in sem.get("model_answer_paragraphs", []):
                add_paragraph(doc, body, bold_prefix=heading)

        # 2. APTITUDE
        add_heading_2(doc, f"2. Quantitative & Placement Aptitude: {apt.get('topic', '')}")
        for tut in apt.get("tutorial", []):
            add_paragraph(doc, tut)

        if "formulas" in apt and apt["formulas"]:
            add_callout(doc, "ESSENTIAL FORMULAS & SHORTCUTS", [
                ("Key Mathematical Formulas:", apt.get('formulas', '')),
                ("Speed Calculation Shortcut:", apt.get('shortcut', ''))
            ], box_type="memorize")

        add_heading_3(doc, "4-Tier Progressively Challenging Solved Problems")
        if "tier1_problem" in apt:
            add_paragraph(doc, apt["tier1_problem"], bold_prefix="Tier 1 (Foundation):")
            add_paragraph(doc, apt["tier1_solution"], bold_prefix="Solution:")
        if "tier2_problem" in apt:
            add_paragraph(doc, apt["tier2_problem"], bold_prefix="Tier 2 (Standard):")
            add_paragraph(doc, apt["tier2_solution"], bold_prefix="Solution:")
        if "tier3_problem" in apt:
            add_paragraph(doc, apt["tier3_problem"], bold_prefix="Tier 3 (Placement):")
            add_paragraph(doc, apt["tier3_solution"], bold_prefix="Solution:")
        if "tier4_problem" in apt:
            add_paragraph(doc, apt["tier4_problem"], bold_prefix="Tier 4 (Hard / Advanced):")
            add_paragraph(doc, apt["tier4_solution"], bold_prefix="Solution:")

        # 3. DSA PROBLEMS
        dsa = d.get("dsa_problems", [])
        if dsa:
            add_heading_2(doc, "3. Placement Coding & Data Structures (Python)")
            for p in dsa:
                add_heading_3(doc, f"Problem: {p.get('title', '')}")
                add_paragraph(doc, p.get('problem_statement', ''), bold_prefix="Problem Statement:")
                add_paragraph(doc, p.get('solution_approach', ''), bold_prefix="Algorithmic Approach:")
                if "code" in p:
                    add_code_block(doc, p["code"], language="python")
                add_paragraph(doc, f"Time: {p.get('time_complexity', 'O(N)')}  |  Space: {p.get('space_complexity', 'O(1)')}", bold_prefix="Complexities:")
                if "edge_cases" in p:
                    add_paragraph(doc, p["edge_cases"], bold_prefix="Edge Cases:")

        # 4. CORE CS
        cs = d.get("cs_core", {})
        if cs and "topic" in cs:
            add_heading_2(doc, f"4. Core Computer Science: {cs.get('subject', '')} — {cs.get('topic', '')}")
            for note in cs.get("detailed_notes", []):
                add_paragraph(doc, note)
            for qa in cs.get("interview_qa", []):
                add_callout(doc, f"PLACEMENT INTERVIEW Q&A: {qa['q']}", [
                    ("Expected Technical Answer:", qa['a'])
                ], box_type="understand")

        # 5. PROJECT DEFENSE
        proj = d.get("project_defense", {})
        if proj and "project_name" in proj:
            add_heading_2(doc, f"5. Project Architecture Defense: {proj.get('project_name', '')}")
            add_paragraph(doc, proj.get('architecture_deep_dive', ''))
            for qa in proj.get("interview_qa", []):
                add_callout(doc, f"PROJECT INTERVIEW DEFENSE: {qa['q']}", [
                    ("Strong Architectural Answer:", qa['a'])
                ], box_type="memorize")

        # 6. DAILY TEST
        test = d.get("daily_test", {})
        if test and "questions" in test:
            add_heading_2(doc, f"6. Day {day_num} Comprehensive 8-Question Mastery Test")
            q_rows = []
            for idx, q in enumerate(test.get("questions", []), 1):
                q_rows.append([f"Q{idx}", q["q"], q["a"]])
            add_table(doc, ["No.", "Question", "Full Solution"], q_rows, [Inches(0.6), Inches(2.9), Inches(3.0)])

    # Save final DOCX
    print(f"\n--> Saving final DOCX to: {OUTPUT_DOCX}")
    doc.save(OUTPUT_DOCX)
    print(f"--> SUCCESS! Master Handbook DOCX compiled ({os.path.getsize(OUTPUT_DOCX) / 1024 / 1024:.2f} MB)")

if __name__ == "__main__":
    build_master_docx()
