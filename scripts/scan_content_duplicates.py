import json
import glob
import re
from collections import defaultdict

def normalize_text(text):
    if not isinstance(text, str):
        return ""
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())
    return " ".join(text.split())

def scan_duplicates():
    all_files = sorted(glob.glob("content/days/day*.json"))
    question_map = defaultdict(list)
    aptitude_map = defaultdict(list)
    mixed_map = defaultdict(list)
    rapid_fire_map = defaultdict(list)

    total_mixed = 0
    total_aptitude = 0
    total_rapid = 0

    for path in all_files:
        with open(path, "r", encoding="utf-8") as f:
            d = json.load(f)
            day = d.get("day", 0)

            # Aptitude MCQs
            apt_mcqs = d.get("streams", {}).get("aptitude_mcqs", []) or d.get("apt_data", {}).get("mcqs", [])
            for q in apt_mcqs:
                total_aptitude += 1
                q_text = normalize_text(q.get("question", ""))
                if q_text:
                    aptitude_map[q_text].append(f"Day {day}")

            # Mixed MCQs
            mixed = d.get("streams", {}).get("mixed_test", []) or d.get("daily_test", {}).get("mcqs", [])
            for q in mixed:
                total_mixed += 1
                q_text = normalize_text(q.get("question", ""))
                if q_text:
                    mixed_map[q_text].append(f"Day {day}")

            # Rapid fire revision
            rev = d.get("streams", {}).get("daily_revision", {}) or d.get("daily_revision", {})
            for key, val in rev.items():
                if isinstance(val, list):
                    for item in val:
                        total_rapid += 1
                        q_str = item if isinstance(item, str) else str(item)
                        q_norm = normalize_text(q_str)
                        if q_norm:
                            rapid_fire_map[q_norm].append(f"Day {day}:{key}")

    # Check for accidental duplicates
    accidental_mixed_dups = {k: v for k, v in mixed_map.items() if len(v) > 1 and len(set(v)) > 1}
    accidental_apt_dups = {k: v for k, v in aptitude_map.items() if len(v) > 1 and len(set(v)) > 1}

    report = {
        "total_days_audited": len(all_files),
        "total_mixed_mcqs": total_mixed,
        "total_aptitude_mcqs": total_aptitude,
        "total_rapid_fire_items": total_rapid,
        "unique_mixed_mcqs": len(mixed_map),
        "unique_aptitude_mcqs": len(aptitude_map),
        "accidental_mixed_duplicates_count": len(accidental_mixed_dups),
        "accidental_aptitude_duplicates_count": len(accidental_apt_dups),
        "mixed_duplicate_samples": [
            {"question": k[:80], "occurrences": v} for k, v in list(accidental_mixed_dups.items())[:5]
        ],
        "aptitude_duplicate_samples": [
            {"question": k[:80], "occurrences": v} for k, v in list(accidental_apt_dups.items())[:5]
        ],
        "status": "PASS" if (len(accidental_mixed_dups) == 0 and len(accidental_apt_dups) == 0) else "WARN"
    }

    import os
    os.makedirs("evidence", exist_ok=True)
    with open("evidence/content_duplication_report.json", "w", encoding="utf-8") as out:
        json.dump(report, out, indent=2)

    print("===========================================================================")
    print("CONTENT DUPLICATION AUDIT REPORT")
    print("===========================================================================")
    print(f"Total Days Audited            : {report['total_days_audited']}")
    print(f"Total Mixed MCQs Scanned      : {report['total_mixed_mcqs']} (Unique: {report['unique_mixed_mcqs']})")
    print(f"Total Aptitude MCQs Scanned   : {report['total_aptitude_mcqs']} (Unique: {report['unique_aptitude_mcqs']})")
    print(f"Accidental Mixed Duplicates   : {report['accidental_mixed_duplicates_count']}")
    print(f"Accidental Aptitude Duplicates: {report['accidental_aptitude_duplicates_count']}")
    print(f"Duplication Audit Status      : {report['status']}")
    print("Report written to evidence/content_duplication_report.json")

if __name__ == "__main__":
    scan_duplicates()
