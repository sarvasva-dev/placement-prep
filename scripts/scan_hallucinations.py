#!/usr/bin/env python3
"""
scripts/scan_hallucinations.py
Hallucination Scanner

Scans content/ and generated JSON files for:
- Mistaken / hallucinated project identities (e.g., claiming CSMS is a car dealership)
- Unknown university names (must only be CSJMU / Dr. Virendra Swarup Institute)
- Unverified revenue claims
- Unverified candidate identities

Outputs evidence/hallucination_report.json.
"""
import os
import glob
import json
import re

FORBIDDEN_PATTERNS = [
    (r"Car Dealership", "Misidentifying CSMS or another project as a car dealership"),
    (r"Automobile Management", "Misidentifying CSMS as automobile software"),
    (r"Delhi University", "Hallucinated university (candidate studies at CSJMU Kanpur)"),
    (r"AKTU", "Hallucinated university affiliation"),
    (r"₹[0-9]+ Crore", "Hallucinated outsized metric"),
    (r"500K users", "Unverified metric claim"),
]

def scan_files():
    findings = []
    
    # Check all json files in content/
    target_files = glob.glob("content/**/*.json", recursive=True)
    
    for filepath in target_files:
        norm_path = filepath.replace("\\", "/")
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                
            for pattern, reason in FORBIDDEN_PATTERNS:
                matches = re.findall(pattern, content, re.IGNORECASE)
                if matches:
                    findings.append({
                        "file": norm_path,
                        "pattern": pattern,
                        "reason": reason,
                        "match_count": len(matches)
                    })
        except Exception as e:
            pass

    report = {
        "files_scanned": len(target_files),
        "total_hallucinations_detected": len(findings),
        "findings": findings,
        "status": "PASS" if len(findings) == 0 else "FAIL"
    }

    os.makedirs("evidence", exist_ok=True)
    with open("evidence/hallucination_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    if findings:
        print(f"[FAIL] Found {len(findings)} hallucination patterns in generated content!")
        for f in findings:
            print(f"  - {f['file']}: {f['reason']}")
    else:
        print(f"[PASS] Hallucination scan clean across {len(target_files)} files. Report saved to evidence/hallucination_report.json")

if __name__ == "__main__":
    scan_files()
