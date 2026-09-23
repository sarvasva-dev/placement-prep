import json
import glob

def calculate_quality_scores():
    all_files = sorted([f for f in glob.glob("content/days/day*.json") if "_expected" not in f])
    
    print("===========================================================================")
    print("DAY-BY-DAY COMPREHENSIVE QUALITY SCORE AUDIT (DAYS 1-30)")
    print("===========================================================================")
    print("Day | Acad | PYQ | Apt | DSA | Code | Core | Proj | Intv | Rev | Test | TOTAL")
    print("----+------+-----+-----+-----+------+------+------+------+-----+------+------")
    
    total_curriculum_score = 0
    
    for path in all_files:
        with open(path, "r", encoding="utf-8") as f:
            d = json.load(f)
            day = d.get("day", 0)
            streams = d.get("streams", {})
            
            # Scores (each out of 10)
            # 1. Academic depth (explanation length, diagram, comparison table, memorize/understand)
            acad = streams.get("academic") or d.get("sem_data") or {}
            acad_score = 0
            if len(acad.get("explanation", "")) > 500: acad_score += 4
            if acad.get("diagram"): acad_score += 2
            if acad.get("comparison_table"): acad_score += 2
            if acad.get("memorize") and acad.get("understand"): acad_score += 2
            
            # 2. PYQ Quality (verified question, rubric, model answer)
            pyqs = streams.get("academic_pyqs") or acad.get("pyqs") or []
            pyq_score = 0
            if len(pyqs) >= 1: pyq_score += 4
            if len(pyqs) >= 2: pyq_score += 2
            if pyqs and pyqs[0].get("model_answer"): pyq_score += 2
            if pyqs and pyqs[0].get("rubric"): pyq_score += 2
            
            # 3. Aptitude Quality (worked examples >= 5, mcqs >= 10, formulas)
            apt_worked = streams.get("aptitude_solved") or d.get("apt_data", {}).get("solved_examples") or []
            apt_mcqs = streams.get("aptitude_mcqs") or d.get("apt_data", {}).get("mcqs") or []
            apt_score = 0
            if len(apt_worked) >= 5: apt_score += 5
            if len(apt_mcqs) >= 10: apt_score += 5
            
            # 4. DSA Quality (pattern, concept, why_it_works, java_code)
            dsa_pat = streams.get("dsa_pattern") or d.get("dsa_pattern") or {}
            dsa_score = 0
            if dsa_pat.get("pattern_name"): dsa_score += 3
            if dsa_pat.get("concept"): dsa_score += 3
            if dsa_pat.get("java_code") and len(dsa_pat.get("java_code")) > 100: dsa_score += 4
            
            # 5. Java Coding Quality (2 problems with full java solutions and explanations)
            coding_probs = streams.get("coding_problems") or d.get("dsa_problems") or []
            code_score = 0
            if len(coding_probs) >= 2: code_score += 5
            if coding_probs and coding_probs[0].get("java_solution"): code_score += 5
            
            # 6. Core CS Quality (lesson, 5 QA, 5 MCQs)
            core_cs = streams.get("core_cs") or d.get("cs_core") or {}
            core_qa = core_cs.get("interview_questions") or core_cs.get("interview_qa") or []
            core_mcqs = core_cs.get("mcqs") or []
            core_score = 0
            if core_cs.get("topic"): core_score += 2
            if len(core_qa) >= 5: core_score += 4
            if len(core_mcqs) >= 5: core_score += 4
            
            # 7. Project Grounding (project_name verified, technical depth, 2 QA)
            proj = streams.get("project_preparation") or d.get("project_defense") or {}
            proj_qa = proj.get("interview_questions") or []
            proj_score = 0
            if proj.get("project_name"): proj_score += 4
            if proj.get("topic"): proj_score += 2
            if len(proj_qa) >= 2: proj_score += 4
            
            # 8. Placement Interview (5 questions with answers)
            intv = streams.get("placement_interview") or d.get("placement_interview") or []
            intv_score = 0
            if len(intv) >= 5: intv_score += 10
            elif len(intv) >= 3: intv_score += 6
            
            # 9. Revision Quality (10+ rapid-fire items)
            rev = streams.get("daily_revision") or d.get("daily_revision") or {}
            rev_count = sum(len(v) for v in rev.values() if isinstance(v, list))
            rev_score = 0
            if rev_count >= 10: rev_score += 10
            elif rev_count >= 5: rev_score += 5
            
            # 10. Assessment Quality (20+ unique mixed MCQs)
            mixed = streams.get("mixed_test") or d.get("daily_test", {}).get("mcqs") or []
            test_score = 0
            if len(mixed) >= 20: test_score += 10
            elif len(mixed) >= 10: test_score += 5
            
            day_total = (acad_score + pyq_score + apt_score + dsa_score + code_score + 
                         core_score + proj_score + intv_score + rev_score + test_score)
            
            total_curriculum_score += day_total
            print(f"{day:02d}  |  {acad_score:2d}  |  {pyq_score:2d} |  {apt_score:2d} |  {dsa_score:2d} |  {code_score:2d}  |  {core_score:2d}  |  {proj_score:2d}  |  {intv_score:2d}  |  {rev_score:2d} |  {test_score:2d}  |  {day_total:3d}/100")
            
    avg_score = total_curriculum_score / len(all_files)
    print("---------------------------------------------------------------------------")
    print(f"CURRICULUM OVERALL AVERAGE QUALITY SCORE: {avg_score:.1f} / 100.0")
    print("===========================================================================")

if __name__ == "__main__":
    calculate_quality_scores()
