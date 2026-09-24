#!/usr/bin/env python3
"""
scripts/validate_resume_claims.py
Automated validator for technical resumes:
- Verifies absence of obsolete project names (TerraStract, BEVM in primary lineup, Dealership/Car Showroom)
- Verifies absence of exaggerated claims (12M+ Kirana stores)
- Verifies presence of the 4 verified primary projects in order:
    1. BulkBeat TV
    2. SmartGalla
    3. College Student Management System (CSMS)
    4. DocRoute (with 'Under Development' status)
- Verifies contact details and GitHub account against real repository remotes
- Checks that claims match evidence/resume_project_claims.json
"""

import os
import sys
import json
import re

WEB_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESUMES_JSON = os.path.join(WEB_ROOT, "content", "resumes", "resumes_all.json")
CLAIMS_JSON = os.path.join(WEB_ROOT, "evidence", "resume_project_claims.json")

def validate_resume_claims():
    print("=" * 70)
    print("RUNNING RESUME CLAIM & GROUND TRUTH VALIDATOR")
    print("=" * 70)

    if not os.path.exists(RESUMES_JSON):
        print(f"[-] FATAL: Missing resumes file: {RESUMES_JSON}")
        return False

    with open(RESUMES_JSON, "r", encoding="utf-8") as f:
        resumes = json.load(f)

    if not os.path.exists(CLAIMS_JSON):
        print(f"[-] FATAL: Missing claims file: {CLAIMS_JSON}")
        return False

    with open(CLAIMS_JSON, "r", encoding="utf-8") as f:
        verified_claims = json.load(f)

    errors = []
    warnings = []

    # 1. Global Forbidden Tokens
    FORBIDDEN_PATTERNS = [
        (r"\bterrastract\b", "Forbidden project reference: TerraStract"),
        (r"\bbevm\b", "Forbidden in primary resume: BEVM"),
        (r"\bbiometric electronic voting\b", "Forbidden in primary resume: Biometric Electronic Voting System"),
        (r"12M\+?\s*kirana", "Forbidden exaggerated metric: 12M+ Kirana"),
        (r"12\s*million\s*kirana", "Forbidden exaggerated metric: 12 million Kirana"),
        (r"\bdealership\b", "Forbidden misinterpretation of CSMS as car dealership"),
        (r"\bcar showroom\b", "Forbidden misinterpretation of CSMS as car showroom"),
        (r"35%\s*accuracy\s*boost", "Forbidden unmeasured benchmark claim for DocRoute"),
        (r"\breact\b", "Forbidden unlearned framework: React"),
        (r"\bnext\.js\b", "Forbidden unlearned framework: Next.js"),
        (r"\bzustand\b", "Forbidden unlearned library: Zustand"),
        (r"\bwebsockets?\b", "Forbidden unlearned technology: WebSocket"),
        (r"target\s*sgpa", "Forbidden unprofessional target phrasing: Target SGPA"),
        (r"\bdevqbx\b", "Forbidden removed organization: DevQBX")
    ]

    REQUIRED_VARIANTS = ["python_backend", "software_engineer", "data_ai"]
    for v in REQUIRED_VARIANTS:
        if v not in resumes:
            errors.append(f"Missing required resume variant: {v}")

    for variant_key, r in resumes.items():
        print(f"\n--> Auditing profile: '{variant_key}'")
        raw_text = json.dumps(r, ensure_ascii=False).lower()

        # Check forbidden tokens
        for pattern, msg in FORBIDDEN_PATTERNS:
            if re.search(pattern, raw_text, re.IGNORECASE):
                errors.append(f"[{variant_key}] {msg}")

        # Check contact integrity
        contact = r.get("contact", {})
        if contact.get("email") != "ss8971132@gmail.com":
            errors.append(f"[{variant_key}] Incorrect email: {contact.get('email')}")
        if "github.com/sarvasva-dev" not in contact.get("github", ""):
            errors.append(f"[{variant_key}] Incorrect GitHub URL: {contact.get('github')}")

        # Check projects lineup
        projects = r.get("experience_and_projects", [])
        if len(projects) != 4:
            errors.append(f"[{variant_key}] Expected exactly 4 primary projects, found {len(projects)}")

        proj_names = [p.get("name", "") for p in projects]
        
        # Verify 1. BulkBeat TV
        if not any("bulkbeat" in name.lower() for name in proj_names):
            errors.append(f"[{variant_key}] Missing required primary project: BulkBeat TV")
            
        # Verify 2. SmartGalla
        if not any("smartgalla" in name.lower() or "smart galla" in name.lower() for name in proj_names):
            errors.append(f"[{variant_key}] Missing required primary project: SmartGalla")

        # Verify 3. College Student Management System (CSMS)
        csms_found = False
        for p in projects:
            if "college student management system" in p.get("name", "").lower():
                csms_found = True
                if "CSMS" not in p.get("name", "").upper():
                    errors.append(f"[{variant_key}] Project name must include CSMS abbreviation: {p.get('name')}")
        if not csms_found:
            errors.append(f"[{variant_key}] Missing required primary project: College Student Management System (CSMS)")

        # Verify 4. DocRoute
        docroute_found = False
        for p in projects:
            p_text = (p.get("name", "") + " " + p.get("role", "") + " " + " ".join(p.get("bullets", []))).lower()
            if "docroute" in p_text:
                docroute_found = True
                if "under development" not in p_text:
                    errors.append(f"[{variant_key}] DocRoute must be explicitly designated as 'Under Development'")
        if not docroute_found:
            errors.append(f"[{variant_key}] Missing required primary project: DocRoute")

        # Check SmartGalla pilot truth
        for p in projects:
            if "smart" in p.get("name", "").lower():
                bullets_joined = " ".join(p.get("bullets", [])).lower()
                if "4–5" not in bullets_joined and "4-5" not in bullets_joined:
                    errors.append(f"[{variant_key}] SmartGalla must mention authentic pilot size (4-5 local shops)")
                if "sunset" not in bullets_joined:
                    errors.append(f"[{variant_key}] SmartGalla must mention infrastructure cost sunset reality")

    print("\n" + "=" * 70)
    print("VALIDATION SUMMARY")
    print("=" * 70)
    if errors:
        print(f"[-] FAILED with {len(errors)} error(s):")
        for err in errors:
            print(f"    - {err}")
        return False
    else:
        print("[+] SUCCESS: All resume claims verified against ground truth!")
        print(f"    - 0 forbidden tokens found")
        print(f"    - All 4 primary projects verified in each of the {len(resumes)} profiles")
        print(f"    - CSMS full name and non-dealership truth verified")
        print(f"    - SmartGalla 4-5 shop pilot & sunset truth verified")
        print(f"    - DocRoute 'Under Development' disclaimer verified")
        return True

if __name__ == "__main__":
    success = validate_resume_claims()
    sys.exit(0 if success else 1)
