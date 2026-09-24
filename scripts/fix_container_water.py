import json
import os

day1_file = 'content/days/day01.json'
with open(day1_file, 'r', encoding='utf-8') as f:
    d = json.load(f)

def clean_water_item(item):
    if not isinstance(item, dict):
        return
    if 'Container With Most Water' in item.get('title', '') or 'Container With Most Water' in item.get('problem', ''):
        item['approach'] = (
            "1. Two Pointers (Opposite Direction) placing left at index 0 and right at index n-1.\n"
            "2. Handle edge cases: n = 2, minimum and maximum heights, zero-height lines, "
            "equal heights, all equal heights, pointer reaches boundary, large area values.\n"
            "3. Compute current area = min(height[left], height[right]) * (right - left). "
            "Move the pointer at the shorter line inward to seek a taller line."
        )
        item['solution_approach'] = item['approach']
        item['intuition'] = item['approach']
        item['edge_cases'] = (
            "n = 2, minimum and maximum heights, zero-height lines, equal heights, "
            "all equal heights, pointer reaches boundary, large area values."
        )

# Fix in streams.coding_problems
if 'streams' in d and 'coding_problems' in d['streams']:
    for p in d['streams']['coding_problems']:
        clean_water_item(p)

# Recursively fix any dict with title Container With Most Water
def walk_and_fix(obj):
    if isinstance(obj, dict):
        clean_water_item(obj)
        for v in obj.values():
            walk_and_fix(v)
    elif isinstance(obj, list):
        for item in obj:
            walk_and_fix(item)

walk_and_fix(d)

with open(day1_file, 'w', encoding='utf-8') as f:
    json.dump(d, f, indent=2)

print("Updated day01.json cleanly")

# Also fix content/coding/all_coding.json
all_coding_file = 'content/coding/all_coding.json'
if os.path.exists(all_coding_file):
    with open(all_coding_file, 'r', encoding='utf-8') as f:
        ac = json.load(f)
    walk_and_fix(ac)
    with open(all_coding_file, 'w', encoding='utf-8') as f:
        json.dump(ac, f, indent=2)
    print("Updated all_coding.json cleanly")
