#!/usr/bin/env python3
"""
scripts/audit_github_remotes.py
AGENT 4 - GITHUB AUDITOR

Checks git remotes, commit history, and branches across D:\Projects repositories.
Outputs evidence/github_evidence.json.
"""
import os
import subprocess
import json

def get_git_info(repo_path):
    if not os.path.exists(os.path.join(repo_path, ".git")):
        return None
    
    info = {
        "local_path": repo_path.replace("\\", "/"),
        "repo_name": os.path.basename(repo_path),
        "remotes": {},
        "current_branch": None,
        "latest_commit": None,
        "commit_date": None,
        "commit_message": None
    }
    
    try:
        # Remotes
        res = subprocess.run(["git", "-C", repo_path, "remote", "-v"], capture_output=True, text=True, timeout=5)
        for line in res.stdout.strip().split("\n"):
            if line:
                parts = line.split()
                if len(parts) >= 2:
                    info["remotes"][parts[0]] = parts[1]
                    
        # Branch
        res = subprocess.run(["git", "-C", repo_path, "branch", "--show-current"], capture_output=True, text=True, timeout=5)
        info["current_branch"] = res.stdout.strip()
        
        # Latest Commit
        res = subprocess.run(["git", "-C", repo_path, "log", "-1", "--format=%H|%cd|%s"], capture_output=True, text=True, timeout=5)
        if res.stdout.strip():
            parts = res.stdout.strip().split("|", 2)
            if len(parts) == 3:
                info["latest_commit"] = parts[0]
                info["commit_date"] = parts[1]
                info["commit_message"] = parts[2]
    except Exception as e:
        info["error"] = str(e)
        
    return info

def audit_all():
    base_dir = "D:/Projects"
    github_evidence = []
    
    target_projects = [
        "College Student Management System",
        "SmartGalla",
        "nse2",
        "Caloriv",
        "sarthak-modern-portfolio",
        "portfolio-v2",
        "TestPlatform",
        "Tender automation",
        "Democracy-Flow",
        "Code  for nation"
    ]
    
    for proj in target_projects:
        full_path = os.path.join(base_dir, proj)
        if os.path.exists(full_path):
            info = get_git_info(full_path)
            if info:
                github_evidence.append(info)
                
    output_path = "evidence/github_evidence.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(github_evidence, f, indent=2)
    print(f"[OK] Generated {output_path} with {len(github_evidence)} repository records.")

if __name__ == "__main__":
    audit_all()
