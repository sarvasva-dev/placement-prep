import os
import sys
import json

HANDBOOK_SRC = r"D:\Projects\Placement_Master_Handbook\src"
if HANDBOOK_SRC not in sys.path:
    sys.path.insert(0, HANDBOOK_SRC)

WEB_ROOT = r"D:\Projects\Placement_Master_Handbook_Web"
SCRIPTS_DIR = os.path.join(WEB_ROOT, "scripts")
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR)

CONTENT_DIR = os.path.join(WEB_ROOT, "content")
DAYS_DIR = os.path.join(CONTENT_DIR, "days")
os.makedirs(DAYS_DIR, exist_ok=True)

import gen_days_20_24
import gen_days_25_30
import gen_cross_cutting

all_days = {}

def mock_render_day_block(doc, day_num, title, **kwargs):
    sem = kwargs.get('sem_data', {})
    if 'comparison_table' in sem and sem['comparison_table']:
        table = sem['comparison_table']
        headers = table[0]
        rows = table[1]
        sem['comparison_table'] = {'headers': headers, 'rows': rows}
    
    all_days[day_num] = {
        'day': day_num,
        'title': title,
        'sem_data': kwargs.get('sem_data', {}),
        'sgpa_target': kwargs.get('sgpa_target', {}),
        'apt_data': kwargs.get('apt_data', {}),
        'dsa_problems': kwargs.get('dsa_problems', []),
        'cs_core': kwargs.get('cs_core', {}),
        'project_defense': kwargs.get('project_defense', {}),
        'daily_test': kwargs.get('daily_test', {})
    }

import part13_textbook_days
part13_textbook_days.render_day_block = mock_render_day_block

print("==================================================")
print("1. INGESTING DAYS 1 TO 18 FROM VERIFIED CURRICULUM")
print("==================================================")
for i in range(1, 19):
    mod = __import__(f"curriculum.day{i:02d}", fromlist=['render'])
    mod.render(None)
    print(f"  [+] Day {i:02d}: {all_days[i]['title']}")

print("\n==================================================")
print("2. INGESTING DAY 19")
print("==================================================")
import populate_content
all_days[19] = populate_content.captured_days[19]
print(f"  [+] Day 19: {all_days[19]['title']}")

print("\n==================================================")
print("3. INGESTING DAYS 20 TO 24")
print("==================================================")
days_20_24 = gen_days_20_24.get_days_20_to_24()
for d, data in days_20_24.items():
    all_days[d] = data
    print(f"  [+] Day {d:02d}: {data['title']}")

print("\n==================================================")
print("4. INGESTING DAYS 25 TO 30")
print("==================================================")
days_25_30 = gen_days_25_30.get_days_25_to_30()
for d, data in days_25_30.items():
    all_days[d] = data
    print(f"  [+] Day {d:02d}: {data['title']}")

print("\n==================================================")
print("5. SAVING ALL 30 DAYS TO /content/days/dayXX.json")
print("==================================================")
days_index = []
all_pyqs = []
all_aptitude = []
all_coding = []
all_core_cs = []

for day_num in range(1, 31):
    day_data = all_days[day_num]
    day_file = os.path.join(DAYS_DIR, f"day{day_num:02d}.json")
    with open(day_file, "w", encoding="utf-8") as f:
        json.dump(day_data, f, indent=2)
    
    # Add to lightweight timeline index
    days_index.append({
        "day": day_num,
        "title": day_data["title"],
        "subject": day_data.get("sem_data", {}).get("subject", ""),
        "topic": day_data.get("sem_data", {}).get("topic", ""),
        "aptitude": day_data.get("apt_data", {}).get("topic", ""),
        "dsa": [p.get("title", "") for p in day_data.get("dsa_problems", [])],
        "core_cs": day_data.get("cs_core", {}).get("topic", ""),
        "project": day_data.get("project_defense", {}).get("project_name", "")
    })

    # Harvest PYQs for global PYQ search
    sem = day_data.get("sem_data", {})
    if "pyq_question" in sem and sem["pyq_question"]:
        all_pyqs.append({
            "day": day_num,
            "subject": sem.get("subject", ""),
            "topic": sem.get("topic", ""),
            "pyq_year": sem.get("pyq_year", ""),
            "pyq_freq": sem.get("pyq_freq", ""),
            "question": sem.get("pyq_question", ""),
            "rubric": sem.get("pyq_rubric", ""),
            "model_answer_paragraphs": sem.get("model_answer_paragraphs", [])
        })

    # Harvest Aptitude for global practice
    apt = day_data.get("apt_data", {})
    if "topic" in apt:
        all_aptitude.append({
            "day": day_num,
            "topic": apt.get("topic", ""),
            "formulas": apt.get("formulas", ""),
            "shortcut": apt.get("shortcut", ""),
            "tutorial": apt.get("tutorial", []),
            "recognition": apt.get("recognition", ""),
            "tier1_problem": apt.get("p1_q") or apt.get("tier1_problem", ""),
            "tier1_solution": apt.get("p1_s") or apt.get("tier1_solution", ""),
            "tier2_problem": apt.get("p2_q") or apt.get("tier2_problem", ""),
            "tier2_solution": apt.get("p2_s") or apt.get("tier2_solution", ""),
            "tier3_problem": apt.get("p3_q") or apt.get("tier3_problem", ""),
            "tier3_solution": apt.get("p3_s") or apt.get("tier3_solution", ""),
            "tier3_source": apt.get("p3_source", ""),
            "tier4_problem": apt.get("p4_q") or apt.get("tier4_problem", ""),
            "tier4_solution": apt.get("p4_s") or apt.get("tier4_solution", ""),
            "timed_set": apt.get("timed_set", []) or apt.get("speed_drills", [])
        })

    # Harvest DSA
    for p in day_data.get("dsa_problems", []):
        all_coding.append({
            "day": day_num,
            **p
        })

    # Harvest Core CS
    cs = day_data.get("cs_core", {})
    if "topic" in cs:
        all_core_cs.append({
            "day": day_num,
            **cs
        })

# Save days index
with open(os.path.join(CONTENT_DIR, "days_index.json"), "w", encoding="utf-8") as f:
    json.dump(days_index, f, indent=2)

# Save consolidated PYQs
os.makedirs(os.path.join(CONTENT_DIR, "pyqs"), exist_ok=True)
with open(os.path.join(CONTENT_DIR, "pyqs", "all_pyqs.json"), "w", encoding="utf-8") as f:
    json.dump(all_pyqs, f, indent=2)

# Save consolidated Aptitude
os.makedirs(os.path.join(CONTENT_DIR, "aptitude"), exist_ok=True)
with open(os.path.join(CONTENT_DIR, "aptitude", "all_aptitude.json"), "w", encoding="utf-8") as f:
    json.dump(all_aptitude, f, indent=2)

# Save consolidated Coding
os.makedirs(os.path.join(CONTENT_DIR, "coding"), exist_ok=True)
with open(os.path.join(CONTENT_DIR, "coding", "all_coding.json"), "w", encoding="utf-8") as f:
    json.dump(all_coding, f, indent=2)

# Save consolidated Core CS
os.makedirs(os.path.join(CONTENT_DIR, "core_cs"), exist_ok=True)
with open(os.path.join(CONTENT_DIR, "core_cs", "all_core_cs.json"), "w", encoding="utf-8") as f:
    json.dump(all_core_cs, f, indent=2)

print("\n==================================================")
print("6. GENERATING CROSS-CUTTING CURRICULUM ASSETS")
print("==================================================")
gen_cross_cutting.generate_cross_cutting(CONTENT_DIR)

print("\n==================================================")
print("SUCCESS: ALL CONTENT LAYER JSON FILES FULLY GENERATED!")
print("==================================================")
