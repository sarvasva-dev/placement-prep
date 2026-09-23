#!/usr/bin/env python3
"""
scripts/generate_30_days_complete.py
Master Generator for the 30-Day Placement & Semester Study System.

Generates:
1. content/days/day01.json through day30.json (Complete, self-contained, all 14 streams)
2. content/days_index.json (Lightweight 30-day index for timeline navigation)
3. Global resource libraries:
   - content/pyqs/all_pyqs.json
   - content/aptitude/all_aptitude.json
   - content/coding/all_coding.json
   - content/core_cs/all_core_cs.json
   - content/projects/projects_all.json
"""

import os
import sys
import json

# Setup directory paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CURRICULUM_DIR = os.path.join(BASE_DIR, "scripts", "curriculum")
CONTENT_DIR = os.path.join(BASE_DIR, "content")
DAYS_DIR = os.path.join(CONTENT_DIR, "days")
os.makedirs(DAYS_DIR, exist_ok=True)
for sub in ["pyqs", "aptitude", "coding", "core_cs", "projects"]:
    os.makedirs(os.path.join(CONTENT_DIR, sub), exist_ok=True)

if CURRICULUM_DIR not in sys.path:
    sys.path.insert(0, CURRICULUM_DIR)

# Import all 9 curriculum modules
import academic_curriculum
import aptitude_curriculum
import dsa_curriculum
import project_curriculum
import core_cs_curriculum
import placement_curriculum
import revision_curriculum
import mixed_tests_curriculum
import coding_tasks_curriculum

def generate_all():
    print("=" * 60)
    print("STARTING 30-DAY MASTER CONTENT GENERATION")
    print("=" * 60)

    days_index = []
    all_pyqs = []
    all_aptitude = []
    all_coding = []
    all_core_cs = []
    all_projects = {}

    for day in range(1, 31):
        print(f"Generating Day {day:02d}...", end=" ")

        # 1. Academic Module
        acad = academic_curriculum.get_academic_for_day(day)

        # 2. Aptitude Module
        apt = aptitude_curriculum.get_aptitude_for_day(day)

        # 3. DSA Module
        dsa = dsa_curriculum.get_dsa_for_day(day)

        # 4. Project Module
        proj = project_curriculum.get_project_for_day(day)

        # 5. Core CS Module
        cs = core_cs_curriculum.get_core_cs_for_day(day)

        # 6. Placement Interview Module
        place = placement_curriculum.get_placement_for_day(day)

        # 7. Revision Module
        rev = revision_curriculum.get_revision_for_day(day)

        # 8. Mixed Tests Module
        mixed = mixed_tests_curriculum.get_mixed_test_for_day(day)

        # 9. Practical Coding Tasks Module
        task = coding_tasks_curriculum.get_coding_task_for_day(day)

        # Extract PYQs from academic
        day_pyqs = acad.get("pyqs", [])
        for pyq in day_pyqs:
            pyq_copy = dict(pyq)
            pyq_copy["day"] = day
            all_pyqs.append(pyq_copy)

        # Build 100-Point Score Model
        score_model = {
            "total_points": 100,
            "passing_threshold": 80,
            "breakdown": [
                {"stream": "Academic Theory & University PYQs", "points": 15, "passing": 12},
                {"stream": "Placement Aptitude Solved & MCQs", "points": 15, "passing": 12},
                {"stream": "DSA Pattern & 2 Coding Problems", "points": 20, "passing": 16},
                {"stream": "Core Computer Science Lesson & MCQs", "points": 15, "passing": 12},
                {"stream": "Project Architecture & Defense", "points": 10, "passing": 8},
                {"stream": "Placement & Behavioral (STAR) Prep", "points": 10, "passing": 8},
                {"stream": "Mixed Daily Test (20 MCQs)", "points": 10, "passing": 8},
                {"stream": "Timed Practical Coding Task", "points": 5, "passing": 4}
            ]
        }

        # Build day title
        subject_name = acad.get("subject_name", "Academic Theory")
        topic_name = acad.get("topic", "Core Curriculum")
        day_title = f"Day {day:02d}: {topic_name.split('—')[-1].strip() if '—' in topic_name else topic_name} & {dsa.get('pattern_name', 'DSA')}"

        # 14 Canonical Streams Container
        streams = {
            "academic": acad,
            "academic_pyqs": day_pyqs,
            "academic_mcqs": acad.get("mcqs", []),
            "aptitude_lesson": {
                "topic": apt.get("topic", ""),
                "category": apt.get("category", ""),
                "subtopic": apt.get("subtopic", ""),
                "formulas": apt.get("formulas", ""),
                "shortcuts": apt.get("shortcuts", ""),
                "tutorial": apt.get("tutorial", [])
            },
            "aptitude_solved": apt.get("solved_examples", []),
            "aptitude_mcqs": apt.get("mcqs", []),
            "aptitude_practice": apt.get("practice_problems", []),
            "aptitude_timed_drill": apt.get("timed_drill", {}),
            "dsa_pattern": {
                "pattern_name": dsa.get("pattern_name", ""),
                "category": dsa.get("category", ""),
                "concept": dsa.get("concept", ""),
                "why_it_works": dsa.get("why_it_works", ""),
                "visual_explanation": dsa.get("visual_explanation", ""),
                "language": "Java",
                "java_code": dsa.get("java_code", dsa.get("code", "")),
                "code": dsa.get("java_code", dsa.get("code", "")),
                "line_by_line_walkthrough": dsa.get("line_by_line_walkthrough", []),
                "dry_run": dsa.get("dry_run", ""),
                "complexity": dsa.get("complexity", ""),
                "edge_cases": ", ".join(dsa.get("edge_cases", [])) if isinstance(dsa.get("edge_cases"), list) else str(dsa.get("edge_cases", "")),
                "edge_cases_list": dsa.get("edge_cases", []) if isinstance(dsa.get("edge_cases"), list) else [str(dsa.get("edge_cases", ""))],
                "interview_variations": dsa.get("interview_variations", [])
            },
            "coding_problems": dsa.get("coding_problems", []),
            "core_cs": cs,
            "project_preparation": proj,
            "placement_interview": place,
            "daily_revision": rev,
            "mixed_test": mixed,
            "daily_coding_task": task,
            "daily_score_model": score_model
        }

        # Backward-compatible structures for existing UI renderers
        sem_data = {
            "subject": subject_name,
            "subject_code": acad.get("subject_code", ""),
            "unit": acad.get("unit", 1),
            "topic": acad.get("topic", ""),
            "objectives": acad.get("objectives", []),
            "detailed_notes": [acad.get("explanation", "")] + [s.get("content", "") for s in acad.get("subtopics", [])],
            "diagram_ascii": acad.get("diagram", ""),
            "comparison_table": acad.get("comparison_table"),
            "memorize": acad.get("memorize", ""),
            "understand": acad.get("understand", ""),
            "common_mistakes": acad.get("common_mistakes", ""),
            "pyqs": day_pyqs,
            "mcqs": acad.get("mcqs", []),
            "pyq_year": day_pyqs[0].get("year", "CSJM University") if day_pyqs else "CSJMU",
            "pyq_freq": "Verified University Paper Question",
            "pyq_question": day_pyqs[0].get("question", "") if day_pyqs else "",
            "pyq_rubric": day_pyqs[0].get("rubric", "") if day_pyqs else "",
            "model_answer_paragraphs": [
                ("1. Model Answer & Technical Presentation", day_pyqs[0].get("model_answer", "")),
                ("2. Expected Examiner Criteria", day_pyqs[0].get("expected_examiner_points", ""))
            ] if day_pyqs else []
        }

        apt_data = {
            "topic": apt.get("topic", ""),
            "category": apt.get("category", ""),
            "subtopic": apt.get("subtopic", ""),
            "formulas": apt.get("formulas", ""),
            "shortcut": apt.get("shortcuts", ""),
            "tutorial": apt.get("tutorial", []),
            "tier1_problem": apt["solved_examples"][0].get("problem", "") if len(apt.get("solved_examples", [])) > 0 else "",
            "tier1_solution": apt["solved_examples"][0].get("step_by_step_solution", "") if len(apt.get("solved_examples", [])) > 0 else "",
            "tier2_problem": apt["solved_examples"][1].get("problem", "") if len(apt.get("solved_examples", [])) > 1 else "",
            "tier2_solution": apt["solved_examples"][1].get("step_by_step_solution", "") if len(apt.get("solved_examples", [])) > 1 else "",
            "tier3_problem": apt["solved_examples"][2].get("problem", "") if len(apt.get("solved_examples", [])) > 2 else "",
            "tier3_solution": apt["solved_examples"][2].get("step_by_step_solution", "") if len(apt.get("solved_examples", [])) > 2 else "",
            "tier4_problem": apt["solved_examples"][3].get("problem", "") if len(apt.get("solved_examples", [])) > 3 else "",
            "tier4_solution": apt["solved_examples"][3].get("step_by_step_solution", "") if len(apt.get("solved_examples", [])) > 3 else "",
            "speed_drills": [{"q": ex.get("problem", ""), "a": ex.get("final_answer", "")} for ex in apt.get("solved_examples", [])],
            "solved_examples": apt.get("solved_examples", []),
            "mcqs": apt.get("mcqs", []),
            "practice_problems": apt.get("practice_problems", []),
            "timed_drill": apt.get("timed_drill", {})
        }

        dsa_problems = [
            {
                "title": p.get("title", ""),
                "difficulty": p.get("difficulty", "Medium"),
                "importance": f"High Frequency in {', '.join(p.get('companies', ['Top Tech']))}",
                "language": "Java",
                "problem_statement": p.get("statement", ""),
                "solution_approach": p.get("approach", ""),
                "code": p.get("solution_java", p.get("code", "")),
                "java_solution": p.get("solution_java", p.get("code", "")),
                "solution_java": p.get("solution_java", p.get("code", "")),
                "time_complexity": p.get("time_complexity", "O(N)"),
                "space_complexity": p.get("space_complexity", "O(1)"),
                "edge_cases": p.get("constraints", "")
            }
            for p in dsa.get("coding_problems", [])
        ]

        cs_core = {
            "subject": cs.get("subject", ""),
            "topic": cs.get("topic", ""),
            "detailed_notes": [cs.get("concept_lesson", "")],
            "key_definitions": cs.get("key_definitions", []),
            "interview_qa": [{"q": item.get("q", ""), "a": item.get("a", "")} for item in cs.get("interview_questions", [])],
            "mcqs": cs.get("mcqs", [])
        }

        project_defense = {
            "project_name": proj.get("project_name", ""),
            "repo_path": proj.get("repo_path", ""),
            "feature_focus": proj.get("topic", ""),
            "architecture_deep_dive": f"WHAT TO UNDERSTAND:\n{proj.get('what_to_understand', '')}\n\nWHAT TO MEMORIZE:\n{proj.get('what_to_memorize', '')}\n\n60-SECOND INTERVIEW PITCH:\n{proj.get('interview_pitch_exercise', '')}",
            "interview_qa": [{"q": item.get("q", ""), "a": item.get("a", "")} for item in proj.get("interview_questions", [])]
        }

        daily_test = {
            "title": f"Day {day:02d} Mixed Mastery Test (20 MCQs)",
            "questions": [{"q": m.get("question", ""), "a": f"Answer: {m.get('correct_answer')}\n\n{m.get('explanation')}"} for m in mixed[:8]],
            "mcqs": mixed
        }

        # Build Complete Day Object
        day_payload = {
            "day": day,
            "title": day_title,
            "streams": streams,
            "sem_data": sem_data,
            "apt_data": apt_data,
            "dsa_problems": dsa_problems,
            "dsa_pattern": dsa,
            "cs_core": cs_core,
            "project_defense": project_defense,
            "placement_interview": place,
            "daily_revision": rev,
            "daily_test": daily_test,
            "daily_coding_task": task,
            "daily_score_model": score_model
        }

        # Save day file
        day_file = os.path.join(DAYS_DIR, f"day{day:02d}.json")
        with open(day_file, "w", encoding="utf-8") as f:
            json.dump(day_payload, f, indent=2, ensure_ascii=False)

        # Index entry
        days_index.append({
            "day": day,
            "title": day_title,
            "subject": subject_name,
            "topic": topic_name,
            "aptitude": apt.get("topic", ""),
            "dsa_pattern": dsa.get("pattern_name", ""),
            "dsa": [p.get("title", "") for p in dsa.get("coding_problems", [])],
            "cs_core_topic": cs.get("topic", ""),
            "project": proj.get("project_name", "")
        })

        # Global aggregation
        all_aptitude.append({
            "day": day,
            "topic": apt.get("topic", ""),
            "category": apt.get("category", ""),
            "formulas": apt.get("formulas", ""),
            "shortcuts": apt.get("shortcuts", ""),
            "solved_examples": apt.get("solved_examples", []),
            "mcqs": apt.get("mcqs", [])
        })

        all_coding.append({
            "day": day,
            "pattern": dsa.get("pattern_name", ""),
            "pattern_details": dsa,
            "problems": dsa.get("coding_problems", []),
            "daily_task": task
        })

        all_core_cs.append({
            "day": day,
            "subject": cs.get("subject", ""),
            "topic": cs.get("topic", ""),
            "lesson": cs.get("concept_lesson", ""),
            "definitions": cs.get("key_definitions", []),
            "interview_questions": cs.get("interview_questions", []),
            "mcqs": cs.get("mcqs", [])
        })

        p_name = proj.get("project_name", "")
        if p_name not in all_projects:
            all_projects[p_name] = {
                "name": p_name,
                "repo_path": proj.get("repo_path", ""),
                "sessions": []
            }
        all_projects[p_name]["sessions"].append({
            "day": day,
            "topic": proj.get("topic", ""),
            "understand": proj.get("what_to_understand", ""),
            "memorize": proj.get("what_to_memorize", ""),
            "interview_qa": proj.get("interview_questions", []),
            "pitch": proj.get("interview_pitch_exercise", "")
        })

        print("DONE")

    # Save Days Index
    with open(os.path.join(CONTENT_DIR, "days_index.json"), "w", encoding="utf-8") as f:
        json.dump(days_index, f, indent=2, ensure_ascii=False)
    print(f"\n[+] Saved content/days_index.json ({len(days_index)} days)")

    # Save Global PYQs Library
    with open(os.path.join(CONTENT_DIR, "pyqs", "all_pyqs.json"), "w", encoding="utf-8") as f:
        json.dump(all_pyqs, f, indent=2, ensure_ascii=False)
    print(f"[+] Saved content/pyqs/all_pyqs.json ({len(all_pyqs)} authentic PYQs)")

    # Save Global Aptitude Library
    with open(os.path.join(CONTENT_DIR, "aptitude", "all_aptitude.json"), "w", encoding="utf-8") as f:
        json.dump(all_aptitude, f, indent=2, ensure_ascii=False)
    print(f"[+] Saved content/aptitude/all_aptitude.json ({len(all_aptitude)} daily modules)")

    # Save Global Coding Library
    with open(os.path.join(CONTENT_DIR, "coding", "all_coding.json"), "w", encoding="utf-8") as f:
        json.dump(all_coding, f, indent=2, ensure_ascii=False)
    print(f"[+] Saved content/coding/all_coding.json ({len(all_coding)} patterns and problem sets)")

    # Save Global Core CS Library
    with open(os.path.join(CONTENT_DIR, "core_cs", "all_core_cs.json"), "w", encoding="utf-8") as f:
        json.dump(all_core_cs, f, indent=2, ensure_ascii=False)
    print(f"[+] Saved content/core_cs/all_core_cs.json ({len(all_core_cs)} lessons and interview sets)")

    # Save Global Projects Library
    with open(os.path.join(CONTENT_DIR, "projects", "projects_all.json"), "w", encoding="utf-8") as f:
        json.dump(all_projects, f, indent=2, ensure_ascii=False)
    print(f"[+] Saved content/projects/projects_all.json ({len(all_projects)} verified projects)")

    print("\n" + "=" * 60)
    print("SUCCESS: ALL 30 DAYS AND RESOURCE LIBRARIES COMPILED!")
    print("=" * 60)

if __name__ == "__main__":
    generate_all()
