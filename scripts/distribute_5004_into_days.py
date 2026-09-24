#!/usr/bin/env python3
"""
scripts/distribute_5004_into_days.py
Injects rich numerical worked problems, practice questions, formula recall,
and timed numerical drills into Day 05, 10, 15, 19, 23, and 27 JSON files
directly from the verified BCA-5004 master practice bank.
"""

import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DAYS_DIR = os.path.join(BASE_DIR, 'content', 'days')
PRACTICE_FILE = os.path.join(BASE_DIR, 'content', 'semester', '5004', 'numerical_methods_practice.json')

with open(PRACTICE_FILE, 'r', encoding='utf-8') as f:
    practice_data = json.load(f)

units = practice_data.get('units', {})

# Mapping of days to units
DAY_UNIT_MAPPING = {
    5: {
        "unit_key": "unit1_roots",
        "slice_worked": (0, 4),      # 4 Bisection problems
        "slice_practice": (4, 10),   # 6 practice problems
        "drill_idx": 7,              # B8 Bisection iteration bound
        "formula_recall": "Bisection: c = (a+b)/2. Error bound: |b-a|/2^n < epsilon. Sign check: f(a)*f(b) < 0."
    },
    10: {
        "unit_key": "unit1_roots",
        "slice_worked": (16, 21),    # 5 Newton-Raphson problems
        "slice_practice": (8, 16),   # 8 Regula-Falsi practice problems
        "drill_idx": 21,             # Heron's sqrt(12) extraction
        "formula_recall": "Newton-Raphson: x_{n+1} = x_n - f(x_n)/f'(x_n). Quadratic convergence e_{n+1} \u2248 C*e_n^2 requires simple root f'(r) != 0. Regula-Falsi: x_r = (a*f(b) - b*f(a))/(f(b) - f(a))."
    },
    15: {
        "unit_key": "unit4_linear_equations",
        "slice_worked": (0, 4),      # 4 Gauss Elimination
        "slice_practice": (4, 10),   # Gauss-Jordan problems
        "drill_idx": 3,              # Partial pivoting 0.0003x
        "formula_recall": "Gauss Elimination: Forward elimination to upper triangular matrix U, then backward substitution. Partial pivoting swaps row with max |a_ik| to avoid division by small pivots."
    },
    19: {
        "unit_key": "unit4_linear_equations",
        "slice_worked": (14, 19),    # Gauss-Seidel & Jacobi worked
        "slice_practice": (20, 28),  # 8 practice problems
        "drill_idx": 15,             # 27x + 6y - z = 85 (CSJMU 15-mark)
        "formula_recall": "Gauss-Seidel: x_i^{(k+1)} = (1/a_ii)[b_i - \u2211_{j<i} a_ij x_j^{(k+1)} - \u2211_{j>i} a_ij x_j^{(k)}]. Strictly diagonally dominant (|a_ii| > \u2211_{j!=i}|a_ij|) OR symmetric positive-definite (Ostrowski-Reich) guarantees convergence."
    },
    23: {
        "unit_key": "unit3_differentiation_integration",
        "slice_worked": (8, 13),     # Trapezoidal & Simpson 1/3 worked
        "slice_practice": (13, 22),  # 9 Simpson 1/3 and 3/8 practice problems
        "drill_idx": 9,              # Simpson 1/3 on 1/(1+x^2)
        "formula_recall": "Trapezoidal: I = (h/2)[(y0+yn) + 2\u2211 y_mid]. Simpson 1/3: I = (h/3)[(y0+yn) + 4\u2211 y_odd + 2\u2211 y_even] (requires EVEN n). Simpson 3/8: I = (3h/8)[(y0+yn) + 3\u2211 y_non3 + 2\u2211 y_mult3] (requires n MULTIPLE OF 3)."
    },
    27: {
        "unit_key": "unit5_odes",
        "slice_worked": (17, 22),    # RK4 worked problems
        "slice_practice": (0, 10),   # Euler & Modified Euler practice problems
        "drill_idx": 18,             # dy/dx = (y-x)/(y+x) RK4
        "formula_recall": "RK4: k1=h*f(x_n, y_n); k2=h*f(x_n+h/2, y_n+k1/2); k3=h*f(x_n+h/2, y_n+k2/2); k4=h*f(x_n+h, y_n+k3); y_{n+1} = y_n + (1/6)[k1 + 2k2 + 2k3 + k4]. Local truncation error O(h^5), global error O(h^4)."
    }
}

for day_num, cfg in DAY_UNIT_MAPPING.items():
    day_file = os.path.join(DAYS_DIR, f"day{day_num:02d}.json")
    if not os.path.exists(day_file):
        continue
        
    with open(day_file, 'r', encoding='utf-8') as f:
        d = json.load(f)
        
    q_list = units[cfg["unit_key"]]["questions"]
    worked = q_list[cfg["slice_worked"][0] : cfg["slice_worked"][1]]
    practice = q_list[cfg["slice_practice"][0] : cfg["slice_practice"][1]]
    drill_q = q_list[cfg["drill_idx"]]
    
    acad = d.setdefault('streams', {}).setdefault('academic', {})
    
    acad['worked_numerical_problems'] = worked
    acad['expanded_numerical_practice'] = practice
    acad['timed_numerical_drill'] = {
        "problem_id": drill_q["problem_id"],
        "title": f"Timed Exam Drill: {drill_q['topic']}",
        "time_limit_minutes": 15,
        "marks": 15,
        "problem": drill_q["problem"],
        "formula": drill_q["formula"],
        "final_answer": drill_q["final_answer"],
        "verification": drill_q["verification"],
        "common_mistake": drill_q["common_mistake"]
    }
    acad['formula_recall'] = cfg['formula_recall']
    
    with open(day_file, 'w', encoding='utf-8') as f:
        json.dump(d, f, indent=2)
        
    print(f"Updated Day {day_num:02d}: {len(worked)} worked problems, {len(practice)} practice problems, 1 timed drill.")

print("All 5004 days successfully updated with verified numerical problem sets!")
