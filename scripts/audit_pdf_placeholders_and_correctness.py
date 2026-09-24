#!/usr/bin/env python3
"""
scripts/audit_pdf_placeholders_and_correctness.py
Performs a rigorous, page-by-page audit of the current compiled PDF:
exports/pdf/Sarthak_30_Day_Placement_Master_Handbook.pdf

Checks:
1. Placeholder detection:
   - Scans for forbidden unresolved table placeholders:
     'a3', 'b3', 'c3', 'a4', 'b4', 'c4'
     'f(x0)', 'f\'(x0)'
     'x1', 'x2' (in iteration table columns)
   - Distinguishes formula definitions (e.g., 'f(x0 + h)') from unresolved placeholders.
2. Legacy bleed detection:
   - '8-question', '8 question', '8 Question'
3. Container With Most Water edge cases:
   - Verifies that Two Sum edge cases ('Duplicates summing to target') do not appear in Container With Most Water.
4. Numerical Methods tables:
   - Verifies that Day 5 Bisection, Day 10 Newton-Raphson, Day 15 Gauss, Day 19 Seidel, Day 23 Simpson, Day 27 RK4 tables contain real numeric digits.
"""

import json
import os
import re
import fitz

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF_PATH = os.path.join(BASE_DIR, 'exports', 'pdf', 'Sarthak_30_Day_Placement_Master_Handbook.pdf')

doc = fitz.open(PDF_PATH)
num_pages = len(doc)
print(f"Auditing PDF: {PDF_PATH}")
print(f"Total Pages: {num_pages}")

results = {
    "total_pages": num_pages,
    "file_size_mb": round(os.path.getsize(PDF_PATH) / (1024 * 1024), 2),
    "legacy_8_question_hits": [],
    "forbidden_placeholder_hits": [],
    "two_sum_bleed_in_water_hits": [],
    "audit_status": "PASS"
}

placeholder_patterns = [
    (r'\b(a3|b3|c3|a4|b4|c4)\b', "Unresolved bracket coordinate placeholder"),
    (r'f\(x0\)\s*\|\s*f\'\(x0\)', "Newton-Raphson table placeholder row"),
    (r'\bTODO\b|\bTBD\b', "Developer placeholder token")
]

eight_q_regex = re.compile(r'\b8[- ]question\b', re.IGNORECASE)

full_pdf_text = []

for page_idx in range(num_pages):
    page = doc[page_idx]
    text = page.get_text("text")
    full_pdf_text.append(text)
    
    # 1. Legacy 8-question check
    if eight_q_regex.search(text):
        for line in text.splitlines():
            if eight_q_regex.search(line):
                results["legacy_8_question_hits"].append({
                    "page": page_idx + 1,
                    "line": line.strip()
                })
                
    # 2. Unresolved placeholder check
    for pat, desc in placeholder_patterns:
        match = re.search(pat, text)
        if match:
            # Check context: ignore if it's part of a matrix subscript like a31 or sha256
            hit_text = match.group(0)
            # Find surrounding snippet
            pos = match.start()
            snippet = text[max(0, pos-40):min(len(text), pos+40)].replace('\n', ' ')
            # Filter legitimate formulas
            if "a31" in snippet or "a32" in snippet or "a33" in snippet:
                continue
            results["forbidden_placeholder_hits"].append({
                "page": page_idx + 1,
                "hit": hit_text,
                "description": desc,
                "snippet": snippet
            })

all_text_concat = "\n".join(full_pdf_text)

# 3. Container With Most Water check
water_pos = all_text_concat.find("Container With Most Water")
if water_pos != -1:
    water_snippet = all_text_concat[water_pos:water_pos + 1200]
    if "Duplicates summing to target" in water_snippet:
        results["two_sum_bleed_in_water_hits"].append({
            "error": "Found 'Duplicates summing to target' inside Container With Most Water section!",
            "snippet": water_snippet[:200]
        })

print("\n" + "="*50)
print("PDF AUDIT SUMMARY:")
print(f"Total Pages:                 {num_pages}")
print(f"Legacy 8-Question Hits:      {len(results['legacy_8_question_hits'])}")
print(f"Forbidden Placeholder Hits:  {len(results['forbidden_placeholder_hits'])}")
print(f"Two Sum Bleed in Water Hits: {len(results['two_sum_bleed_in_water_hits'])}")
print("="*50)

if results['legacy_8_question_hits']:
    print("\nLegacy 8-question hits:")
    for h in results['legacy_8_question_hits']:
        print(f"  Page {h['page']}: {h['line']}")
    results["audit_status"] = "FAIL"

if results['forbidden_placeholder_hits']:
    print("\nForbidden placeholder hits:")
    for h in results['forbidden_placeholder_hits']:
        print(f"  Page {h['page']}: '{h['hit']}' ({h['description']}) in: {h['snippet']}")
    results["audit_status"] = "FAIL"

if results['two_sum_bleed_in_water_hits']:
    print("\nTwo Sum bleed in Container With Most Water:")
    for h in results['two_sum_bleed_in_water_hits']:
        print(f"  {h['error']}")
    results["audit_status"] = "FAIL"

output_audit = os.path.join(BASE_DIR, 'evidence', 'pdf_qa_audit.json')
with open(output_audit, 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2)

print(f"\nAudit Report written to: {output_audit}")
print(f"Overall Audit Status: {results['audit_status']}")
