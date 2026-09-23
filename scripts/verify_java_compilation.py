#!/usr/bin/env python3
"""
Java Compilation Verification Suite (Parallel Isolated Compilation)
Extracts all Java DSA and coding problem solutions across:
1. content/coding/all_coding.json (60 problems)
2. content/days/day01.json through day30.json (dsa_pattern, coding_problems, daily_coding_task)
Compiles each using `javac` (version 25.0.1) in isolated subdirectories with standard LeetCode data structures (ListNode, TreeNode).
"""

import os
import sys
import json
import re
import tempfile
import subprocess
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

COMMON_DATA_STRUCTURES = """
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
"""

def prepare_java_file(raw_code: str, target_dir: Path):
    code = raw_code.strip()
    
    # Check if there is a public class name
    pub_match = re.search(r'public\s+class\s+(\w+)', code)
    if pub_match:
        main_class_name = pub_match.group(1)
    else:
        # Check if there is any class name
        class_match = re.search(r'class\s+(\w+)', code)
        if class_match:
            main_class_name = class_match.group(1)
        else:
            main_class_name = "Solution"
            code = f"public class Solution {{\n{code}\n}}"
            
    header = """import java.util.*;
import java.io.*;

"""
    extra_ds = ""
    if "class ListNode" not in code:
        extra_ds += """
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}
"""
    if "class TreeNode" not in code:
        extra_ds += """
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
"""
    full_source = header + code + "\n" + extra_ds
    file_path = target_dir / f"{main_class_name}.java"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(full_source)
    return file_path

def compile_snippet(args):
    idx, src_name, raw_code, tmp_dir = args
    snippet_dir = tmp_dir / f"snip_{idx:04d}"
    snippet_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        java_file = prepare_java_file(raw_code, snippet_dir)
        res = subprocess.run(
            ["javac", "-encoding", "UTF-8", str(java_file.name)],
            cwd=str(snippet_dir),
            capture_output=True,
            text=True
        )
        if res.returncode == 0:
            return (True, src_name, None)
        else:
            return (False, src_name, res.stderr.strip()[:300])
    except Exception as e:
        return (False, src_name, str(e))

def main():
    base_dir = Path(__file__).resolve().parent.parent
    coding_file = base_dir / "content" / "coding" / "all_coding.json"
    days_dir = base_dir / "content" / "days"
    
    print("=" * 60)
    print("JAVA CODE COMPILATION VERIFICATION SUITE")
    print("=" * 60)
    
    try:
        ver = subprocess.run(["javac", "-version"], capture_output=True, text=True, check=True)
        print(f"Compiler detected: {ver.stdout.strip() or ver.stderr.strip()}")
    except Exception as e:
        print(f"FATAL: javac compiler not found: {e}")
        sys.exit(1)
        
    snippets_to_test = [] # (source_name, code_str)
    
    # 1. Load from all_coding.json
    if coding_file.exists():
        with open(coding_file, "r", encoding="utf-8") as f:
            all_coding = json.load(f)
            for idx, item in enumerate(all_coding):
                code = item.get("java_code") or item.get("code") or item.get("solution") or ""
                if code.strip():
                    src_id = f"AllCoding_Day{item.get('day', 0)}_P{idx+1}_{item.get('problem_id', 'prob')}"
                    snippets_to_test.append((src_id, code))
                    
    # 2. Load from each dayXX.json
    for day_num in range(1, 31):
        day_path = days_dir / f"day{day_num:02d}.json"
        if not day_path.exists():
            continue
        with open(day_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            streams = data.get("streams", {})
            
            # DSA pattern
            dsa = streams.get("dsa_pattern", {})
            dsa_code = dsa.get("java_code") or dsa.get("java_solution") or dsa.get("code") or ""
            if dsa_code.strip():
                snippets_to_test.append((f"Day{day_num:02d}_DSAPattern", dsa_code))
                
            # Coding problems
            coding_probs = streams.get("coding_problems", [])
            for c_idx, cp in enumerate(coding_probs):
                c_code = cp.get("java_solution") or cp.get("java_code") or cp.get("code") or ""
                if c_code.strip():
                    snippets_to_test.append((f"Day{day_num:02d}_CodingProb{c_idx+1}", c_code))
                    
            # Practical coding task
            task = streams.get("daily_coding_task", {})
            task_sol = task.get("java_solution_code") or task.get("solution_code") or ""
            if task_sol.strip():
                snippets_to_test.append((f"Day{day_num:02d}_DailyTaskSol", task_sol))

    print(f"Discovered {len(snippets_to_test)} Java code snippets across curriculum.")
    print("Compiling in parallel with isolated namespaces...")
    
    passed_count = 0
    failed_count = 0
    failures = []
    
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        tasks = [
            (idx, src_name, code, tmp_path)
            for idx, (src_name, code) in enumerate(snippets_to_test)
        ]
        
        with ThreadPoolExecutor(max_workers=8) as executor:
            results = list(executor.map(compile_snippet, tasks))
            
        for success, src_name, err in results:
            if success:
                passed_count += 1
            else:
                failed_count += 1
                failures.append({"name": src_name, "error": err})
                print(f"  [FAIL] {src_name}")
                print(f"         {err[:150]}")

    print("\n" + "=" * 60)
    print("JAVA COMPILATION RESULTS SUMMARY")
    print("=" * 60)
    print(f"Total Snippets Checked: {len(snippets_to_test)}")
    print(f"Passed Compilation:     {passed_count} ({passed_count/len(snippets_to_test)*100:.1f}%)")
    print(f"Failed Compilation:     {failed_count}")
    
    report_path = base_dir / "evidence" / "java_compilation_report.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as rf:
        json.dump({
            "total_snippets": len(snippets_to_test),
            "passed": passed_count,
            "failed": failed_count,
            "failures": failures
        }, rf, indent=2)
    print(f"Saved compilation report to {report_path}")

    if failed_count > 0:
        print("\nWARNING: Some snippets failed javac compilation.")
        sys.exit(1)
    else:
        print("\nALL JAVA CODE SNIPPETS COMPILED SUCCESSFULLY (0 ERRORS)!")
        sys.exit(0)

if __name__ == "__main__":
    main()
