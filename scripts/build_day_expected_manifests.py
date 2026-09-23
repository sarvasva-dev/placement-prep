#!/usr/bin/env python3
"""
scripts/build_day_expected_manifests.py
Generates content/days/dayXX_expected.json for all 30 days.
Defines the authoritative expected semantic identity for each day to prevent
pages from rendering generic content from the wrong day.
"""

import os
import json
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DAYS_DIR = os.path.join(BASE_DIR, "content", "days")

def build_manifests():
    index_file = os.path.join(BASE_DIR, "content", "days_index.json")
    with open(index_file, "r", encoding="utf-8") as f:
        days_index = json.load(f)

    for entry in days_index:
        day_num = entry["day"]
        day_str = f"{day_num:02d}"

        # Load day content to get exact canonical strings
        day_content_file = os.path.join(DAYS_DIR, f"day{day_str}.json")
        with open(day_content_file, "r", encoding="utf-8") as df:
            d = json.load(df)

        streams = d.get("streams", {})
        acad = streams.get("academic", {})
        apt = streams.get("aptitude_lesson", {})
        dsa = streams.get("dsa_pattern", {})
        core = streams.get("core_cs", {})
        proj = streams.get("project_preparation", {})

        manifest = {
            "day": day_num,
            "title": d.get("title", ""),
            "academic_subject": acad.get("subject_name", ""),
            "academic_topic": acad.get("topic", ""),
            "aptitude_topic": apt.get("topic", ""),
            "dsa_pattern": dsa.get("pattern_name", ""),
            "core_cs_topic": core.get("topic", ""),
            "project_name": proj.get("project_name", "")
        }

        out_path = os.path.join(DAYS_DIR, f"day{day_str}_expected.json")
        with open(out_path, "w", encoding="utf-8") as out_f:
            json.dump(manifest, out_f, indent=2, ensure_ascii=False)

    print(f"[+] Successfully generated 30 daily expected identity manifests in {DAYS_DIR}!")

if __name__ == "__main__":
    build_manifests()
