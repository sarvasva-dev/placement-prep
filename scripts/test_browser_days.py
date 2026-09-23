import sys
import os
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

def run_tests():
    print("=" * 70)
    print("STARTING REAL BROWSER HEADLESS QA ON LOCALHOST:8000 (MSEDGE)")
    print("=" * 70)

    test_days = [1, 2, 3, 5, 10, 15, 20, 25, 30]
    all_passed = True
    screenshot_dir = Path("evidence") / "screenshots"
    screenshot_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, channel="msedge")
        context = browser.new_context(viewport={"width": 1440, "height": 900})
        page = context.new_page()

        console_errors = []
        page_errors = []

        def on_console(msg):
            if msg.type == "error":
                console_errors.append(f"[Console Error] {msg.text}")

        def on_page_error(err):
            page_errors.append(f"[Page Error] {str(err)}")

        page.on("console", on_console)
        page.on("pageerror", on_page_error)

        for day in test_days:
            url = f"http://localhost:8000/#day/{day}"
            print(f"\n--> Testing Day {day:02d} at {url}...")

            console_errors.clear()
            page_errors.clear()

            page.goto(url, wait_until="networkidle", timeout=20000)
            # Give UI time to complete rendering
            page.wait_for_timeout(1000)

            # Check for error cards or crash UI
            error_cards = page.locator(".error-card").count()
            if error_cards > 0:
                print(f"[FAIL] Day {day:02d}: Red error-card detected!")
                all_passed = False
                continue

            if page_errors:
                print(f"[FAIL] Day {day:02d}: Uncaught page errors detected:")
                for pe in page_errors:
                    print(f"       {pe}")
                all_passed = False
                continue

            # Check console errors
            critical_console_errors = [e for e in console_errors if "favicon" not in e.lower()]
            if critical_console_errors:
                print(f"[FAIL] Day {day:02d}: Console errors found:")
                for ce in critical_console_errors:
                    print(f"       {ce}")
                all_passed = False
                continue

            # Check key stream elements
            has_academic = page.locator("#sec-acad").count() > 0
            has_pyq = page.locator("#sec-pyq").count() > 0
            has_apt_lesson = page.locator("#sec-apt-lesson").count() > 0
            has_apt_solved = page.locator("#sec-apt-solved").count() > 0
            has_apt_mcq = page.locator("#sec-apt-mcq").count() > 0
            has_dsa_pattern = page.locator("#sec-dsa-pattern").count() > 0
            has_coding_probs = page.locator("#sec-coding-probs").count() > 0
            has_core_cs = page.locator("#sec-core-cs").count() > 0
            has_project = page.locator("#sec-proj-defense").count() > 0
            has_interview = page.locator("#sec-interview-prep").count() > 0
            has_revision = page.locator("#sec-revision").count() > 0
            has_mixed_test = page.locator("#sec-mixed-test").count() > 0
            has_coding_task = page.locator("#sec-coding-task").count() > 0
            has_sign_off = page.locator("#sec-sign-off").count() > 0

            # Check MCQ counts
            apt_mcq_count = page.locator("#sec-apt-mcq .mcq-interactive-card").count()
            mixed_mcq_count = page.locator("#sec-mixed-test .mcq-interactive-card").count()

            # Check Java content in DSA and Coding
            dsa_text = page.locator("#sec-dsa-pattern").inner_text() if has_dsa_pattern else ""
            coding_text = page.locator("#sec-coding-probs").inner_text() if has_coding_probs else ""
            task_text = page.locator("#sec-coding-task").inner_text() if has_coding_task else ""

            is_java = ("class Solution" in dsa_text or "public class" in dsa_text or "public " in dsa_text) and ("def " not in dsa_text[:300])

            print(f"    Streams Check: Acad={has_academic}, PYQ={has_pyq}, Apt={has_apt_lesson}, AptMCQs={apt_mcq_count}/10, DSA={has_dsa_pattern} (Java={is_java}), JavaCoding={has_coding_probs}, CoreCS={has_core_cs}, Proj={has_project}, Interview={has_interview}, Rev={has_revision}, MixedTest={mixed_mcq_count}/20, Task={has_coding_task}, SignOff={has_sign_off}")

            streams_ok = (
                has_academic and has_pyq and has_apt_lesson and
                apt_mcq_count >= 10 and has_dsa_pattern and has_coding_probs and
                has_core_cs and has_project and has_interview and
                has_revision and mixed_mcq_count >= 20 and has_coding_task and has_sign_off and is_java
            )

            if streams_ok:
                print(f"[PASS] Day {day:02d}: Successfully rendered all 14 streams cleanly with 0 console errors!")
            else:
                print(f"[FAIL] Day {day:02d}: Missing stream elements or MCQ counts or Java verification!")
                all_passed = False

            if day == 1:
                screenshot_path = screenshot_dir / "day01_browser_verified.png"
                page.screenshot(path=str(screenshot_path), full_page=False)
                print(f"    [+] Saved Day 1 browser screenshot to {screenshot_path}")

        browser.close()

    print("\n" + "=" * 70)
    if all_passed:
        print("OVERALL BROWSER QA: ALL 9 TESTED DAYS PASSED 100% WITH ZERO ERRORS!")
        print("=" * 70)
        sys.exit(0)
    else:
        print("OVERALL BROWSER QA: ONE OR MORE DAYS FAILED BROWSER QA!")
        print("=" * 70)
        sys.exit(1)

if __name__ == "__main__":
    run_tests()
