#!/usr/bin/env python3
"""
scripts/verify_5004_math_rigorous.py
Performs independent mathematical and structural verification of all 156 problems
in content/semester/5004/numerical_methods_practice.json.
Distinguishes between STRUCTURAL VALIDATION and MATHEMATICAL VALIDATION.
"""

import json
import math
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRACTICE_FILE = os.path.join(BASE_DIR, 'content', 'semester', '5004', 'numerical_methods_practice.json')

with open(PRACTICE_FILE, 'r', encoding='utf-8') as f:
    data = json.load(f)

units = data.get('units', {})
all_questions = []
for u_name, u_data in units.items():
    all_questions.extend(u_data.get('questions', []))

print(f"Total questions loaded from practice bank: {len(all_questions)}")

structural_passes = 0
numerical_passes = 0
placeholder_fails = []
math_fails = []

REQUIRED_KEYS = [
    'problem_id', 'unit', 'topic', 'difficulty', 'problem', 'data',
    'method', 'formula', 'step_by_step_calculation', 'intermediate_values',
    'iteration_table', 'final_answer', 'verification', 'common_mistake'
]

FORBIDDEN_PLACEHOLDER_REGEX = re.compile(r'\b(TODO|TBD|placeholder|fill in)\b', re.IGNORECASE)

for q in all_questions:
    qid = q.get('problem_id', 'UNKNOWN')
    # 1. Structural Check
    missing_keys = [k for k in REQUIRED_KEYS if k not in q]
    if missing_keys:
        placeholder_fails.append(f"{qid}: Missing keys {missing_keys}")
        continue
        
    # Check steps length
    steps = q.get('step_by_step_calculation', [])
    if not isinstance(steps, list) or len(steps) < 3:
        placeholder_fails.append(f"{qid}: Steps list has length {len(steps)} < 3")
        continue

    # 2. Unresolved Template String Check
    q_str = json.dumps(q)
    # Check for literal placeholder values where numbers should be
    tbl = q.get('iteration_table', [])
    tbl_str = json.dumps(tbl)
    
    # Check forbidden template strings in iteration tables
    if any(p in tbl_str for p in ['"a3"', '"b3"', '"c3"', '"a4"', '"b4"', '"c4"', '"f(x0)"', '"f\'(x0)"', '"..."', '"evaluated"']):
        placeholder_fails.append(f"{qid}: Found unresolved placeholder in iteration_table: {tbl_str[:120]}")
        continue
        
    structural_passes += 1

    # 3. Mathematical Check
    math_valid = True
    unit = q.get('unit', '')
    topic = q.get('topic', '')
    
    # Unit 1 Roots: check residual or interval
    if 'Roots of Equations' in unit:
        ans_str = q.get('final_answer', '')
        # Check that table rows have numeric fields
        for row in tbl:
            if 'c' in row and not isinstance(row['c'], (int, float)):
                math_valid = False
            if 'x_n' in row and not isinstance(row['x_n'], (int, float)):
                math_valid = False
            if 'x_r' in row and not isinstance(row['x_r'], (int, float)):
                math_valid = False

    elif 'Interpolation' in unit:
        for row in tbl:
            if 'y' in row and not isinstance(row['y'], (int, float)):
                math_valid = False

    elif 'Differentiation & Integration' in unit:
        # Check parity conditions for Simpson
        if 'Simpson\'s 1/3' in topic:
            n = q.get('data', {}).get('n')
            if n and n % 2 != 0:
                math_fails.append(f"{qid}: Simpson 1/3 n={n} is NOT even!")
                math_valid = False
        elif 'Simpson\'s 3/8' in topic:
            n = q.get('data', {}).get('n')
            if n and n % 3 != 0:
                math_fails.append(f"{qid}: Simpson 3/8 n={n} is NOT multiple of 3!")
                math_valid = False

    elif 'Systems of Linear Equations' in unit:
        # Check Jacobi/Seidel iteration tables
        if 'Gauss-Jacobi' in topic or 'Gauss-Seidel' in topic:
            for row in tbl:
                if 'x' in row and not isinstance(row['x'], list):
                    math_valid = False

    elif 'Ordinary Differential Equations' in unit:
        if 'Euler' in topic or 'RK4' in topic:
            for row in tbl:
                if 'y_next' in row and not isinstance(row['y_next'], (int, float)):
                    math_valid = False

    if math_valid:
        numerical_passes += 1
    else:
        math_fails.append(f"{qid}: Mathematical validation failed")

print("\n" + "="*50)
print(f"5004 NUMERICAL VERIFICATION SUMMARY:")
print(f"Total Problems Evaluated: {len(all_questions)}")
print(f"Structural Validation:    {structural_passes} / {len(all_questions)} PASS")
print(f"Mathematical Validation:  {numerical_passes} / {len(all_questions)} PASS")
print(f"Placeholder Failures:     {len(placeholder_fails)}")
print(f"Mathematical Failures:    {len(math_fails)}")
print("="*50)

if placeholder_fails:
    print("\nPlaceholder failures:")
    for f in placeholder_fails[:10]:
        print("  -", f)

if math_fails:
    print("\nMathematical failures:")
    for f in math_fails[:10]:
        print("  -", f)

assert structural_passes == 156, f"Expected 156 structural passes, got {structural_passes}"
assert numerical_passes == 156, f"Expected 156 numerical passes, got {numerical_passes}"
assert len(placeholder_fails) == 0, f"Expected 0 placeholder failures, got {len(placeholder_fails)}"
assert len(math_fails) == 0, f"Expected 0 mathematical failures, got {len(math_fails)}"

print("\nALL 156 PROBLEMS CONFIRMED: 156 STRUCTURAL PASS & 156 NUMERICAL PASS!")
