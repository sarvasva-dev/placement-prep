#!/usr/bin/env python3
"""
scripts/test_resume_print.py
Playwright Automated Test Suite for Resume 1-Page A4 Printing & Export:
1. Opens browser and navigates to #resumes.
2. For each profile (python_backend, software_engineer, data_ai):
   - Switches to profile tab.
   - Uses Playwright page.pdf() with exact A4 page specifications.
   - Saves to exports/resumes/Sarthak_Backend_Resume.pdf, etc.
   - Audits generated PDF page count using pypdf:
     STRICT REQUIREMENT: len(pages) == 1. Fails if pages > 1.
3. Tests responsive viewports (320x568 to 1440x900) for preview integrity.
4. Outputs test evidence to evidence/resume_print_test_report.json.
"""

import os
import sys
import json
import time
from pathlib import Path
from playwright.sync_api import sync_playwright
import pypdf

sys.stdout.reconfigure(encoding='utf-8')

WEB_ROOT = Path(__file__).resolve().parent.parent
EXPORTS_DIR = WEB_ROOT / "exports" / "resumes"
EVIDENCE_DIR = WEB_ROOT / "evidence"
SCREENSHOTS_DIR = EVIDENCE_DIR / "screenshots"

EXPORTS_DIR.mkdir(parents=True, exist_ok=True)
SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)

BASE_URL = "http://localhost:8000"

PROFILES = [
    {
        "key": "python_backend",
        "tab_label": "Python Backend Developer",
        "output_pdf": EXPORTS_DIR / "Sarthak_Backend_Resume.pdf",
        "title": "Python Backend Developer"
    },
    {
        "key": "software_engineer",
        "tab_label": "Software Engineer (SDE)",
        "output_pdf": EXPORTS_DIR / "Sarthak_Software_Engineer_Resume.pdf",
        "title": "Software Development Engineer"
    },
    {
        "key": "data_ai",
        "tab_label": "Data & AI Systems Engineer",
        "output_pdf": EXPORTS_DIR / "Sarthak_Data_AI_Resume.pdf",
        "title": "Data & AI Systems Engineer"
    }
]

VIEWPORTS = [
    {"name": "iPhone SE", "width": 320, "height": 568},
    {"name": "iPhone X / 11 Pro", "width": 375, "height": 812},
    {"name": "iPhone 12 / 13 Pro", "width": 390, "height": 844},
    {"name": "Pixel 7 / Android", "width": 412, "height": 915},
    {"name": "iPad Portrait", "width": 768, "height": 1024},
    {"name": "HD Laptop", "width": 1280, "height": 720},
    {"name": "Large Desktop", "width": 1440, "height": 900}
]

def run_resume_tests():
    print("=" * 70)
    print("STARTING PLAYWRIGHT RESUME 1-PAGE A4 PRINT & EXPORT TEST SUITE")
    print("=" * 70)

    report = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "pdf_exports": [],
        "responsive_checks": [],
        "summary": {}
    }

    all_passed = True

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, channel="msedge")
        context = browser.new_context(viewport={"width": 1280, "height": 800})
        page = context.new_page()

        console_errors = []
        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)

        print("\n--- STEP 1: EXPORTING & VALIDATING EXACT 1-PAGE A4 PDFS ---")
        page.goto(f"{BASE_URL}/#resumes")
        page.wait_for_selector(".resume-print-container", timeout=8000)
        time.sleep(0.5)

        for prof in PROFILES:
            prof_key = prof["key"]
            out_file = prof["output_pdf"]
            print(f"\n--> Processing Profile: '{prof['title']}' ({prof_key})")

            # Click tab
            tab_btn = page.locator(f"button.resume-tab-btn[data-profile='{prof_key}']")
            tab_btn.click()
            time.sleep(0.3)

            # Generate PDF via print emulation
            page.emulate_media(media="print")
            page.pdf(
                path=str(out_file),
                format="A4",
                print_background=True,
                margin={
                    "top": "0.4in",
                    "bottom": "0.4in",
                    "left": "0.45in",
                    "right": "0.45in"
                }
            )
            # Revert back to screen
            page.emulate_media(media="screen")

            # Validate PDF Page Count
            if not out_file.exists():
                print(f"  [-] ERROR: PDF file not generated at: {out_file}")
                all_passed = False
                continue

            reader = pypdf.PdfReader(str(out_file))
            page_count = len(reader.pages)
            size_kb = out_file.stat().st_size / 1024

            status = "PASS" if page_count == 1 else "FAIL"
            print(f"  [PDF GENERATED]: {out_file.name} ({size_kb:.1f} KB)")
            print(f"  [PAGE COUNT]:    {page_count} page(s) -> {status}")

            if page_count != 1:
                print(f"  [-] FATAL: Resume exceeded 1 page! Must be EXACTLY 1 page.")
                all_passed = False

            report["pdf_exports"].append({
                "profile": prof_key,
                "title": prof["title"],
                "file": str(out_file),
                "file_name": out_file.name,
                "file_size_kb": round(size_kb, 1),
                "page_count": page_count,
                "status": status
            })

        print("\n--- STEP 2: RESPONSIVE SCREEN PREVIEW VERIFICATION ---")
        for vp in VIEWPORTS:
            vp_name = vp["name"]
            w, h = vp["width"], vp["height"]
            print(f"--> Testing viewport {w}x{h} ({vp_name})")

            page.set_viewport_size({"width": w, "height": h})
            time.sleep(0.2)

            container = page.locator(".resume-print-container")
            is_visible = container.is_visible()
            box = container.bounding_box()

            passed = is_visible and box and box["width"] > 0
            if passed:
                print(f"  [PASS] Rendered width: {box['width']}px, height: {box['height']}px")
            else:
                print(f"  [-] FAIL: Resume container not visible at {w}x{h}")
                all_passed = False

            report["responsive_checks"].append({
                "viewport": vp_name,
                "width": w,
                "height": h,
                "visible": is_visible,
                "status": "PASS" if passed else "FAIL"
            })

        # Capture a desktop preview screenshot
        page.set_viewport_size({"width": 1280, "height": 900})
        ss_path = SCREENSHOTS_DIR / "resume_screen_preview.png"
        page.locator(".resume-print-container").screenshot(path=str(ss_path))
        print(f"\n[SCREENSHOT] Saved preview to: {ss_path}")

        browser.close()

    report["summary"] = {
        "all_passed": all_passed,
        "total_pdf_checks": len(report["pdf_exports"]),
        "passed_pdf_checks": sum(1 for p in report["pdf_exports"] if p["status"] == "PASS"),
        "total_responsive_checks": len(report["responsive_checks"]),
        "passed_responsive_checks": sum(1 for r in report["responsive_checks"] if r["status"] == "PASS")
    }

    report_path = EVIDENCE_DIR / "resume_print_test_report.json"
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print("\n" + "=" * 70)
    print("TEST SUITE SUMMARY")
    print("=" * 70)
    print(f"Total PDF Profiles Tested: {len(report['pdf_exports'])}")
    print(f"Single Page Compliance:    {report['summary']['passed_pdf_checks']} / {len(report['pdf_exports'])} PASS")
    print(f"Responsive Viewports:      {report['summary']['passed_responsive_checks']} / {len(report['responsive_checks'])} PASS")
    print(f"Overall Status:            {'ALL PASS' if all_passed else 'FAIL'}")
    print(f"Evidence Report:           {report_path}")
    print("=" * 70)

    return all_passed

if __name__ == "__main__":
    success = run_resume_tests()
    sys.exit(0 if success else 1)
