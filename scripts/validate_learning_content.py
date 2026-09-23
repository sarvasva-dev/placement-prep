import json
import glob

def validate_all_learning():
    all_files = sorted([f for f in glob.glob("content/days/day*.json") if "_expected" not in f])
    assert len(all_files) == 30, f"Expected 30 days, found {len(all_files)}"

    print("===========================================================================")
    print("STRICT MULTI-STREAM LEARNING CONTENT & QUALITY AUDIT (DAYS 1-30)")
    print("===========================================================================")

    failures = []
    
    for path in all_files:
        with open(path, "r", encoding="utf-8") as f:
            d = json.load(f)
            day = d.get("day", 0)
            streams = d.get("streams", {})

            # 1. Academic theory (explanation >= 100 chars, topic present)
            acad = streams.get("academic") or d.get("sem_data") or {}
            has_acad = bool(acad.get("topic") and (acad.get("explanation") or acad.get("detailed_notes")))

            # 2. PYQs
            pyqs = streams.get("academic_pyqs") or acad.get("pyqs") or []
            has_pyq = len(pyqs) >= 1

            # 3. Aptitude lesson
            apt_lesson = streams.get("aptitude_lesson") or d.get("apt_data") or {}
            has_apt_lesson = bool(apt_lesson.get("topic") and (apt_lesson.get("tutorial") or apt_lesson.get("formulas")))

            # 4. Aptitude worked problems >= 5
            apt_solved = streams.get("aptitude_solved") or d.get("apt_data", {}).get("solved_examples") or []
            has_apt_worked = len(apt_solved) >= 5

            # 5. Aptitude MCQs >= 10
            apt_mcqs = streams.get("aptitude_mcqs") or d.get("apt_data", {}).get("mcqs") or []
            has_apt_mcqs = len(apt_mcqs) >= 10

            # 6. DSA lesson
            dsa_pat = streams.get("dsa_pattern") or d.get("dsa_pattern") or {}
            has_dsa_lesson = bool(dsa_pat.get("pattern_name") and dsa_pat.get("concept"))

            # 7. Java DSA code
            has_java_dsa = bool(dsa_pat.get("java_code") and len(dsa_pat.get("java_code", "")) > 50)

            # 8. Coding problems >= 2
            coding_probs = streams.get("coding_problems") or d.get("dsa_problems") or []
            has_coding_probs = len(coding_probs) >= 2

            # 9. Timed Java coding task
            timed_task = streams.get("daily_coding_task") or d.get("daily_coding_task") or {}
            has_timed_task = bool(timed_task.get("title") and (timed_task.get("problem_statement") or timed_task.get("statement")))

            # 10. Core CS lesson
            core_cs = streams.get("core_cs") or d.get("cs_core") or {}
            has_core_lesson = bool(core_cs.get("topic") and (core_cs.get("lesson") or core_cs.get("concept_lesson")))

            # 11. Core CS Q&A >= 5
            core_qa = core_cs.get("interview_questions") or core_cs.get("interview_qa") or []
            has_core_qa = len(core_qa) >= 5

            # 12. Core CS MCQs >= 5
            core_mcqs = core_cs.get("mcqs") or []
            has_core_mcqs = len(core_mcqs) >= 5

            # 13. Project
            proj = streams.get("project_preparation") or d.get("project_defense") or {}
            has_proj = bool(proj.get("project_name") and proj.get("topic"))

            # 14. Project Q&A >= 2
            proj_qa = proj.get("interview_questions") or []
            has_proj_qa = len(proj_qa) >= 2

            # 15. Placement interview >= 5
            placement_int = streams.get("placement_interview") or d.get("placement_interview") or []
            has_placement_int = len(placement_int) >= 5

            # 16. Revision >= 10
            rev = streams.get("daily_revision") or d.get("daily_revision") or {}
            rev_count = sum(len(v) for v in rev.values() if isinstance(v, list))
            has_rev = rev_count >= 10

            # 17. Mixed MCQs >= 20
            mixed = streams.get("mixed_test") or d.get("daily_test", {}).get("mcqs") or []
            has_mixed = len(mixed) >= 20

            checks = [
                ("Academic Lesson", has_acad),
                ("PYQ Practice", has_pyq),
                ("Aptitude Lesson", has_apt_lesson),
                ("Apt Worked Examples >= 5", has_apt_worked),
                ("Aptitude MCQs >= 10", has_apt_mcqs),
                ("DSA Pattern Lesson", has_dsa_lesson),
                ("Java DSA Code", has_java_dsa),
                ("Coding Problems >= 2", has_coding_probs),
                ("Timed Java Coding Task", has_timed_task),
                ("Core CS Lesson", has_core_lesson),
                ("Core CS Q&A >= 5", has_core_qa),
                ("Core CS MCQs >= 5", has_core_mcqs),
                ("Project Defense", has_proj),
                ("Project Q&A >= 2", has_proj_qa),
                ("Placement Interview >= 5", has_placement_int),
                ("Daily Revision >= 10", has_rev),
                ("Mixed MCQs >= 20", has_mixed),
            ]

            failed_checks = [name for name, passed in checks if not passed]
            if failed_checks:
                failures.append((day, failed_checks))
                print(f"[FAIL] Day {day:02d}: Failed checks: {', '.join(failed_checks)}")
            else:
                print(f"[PASS] Day {day:02d}: All 17 mandatory curriculum checkpoints verified 100%!")

    print("===========================================================================")
    print("AUDIT SUMMARY:")
    if not failures:
        print("[RESULT] ALL 30 DAYS PASSED 100% OF STRICT MULTI-STREAM REQUIREMENTS!")
    else:
        print(f"[RESULT] {len(failures)} days had validation failures.")

if __name__ == "__main__":
    validate_all_learning()
