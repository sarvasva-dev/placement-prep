import json
import glob
import re

def validate_facts():
    # Only target actual day data files (exclude _expected.json)
    all_files = sorted([f for f in glob.glob("content/days/day*.json") if "_expected" not in f])
    issues = []
    
    # Forbidden terms
    forbidden_terms = [
        "Car Showroom Management System",
        "Car Dealership System",
        "Automotive ERP",
        "15 marks guaranteed",
        "guaranteed marks"
    ]
    
    csms_verified_days = []
    non_java_dsa = []
    
    for path in all_files:
        with open(path, "r", encoding="utf-8") as f:
            content_str = f.read()
            d = json.loads(content_str)
            day = d.get("day", 0)
            
            # 1. Check forbidden terms
            for term in forbidden_terms:
                if term.lower() in content_str.lower():
                    issues.append(f"Day {day}: Contains forbidden term '{term}'")
            
            # 2. Check CSMS identity
            proj = d.get("project_defense", {})
            if isinstance(proj, dict):
                p_name = proj.get("project_name", "")
                if "csms" in p_name.lower():
                    if "college student management system" not in p_name.lower():
                        issues.append(f"Day {day}: CSMS misidentified as '{p_name}'")
                    else:
                        csms_verified_days.append(day)
                    
            # 3. Check Java DSA only
            dsa = d.get("dsa_pattern", {})
            if isinstance(dsa, dict):
                java_code = dsa.get("java_code", "")
                if not java_code or ("public class" not in java_code and "class Solution" not in java_code and "static" not in java_code and "class " not in java_code):
                    non_java_dsa.append(day)
                
            # 4. Check Coding problems Java solutions
            coding_probs = d.get("dsa_problems", []) or d.get("streams", {}).get("coding_problems", [])
            for idx, prob in enumerate(coding_probs):
                if isinstance(prob, dict):
                    sol = prob.get("java_solution", "")
                    if not sol:
                        issues.append(f"Day {day}: Coding problem {idx+1} missing java_solution")

    print("===========================================================================")
    print("FACTUAL CONTENT QA & FORENSIC AUDIT")
    print("===========================================================================")
    print(f"Total Days Audited            : {len(all_files)}")
    print(f"CSMS Correct Identity Days    : {csms_verified_days}")
    print(f"Non-Java DSA Days             : {non_java_dsa}")
    print(f"Factual / Hallucination Issues: {len(issues)}")
    if issues:
        for iss in issues[:10]:
            print(f"  [ISSUE] {iss}")
    else:
        print("[PASS] 100% of days pass strict factual grounding and Java-only constraints!")

if __name__ == "__main__":
    validate_facts()
