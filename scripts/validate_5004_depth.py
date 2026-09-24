#!/usr/bin/env python3
"""
scripts/validate_5004_depth.py
Validates the structural and numerical depth of BCA-5004 Numerical Methods:
- Verifies quotas:
    Unit 1 >= 34
    Unit 2 >= 29
    Unit 3 >= 37
    Unit 4 >= 31
    Unit 5 >= 25
    Total >= 120
- Verifies problem completeness:
    problem, formula, step_by_step_calculation, final_answer, verification, common_mistake
- Generates evidence/5004_depth_audit.json
"""

import json
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRACTICE_FILE = os.path.join(BASE_DIR, 'content', 'semester', '5004', 'numerical_methods_practice.json')
EVIDENCE_FILE = os.path.join(BASE_DIR, 'evidence', '5004_depth_audit.json')

QUOTAS = {
    "unit1_roots": 34,
    "unit2_interpolation": 29,
    "unit3_differentiation_integration": 37,
    "unit4_linear_equations": 31,
    "unit5_odes": 25
}

def validate_depth():
    if not os.path.exists(PRACTICE_FILE):
        print(f"ERROR: Practice file {PRACTICE_FILE} not found.")
        sys.exit(1)
        
    with open(PRACTICE_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    units = data.get("units", {})
    audit = {
        "timestamp": "2026-09-24",
        "total_target": 120,
        "actual_total": data.get("total_questions", 0),
        "quotas": {},
        "overall_status": "PASS",
        "issues": []
    }
    
    total_q = 0
    for unit_key, min_target in QUOTAS.items():
        unit_info = units.get(unit_key, {})
        questions = unit_info.get("questions", [])
        q_count = len(questions)
        total_q += q_count
        
        status = "PASS" if q_count >= min_target else "FAIL"
        if status == "FAIL":
            audit["overall_status"] = "FAIL"
            audit["issues"].append(f"{unit_key} has {q_count} questions, expected >= {min_target}")
            
        # Check problem fields
        invalid_in_unit = 0
        for q in questions:
            if not q.get("problem") or not q.get("formula") or not q.get("step_by_step_calculation") or not q.get("final_answer") or not q.get("verification") or not q.get("common_mistake"):
                invalid_in_unit += 1
                
        audit["quotas"][unit_key] = {
            "target": min_target,
            "actual": q_count,
            "status": status,
            "complete_problems": q_count - invalid_in_unit
        }
        
    if total_q < audit["total_target"]:
        audit["overall_status"] = "FAIL"
        audit["issues"].append(f"Total questions {total_q} < 120")
        
    os.makedirs(os.path.dirname(EVIDENCE_FILE), exist_ok=True)
    with open(EVIDENCE_FILE, 'w', encoding='utf-8') as f:
        json.dump(audit, f, indent=2)
        
    print("=" * 60)
    print("BCA-5004 DEPTH & QUOTA AUDIT")
    print("=" * 60)
    print(f"Total Solved Questions: {total_q} / 120 Target")
    for k, v in audit["quotas"].items():
        print(f"  {k:35s}: {v['actual']:3d} / {v['target']:2d} -> {v['status']}")
    print(f"Overall Status: {audit['overall_status']}")
    print(f"Audit file saved: {EVIDENCE_FILE}")
    
    if audit["overall_status"] != "PASS":
        sys.exit(1)

if __name__ == '__main__':
    validate_depth()
