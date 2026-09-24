#!/usr/bin/env python3
"""
validate_learning_semantics.py
==============================
Performs semantic checks on learning content to detect logical mismatch,
copy-paste errors, and incorrect edge cases or complexities.
"""

import json
import os
import sys

DAYS_DIR = os.path.join(os.path.dirname(__file__), '..', 'content', 'days')
EVIDENCE_DIR = os.path.join(os.path.dirname(__file__), '..', 'evidence')

def check_learning_semantics():
    issues = []
    
    for day_num in range(1, 31):
        fpath = os.path.join(DAYS_DIR, f'day{day_num:02d}.json')
        if not os.path.exists(fpath):
            continue
            
        with open(fpath, 'r', encoding='utf-8') as f:
            d = json.load(f)
            
        # 1. Check Container With Most Water edge cases
        dsa = d.get('streams', {}).get('dsa_pattern', {})
        prob_title = str(dsa.get('problem', {}).get('title', '')).lower()
        
        if 'container' in prob_title and 'water' in prob_title:
            edge_cases = str(dsa.get('edge_cases', '')).lower()
            if 'duplicate' in edge_cases and 'target' in edge_cases:
                issues.append({
                    'day': day_num,
                    'type': 'WRONG_EDGE_CASE',
                    'message': 'Container With Most Water should not have "duplicates summing to target" as an edge case. This belongs to Two Sum.'
                })
                
        # 2. Basic semantic consistency: Pattern name vs Complexity
        pattern_name = str(dsa.get('pattern_name', '')).lower()
        complexity = str(dsa.get('complexity', '')).lower()
        
        if 'binary search' in pattern_name and 'log' not in complexity and 'complexity' in complexity:
             issues.append({
                 'day': day_num,
                 'type': 'WRONG_COMPLEXITY',
                 'message': 'Binary Search pattern usually has O(log N) time complexity. Not found.'
             })
             
        if 'two pointer' in pattern_name and 'o(n^2)' in complexity:
             issues.append({
                 'day': day_num,
                 'type': 'WRONG_COMPLEXITY',
                 'message': 'Two pointers pattern usually has O(N) time complexity, found O(N^2).'
             })
             
        # 3. Check dry run exists and has content
        dry_run = str(dsa.get('dry_run', dsa.get('dry_run_steps', ''))).lower()
        if dsa and not dry_run and len(str(dsa)) > 20:
             issues.append({
                 'day': day_num,
                 'type': 'MISSING_DRY_RUN',
                 'message': 'DSA Pattern has no dry run or dry run steps.'
             })
             
        # 4. Check for Copied Aptitude
        # If aptitude questions repeat EXACTLY across days
        # (This is handled by our other script, but we can do a quick check here if needed)
        
    return issues

if __name__ == '__main__':
    print("=" * 70)
    print("LEARNING SEMANTICS VALIDATION")
    print("=" * 70)
    issues = check_learning_semantics()
    
    if not issues:
        print("All semantic checks PASSED.")
    else:
        for issue in issues:
            print(f"Day {issue['day']:02d} [{issue['type']}]: {issue['message']}")
            
    # Write report
    os.makedirs(EVIDENCE_DIR, exist_ok=True)
    with open(os.path.join(EVIDENCE_DIR, 'learning_semantics_audit.json'), 'w', encoding='utf-8') as f:
        json.dump({'total_issues': len(issues), 'issues': issues}, f, indent=2)
        
    sys.exit(len(issues))
