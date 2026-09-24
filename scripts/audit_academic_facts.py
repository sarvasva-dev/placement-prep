#!/usr/bin/env python3
"""
audit_academic_facts.py
=======================
Source-verified content fact audit for all 30 days.
Flags unsafe absolute statements, wrong technical facts, and missing critical content.

Run: python scripts/audit_academic_facts.py
"""

import json
import os
import sys
import re
from datetime import datetime

DAYS_DIR = os.path.join(os.path.dirname(__file__), '..', 'content', 'days')
EVIDENCE_DIR = os.path.join(os.path.dirname(__file__), '..', 'evidence')

# ── Unsafe absolute phrases (CONTEXT-AWARE) ───────────────────────────────────
# Phrases that are dangerous if used as blanket claims (not in MCQ option contexts)
UNSAFE_ABSOLUTES = [
    ("immune to eavesdropping", "Fiber is highly resistant, not immune. Physical tapping exists."),
    ("error doubles in accuracy", "Newton-Raphson quadratic convergence means DIGITS double, not errors."),
    ("100% secure", "No system is 100% secure."),
    ("cannot be hacked", "No absolute claim of unhackability."),
    ("impossible to crack", "With sufficient resources, most encryption can be broken."),
    ("never fails", "All methods have failure conditions."),
]

# ── Java Thread States (official Java enum constants) ─────────────────────────
JAVA_THREAD_STATES = ["NEW", "RUNNABLE", "BLOCKED", "WAITING", "TIMED_WAITING", "TERMINATED"]

# ── Subject day mapping ───────────────────────────────────────────────────────
JAVA_DAYS = {6: "Thread Lifecycle"}  # Only Day 6 is specifically about thread lifecycle
FIBER_DAYS = {9: "Transmission Media (Fiber Optic Cable)"}
NR_DAYS = {10: "Newton-Raphson Method"}

# ── Known correct facts ───────────────────────────────────────────────────────
KNOWN_CORRECT = {
    "newton_raphson_convergence": {
        "correct": "quadratic convergence: number of correct decimal digits roughly doubles per iteration",
        "wrong_patterns": ["error doubles in accuracy", "error doubles each step", "errors double"],
        "days": [10, 15, 19, 23, 27]
    },
    "fiber_optic_security": {
        "correct": "highly resistant to eavesdropping (not immune — physical tapping is possible)",
        "wrong_patterns": ["immune to eavesdropping"],
        "days": [9, 13, 22]  # Days covering transmission media / network security
    },
    "thread_states": {
        "correct": "6 official Java Thread.State enum values: NEW, RUNNABLE, BLOCKED, WAITING, TIMED_WAITING, TERMINATED",
        "days": [6]  # Only validate on the specific Thread Lifecycle day
    }
}


def load_day(day_num):
    path = os.path.join(DAYS_DIR, f'day{day_num:02d}.json')
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f), f.name


def check_unsafe_absolutes(content_str, day_num):
    """Check for absolute statements OUTSIDE of MCQ option contexts."""
    issues = []
    content_lower = content_str.lower()
    
    for phrase, reason in UNSAFE_ABSOLUTES:
        idx = 0
        while True:
            pos = content_lower.find(phrase.lower(), idx)
            if pos < 0:
                break
            # Get surrounding context
            start = max(0, pos - 150)
            end = min(len(content_str), pos + 150)
            context = content_str[start:end]
            
            # Determine if this is in an MCQ option (acceptable) or in explanatory content (problematic)
            # MCQ options are inside "options" arrays or as one of A/B/C/D choices
            is_in_mcq_option = (
                '"options"' in context or
                # Parameterized queries being immune to SQL injection IS correct
                'parameterized' in context.lower() or
                'sql injection' in context.lower() or
                # Belady's anomaly immunity for LRU is correct
                "belady" in context.lower()
            )
            
            if not is_in_mcq_option:
                issues.append({
                    "type": "UNSAFE_ABSOLUTE",
                    "phrase": phrase,
                    "reason": reason,
                    "context": context.strip().replace('\n', ' ')[:200],
                    "severity": "HIGH"
                })
            
            idx = pos + 1
    
    return issues


def check_thread_states(day_data, day_num):
    """For Day 6 (Thread Lifecycle), verify all 6 official Java thread states are named."""
    if day_num != 6:
        return []
    
    issues = []
    content_str = json.dumps(day_data)
    
    for state in JAVA_THREAD_STATES:
        # Check for exact state name (uppercase enum style)
        if state not in content_str:
            issues.append({
                "type": "MISSING_THREAD_STATE",
                "phrase": state,
                "reason": f"Java Thread.State.{state} must appear in Day 6 (Thread Lifecycle) content",
                "severity": "HIGH"
            })
    
    # Also check for WRONG convergence of state names
    # "Dead" is wrong — correct term is "TERMINATED"
    content_lower = content_str.lower()
    if '"dead"' in content_lower or "'dead'" in content_lower:
        # Check if context is about threads (not other meanings)
        idx = content_lower.find('dead')
        context = content_str[max(0, idx-50):idx+80]
        if 'thread' in context.lower() or 'state' in context.lower():
            issues.append({
                "type": "WRONG_THREAD_STATE_NAME",
                "phrase": "Dead",
                "reason": "Java thread state is 'TERMINATED' not 'Dead'. 'Dead' is an older informal term.",
                "severity": "MEDIUM"
            })
    
    return issues


def check_nr_convergence(day_data, day_num):
    """For Day 10 (Newton-Raphson), verify convergence is described correctly."""
    if day_num not in [10]:
        return []
    
    issues = []
    content_str = json.dumps(day_data)
    content_lower = content_str.lower()
    
    # Wrong: "error doubles"
    wrong_phrases = ["error doubles in accuracy", "error doubles each step", "errors double"]
    for phrase in wrong_phrases:
        if phrase in content_lower:
            idx = content_lower.find(phrase)
            context = content_str[max(0, idx-100):idx+150].replace('\n', ' ')
            issues.append({
                "type": "WRONG_NR_CONVERGENCE",
                "phrase": phrase,
                "reason": "WRONG: Newton-Raphson quadratic convergence means 'correct decimal digits roughly double per iteration', not that 'error doubles'. Error SQUARES (reduces dramatically), digits double.",
                "context": context.strip()[:200],
                "severity": "HIGH"
            })
    
    return issues


def check_fiber_immunity(day_data, day_num):
    """For fiber-related days, check the fiber eavesdropping claim."""
    if day_num not in [9]:
        return []
    
    issues = []
    content_str = json.dumps(day_data)
    content_lower = content_str.lower()
    
    if 'immune to eavesdropping' in content_lower:
        idx = content_lower.find('immune to eavesdropping')
        context = content_str[max(0, idx-100):idx+150].replace('\n', ' ')
        
        # Only flag if not inside an MCQ where it's listed as wrong answer
        if 'options' not in context and 'correct_answer' not in context:
            issues.append({
                "type": "WRONG_FIBER_CLAIM",
                "phrase": "immune to eavesdropping",
                "reason": "WRONG: Fiber is highly resistant to eavesdropping (physical tapping is difficult but not impossible). Use 'highly resistant' not 'immune'.",
                "context": context.strip()[:200],
                "severity": "HIGH"
            })
    
    return issues


def run_audit():
    all_results = {}
    total_issues = 0
    
    print("=" * 70)
    print("ACADEMIC CONTENT FACT AUDIT")
    print(f"Time: {datetime.now().isoformat()}")
    print("=" * 70)
    
    for day_num in range(1, 31):
        day_data, path = load_day(day_num)
        content_str = json.dumps(day_data)
        
        issues = []
        issues += check_unsafe_absolutes(content_str, day_num)
        issues += check_thread_states(day_data, day_num)
        issues += check_nr_convergence(day_data, day_num)
        issues += check_fiber_immunity(day_data, day_num)
        
        high_issues = [i for i in issues if i.get('severity') == 'HIGH']
        med_issues = [i for i in issues if i.get('severity') == 'MEDIUM']
        
        status = "PASS" if not high_issues else "FAIL"
        
        all_results[f'day{day_num:02d}'] = {
            "status": status,
            "high_severity": len(high_issues),
            "medium_severity": len(med_issues),
            "issues": issues
        }
        
        if issues:
            print(f"\nDay {day_num:02d}: {status} — {len(high_issues)} HIGH, {len(med_issues)} MEDIUM")
            for issue in issues:
                sev = issue.get('severity', 'MEDIUM')
                print(f"  [{sev}] {issue['type']}: {issue['phrase']!r}")
                print(f"         Reason: {issue['reason']}")
                if 'context' in issue:
                    print(f"         Context: ...{issue['context'][:100]}...")
        else:
            print(f"Day {day_num:02d}: PASS")
        
        total_issues += len(high_issues)
    
    print("\n" + "=" * 70)
    print(f"AUDIT COMPLETE — {total_issues} HIGH-severity issues found")
    print("=" * 70)
    
    # Write evidence
    os.makedirs(EVIDENCE_DIR, exist_ok=True)
    evidence_path = os.path.join(EVIDENCE_DIR, 'academic_fact_audit.json')
    with open(evidence_path, 'w', encoding='utf-8') as f:
        json.dump({
            "generated_at": datetime.now().isoformat(),
            "total_high_severity": total_issues,
            "days": all_results
        }, f, indent=2, ensure_ascii=False)
    
    print(f"\nEvidence written to: {evidence_path}")
    return total_issues


if __name__ == '__main__':
    sys.exit(0 if run_audit() == 0 else 1)
