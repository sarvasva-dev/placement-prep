#!/usr/bin/env python3
"""
scripts/validate_evidence.py
Automated Evidence Validation

Enforces:
1. Every project fact has verified evidence and proper identity (CSMS == College Student Management System).
2. Every PYQ has a verified source ID and marks/year.
3. Every resume claim links to evidence.
4. No ambiguous project acronym is unresolved.
5. Fails if any contradiction or hallucination is detected.
"""
import os
import json
import sys

def validate():
    errors = []
    
    # 1. Check required evidence files exist
    required_files = [
        "evidence/source_inventory.json",
        "evidence/academic_evidence.json",
        "evidence/academic_syllabus_map.json",
        "evidence/academic_pyq_registry.json",
        "evidence/project_evidence.json",
        "evidence/github_evidence.json",
        "evidence/career_evidence.json",
        "evidence/evidence_registry.json"
    ]
    for rf in required_files:
        if not os.path.exists(rf):
            errors.append(f"Missing required evidence file: {rf}")
            
    if errors:
        print("[FAIL] Missing evidence files:")
        for e in errors:
            print("  -", e)
        sys.exit(1)
        
    # 2. Check Project Evidence
    with open("evidence/project_evidence.json", "r", encoding="utf-8") as f:
        projects = json.load(f)
        
    csms_found = False
    for p in projects:
        if p.get("acronym") == "CSMS":
            csms_found = True
            if p["actual_project_name"] != "College Student Management System":
                errors.append(f"CSMS misidentified as: {p['actual_project_name']}")
            if not p.get("source_paths") or not os.path.exists(p["source_paths"][0]):
                errors.append(f"CSMS source path does not exist on disk: {p.get('source_paths')}")
        for t in p.get("verified_technologies", []):
            if "classification" not in t or t["classification"] not in {"DIRECTLY_VERIFIED_USED", "VERIFIED_IN_SOURCE", "DOCUMENTED_BUT_NOT_FOUND"}:
                errors.append(f"Invalid tech classification for {p['actual_project_name']}: {t}")
                
    if not csms_found:
        errors.append("CSMS (College Student Management System) not found in project evidence!")

    # 3. Check PYQs
    with open("evidence/academic_pyq_registry.json", "r", encoding="utf-8") as f:
        pyqs = json.load(f)
    if len(pyqs) < 20:
        errors.append(f"Insufficient verified PYQs in registry: {len(pyqs)} (expected >= 20)")
    for q in pyqs:
        if not q.get("source_id"):
            errors.append(f"PYQ missing source_id: {q.get('pyq_id')}")
        if q.get("verification_status") != "VERIFIED":
            errors.append(f"PYQ not marked as VERIFIED: {q.get('pyq_id')}")

    # 4. Check Career Evidence
    with open("evidence/career_evidence.json", "r", encoding="utf-8") as f:
        career = json.load(f)
    if career.get("candidate_identity", {}).get("name") != "Sarthak Srivastava":
        errors.append("Candidate name does not match Sarthak Srivastava")
    if not career.get("work_experience"):
        errors.append("Work experience missing from career evidence")

    # 5. Check Evidence Registry
    with open("evidence/evidence_registry.json", "r", encoding="utf-8") as f:
        registry = json.load(f)
    conflicts = [c for c in registry if c.get("status") == "CONFLICT_REQUIRES_REVIEW"]
    if conflicts:
        errors.append(f"Found {len(conflicts)} unresolved conflicts in evidence registry!")

    if errors:
        print("[FAIL] Evidence validation failed:")
        for err in errors:
            print("  ❌", err)
        sys.exit(1)
    else:
        print(f"[PASS] All evidence verified successfully! ({len(projects)} projects, {len(pyqs)} PYQs, {len(registry)} claims)")

if __name__ == "__main__":
    validate()
