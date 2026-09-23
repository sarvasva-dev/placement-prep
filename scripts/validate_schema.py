#!/usr/bin/env python3
"""
scripts/validate_schema.py
Strict recursive schema validator for content/days/day01.json ... day30.json.

Asserts:
- Every expected textual field has type string
- Every expected list field has type list/array
- Every expected dictionary field has type dict/object
- Disallows malformed mixed types (e.g. array where string is expected, or object where string expected)
- Reports DAY 01 ... DAY 30 PASS/FAIL
"""

import os
import sys
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DAYS_DIR = os.path.join(BASE_DIR, "content", "days")

def check_type(val, expected_type, field_path):
    if expected_type == "string":
        if not isinstance(val, str):
            return f"{field_path}: expected string, got {type(val).__name__}"
    elif expected_type == "list":
        if not isinstance(val, list):
            return f"{field_path}: expected list/array, got {type(val).__name__}"
    elif expected_type == "dict":
        if not isinstance(val, dict):
            return f"{field_path}: expected dict/object, got {type(val).__name__}"
    elif expected_type == "int":
        if not isinstance(val, int) or isinstance(val, bool):
            return f"{field_path}: expected int, got {type(val).__name__}"
    return None

def validate_day_schema(day_num, data):
    errors = []

    # Root fields
    root_checks = [
        ("day", "int"),
        ("title", "string"),
        ("streams", "dict"),
        ("sem_data", "dict"),
        ("apt_data", "dict"),
        ("dsa_problems", "list"),
        ("dsa_pattern", "dict"),
        ("cs_core", "dict"),
        ("project_defense", "dict"),
        ("placement_interview", "list"),
        ("daily_revision", "dict"),
        ("daily_test", "dict"),
        ("daily_coding_task", "dict"),
        ("daily_score_model", "dict")
    ]
    for key, t in root_checks:
        if key not in data:
            errors.append(f"Missing root key '{key}'")
        else:
            err = check_type(data[key], t, key)
            if err:
                errors.append(err)

    if errors:
        return errors

    streams = data["streams"]
    stream_keys = [
        ("academic", "dict"),
        ("academic_pyqs", "list"),
        ("academic_mcqs", "list"),
        ("aptitude_lesson", "dict"),
        ("aptitude_solved", "list"),
        ("aptitude_mcqs", "list"),
        ("aptitude_practice", "list"),
        ("aptitude_timed_drill", "dict"),
        ("dsa_pattern", "dict"),
        ("coding_problems", "list"),
        ("core_cs", "dict"),
        ("project_preparation", "dict"),
        ("placement_interview", "list"),
        ("daily_revision", "dict"),
        ("mixed_test", "list"),
        ("daily_coding_task", "dict"),
        ("daily_score_model", "dict")
    ]
    for sk, st in stream_keys:
        if sk not in streams:
            errors.append(f"streams: missing key '{sk}'")
        else:
            err = check_type(streams[sk], st, f"streams.{sk}")
            if err:
                errors.append(err)

    # Validate DSA Pattern
    dsa = streams.get("dsa_pattern", {})
    if isinstance(dsa, dict):
        for field in ["pattern_name", "category", "concept", "why_it_works", "visual_explanation", "dry_run", "complexity", "edge_cases"]:
            err = check_type(dsa.get(field, ""), "string", f"streams.dsa_pattern.{field}")
            if err:
                errors.append(err)
        code = dsa.get("java_code") or dsa.get("code")
        err = check_type(code, "string", "streams.dsa_pattern.java_code")
        if err:
            errors.append(err)

    # Validate Coding Problems
    coding_probs = streams.get("coding_problems", [])
    if isinstance(coding_probs, list):
        for idx, cp in enumerate(coding_probs):
            if not isinstance(cp, dict):
                errors.append(f"streams.coding_problems[{idx}]: expected dict, got {type(cp).__name__}")
                continue
            for field in ["title", "difficulty", "statement", "approach", "time_complexity", "space_complexity"]:
                err = check_type(cp.get(field, ""), "string", f"streams.coding_problems[{idx}].{field}")
                if err:
                    errors.append(err)
            c_code = cp.get("solution_java") or cp.get("code")
            err = check_type(c_code, "string", f"streams.coding_problems[{idx}].solution_java")
            if err:
                errors.append(err)

    # Validate Coding Task
    task = streams.get("daily_coding_task", {})
    if isinstance(task, dict):
        for field in ["task_id", "title", "problem_statement", "starter_code", "solution_code"]:
            err = check_type(task.get(field, ""), "string", f"streams.daily_coding_task.{field}")
            if err:
                errors.append(err)
        err = check_type(task.get("test_cases", []), "list", "streams.daily_coding_task.test_cases")
        if err:
            errors.append(err)

    # Validate Aptitude MCQs
    apt_mcqs = streams.get("aptitude_mcqs", [])
    if isinstance(apt_mcqs, list):
        for idx, mcq in enumerate(apt_mcqs):
            if not isinstance(mcq, dict):
                errors.append(f"streams.aptitude_mcqs[{idx}]: expected dict, got {type(mcq).__name__}")
                continue
            for field in ["question", "correct_answer", "explanation"]:
                err = check_type(mcq.get(field, ""), "string", f"streams.aptitude_mcqs[{idx}].{field}")
                if err:
                    errors.append(err)
            if not (isinstance(mcq.get("options"), (dict, list))):
                errors.append(f"streams.aptitude_mcqs[{idx}].options: expected dict or list, got {type(mcq.get('options')).__name__}")

    # Validate Mixed Test MCQs
    mixed_mcqs = streams.get("mixed_test", [])
    if isinstance(mixed_mcqs, list):
        for idx, mcq in enumerate(mixed_mcqs):
            if not isinstance(mcq, dict):
                errors.append(f"streams.mixed_test[{idx}]: expected dict, got {type(mcq).__name__}")
                continue
            for field in ["question", "correct_answer", "explanation"]:
                err = check_type(mcq.get(field, ""), "string", f"streams.mixed_test[{idx}].{field}")
                if err:
                    errors.append(err)
            if not (isinstance(mcq.get("options"), (dict, list))):
                errors.append(f"streams.mixed_test[{idx}].options: expected dict or list, got {type(mcq.get('options')).__name__}")

    # Validate Revision
    rev = streams.get("daily_revision", {})
    if isinstance(rev, dict):
        for field in ["yesterday_recall", "today_recall", "formula_recall", "pyq_recall", "dsa_recall", "project_recall"]:
            if field not in rev:
                errors.append(f"streams.daily_revision: missing '{field}'")
            elif not isinstance(rev[field], (str, list, dict)):
                errors.append(f"streams.daily_revision.{field}: unexpected type {type(rev[field]).__name__}")
        err = check_type(rev.get("rapid_fire_questions", []), "list", "streams.daily_revision.rapid_fire_questions")
        if err:
            errors.append(err)

    return errors

def main():
    print("=" * 60)
    print("RECURSIVE JSON SCHEMA VALIDATOR (DAYS 01 - 30)")
    print("=" * 60)

    total_days = 30
    failed_count = 0

    for day in range(1, total_days + 1):
        filename = f"day{day:02d}.json"
        filepath = os.path.join(DAYS_DIR, filename)

        if not os.path.exists(filepath):
            print(f"DAY {day:02d} : FAIL (File not found)")
            failed_count += 1
            continue

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print(f"DAY {day:02d} : FAIL (JSON syntax error: {e})")
            failed_count += 1
            continue

        errors = validate_day_schema(day, data)
        if errors:
            print(f"DAY {day:02d} : FAIL ({len(errors)} schema errors)")
            for e in errors[:5]:
                print(f"   [x] {e}")
            if len(errors) > 5:
                print(f"   ... and {len(errors) - 5} more")
            failed_count += 1
        else:
            print(f"DAY {day:02d} : PASS")

    print("=" * 60)
    passed_count = total_days - failed_count
    print(f"Schema Validation Result: {passed_count}/{total_days} Passed")
    if failed_count > 0:
        print("[FAIL] Some days failed schema validation.")
        sys.exit(1)
    else:
        print("[SUCCESS] All 30 Day JSONs passed strict recursive schema validation!")
        sys.exit(0)

if __name__ == "__main__":
    main()
