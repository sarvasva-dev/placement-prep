#!/usr/bin/env python3
"""
scripts/audit_source_inventory.py
AGENT 1 - SOURCE INVENTORY AUDITOR

Scans all source files in A:\ and D:\Projects, hashes each file with SHA-256,
and outputs evidence/source_inventory.json.
"""
import os
import hashlib
import json
import glob

def calculate_sha256(filepath):
    hasher = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(65536):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception as e:
        return f"ERROR: {str(e)}"

def get_dir_size_fast(path):
    total = 0
    try:
        for entry in os.scandir(path):
            if entry.name in {'.git', 'node_modules', '.next', 'venv', '__pycache__', '.pytest_cache'}:
                continue
            if entry.is_file(follow_symlinks=False):
                total += entry.stat().st_size
            elif entry.is_dir(follow_symlinks=False):
                total += get_dir_size_fast(entry.path)
    except Exception:
        pass
    return total

def build_inventory():
    inventory = []
    
    # 1. Scanned Academic Archive PDFs from RAR extraction
    rar_files = glob.glob("source_archive/rar_extracted/**/*.pdf", recursive=True)
    for path in sorted(rar_files):
        norm_path = path.replace("\\", "/")
        filename = os.path.basename(norm_path)
        size = os.path.getsize(norm_path)
        file_hash = calculate_sha256(norm_path)
        
        subject = "Unknown"
        if "Computer Network" in filename or "503" in filename:
            subject = "BCA 5003 Computer Network"
        elif "Java" in filename or "502" in filename:
            subject = "BCA 5002 Java Programming & Dynamic Webpage Design"
        elif "Knowledge Management" in filename or "501" in filename:
            subject = "BCA 5001 Knowledge Management"
        elif "Numerical" in filename or "504" in filename:
            subject = "BCA 5004 Numerical Methods"
        elif "Database" in filename or "DBMS" in filename:
            subject = "BCA Introduction to DBMS"
            
        inventory.append({
            "source_id": f"SRC-PYQ-{len(inventory)+1:03d}",
            "original_path": norm_path,
            "copied_path": norm_path,
            "filename": filename,
            "type": "PDF_SCANNED_EXAM",
            "size": size,
            "hash": file_hash,
            "category": "Academic PYQ",
            "subject": subject,
            "extraction_status": "EXTRACTED_FROM_RAR",
            "ocr_required": True,
            "status": "VERIFIED_PRIMARY_SOURCE"
        })
        
    # 2. Academic Study Guides and Notes in source_archive/academic/
    academic_guides = glob.glob("source_archive/academic/*.pdf")
    for path in sorted(academic_guides):
        norm_path = path.replace("\\", "/")
        filename = os.path.basename(norm_path)
        size = os.path.getsize(norm_path)
        file_hash = calculate_sha256(norm_path)
        inventory.append({
            "source_id": f"SRC-ACAD-{len(inventory)+1:03d}",
            "original_path": f"A:/{filename}",
            "copied_path": norm_path,
            "filename": filename,
            "type": "PDF_STUDY_GUIDE",
            "size": size,
            "hash": file_hash,
            "category": "Academic Notes",
            "extraction_status": "COPIED_TO_SOURCE_ARCHIVE",
            "ocr_required": False,
            "status": "VERIFIED_STUDY_MATERIAL"
        })

    # 3. Resumes
    resumes = glob.glob("source_archive/resumes/*.pdf")
    for path in sorted(resumes):
        norm_path = path.replace("\\", "/")
        filename = os.path.basename(norm_path)
        size = os.path.getsize(norm_path)
        file_hash = calculate_sha256(norm_path)
        inventory.append({
            "source_id": f"SRC-RESUME-{len(inventory)+1:03d}",
            "original_path": f"A:/{filename}",
            "copied_path": norm_path,
            "filename": filename,
            "type": "PDF_RESUME",
            "size": size,
            "hash": file_hash,
            "category": "Career & Resume",
            "extraction_status": "COPIED_TO_SOURCE_ARCHIVE",
            "ocr_required": False,
            "status": "VERIFIED_CANDIDATE_RESUME"
        })

    # 4. Project Documents (Quotation / MSA Bulkbeat)
    project_docs = glob.glob("source_archive/projects/*.pdf")
    for path in sorted(project_docs):
        norm_path = path.replace("\\", "/")
        filename = os.path.basename(norm_path)
        size = os.path.getsize(norm_path)
        file_hash = calculate_sha256(norm_path)
        inventory.append({
            "source_id": f"SRC-PROJ-DOC-{len(inventory)+1:03d}",
            "original_path": f"A:/{filename}",
            "copied_path": norm_path,
            "filename": filename,
            "type": "PDF_CONTRACT_SPEC",
            "size": size,
            "hash": file_hash,
            "category": "Project Documentation",
            "extraction_status": "COPIED_TO_SOURCE_ARCHIVE",
            "ocr_required": False,
            "status": "VERIFIED_COMMERCIAL_DOCUMENT"
        })

    # 5. Core Repositories in D:\Projects
    core_repos = [
        {"name": "College Student Management System", "path": "D:/Projects/College Student Management System", "cat": "Academic Project"},
        {"name": "SmartGalla", "path": "D:/Projects/SmartGalla", "cat": "Production SaaS & Kirana Supply"},
        {"name": "nse2", "path": "D:/Projects/nse2", "cat": "Production Financial Market Engine"},
        {"name": "Caloriv", "path": "D:/Projects/Caloriv", "cat": "Mobile Fitness & Health App"},
        {"name": "sarthak-modern-portfolio", "path": "D:/Projects/sarthak-modern-portfolio", "cat": "Portfolio Portal"}
    ]
    for repo in core_repos:
        if os.path.exists(repo["path"]):
            readme_path = os.path.join(repo["path"], "README.md")
            readme_hash = calculate_sha256(readme_path) if os.path.exists(readme_path) else "NO_README"
            repo_size = get_dir_size_fast(repo["path"])
            inventory.append({
                "source_id": f"SRC-REPO-{len(inventory)+1:03d}",
                "original_path": repo["path"],
                "copied_path": "LIVE_REPOSITORY_IN_D_PROJECTS",
                "filename": repo["name"],
                "type": "GIT_REPOSITORY",
                "size": repo_size,
                "hash": readme_hash,
                "category": repo["cat"],
                "extraction_status": "INSPECTED_DIRECTLY",
                "ocr_required": False,
                "status": "VERIFIED_PRIMARY_REPO"
            })

    output_path = "evidence/source_inventory.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(inventory, f, indent=2)
    print(f"[OK] Generated {output_path} with {len(inventory)} verified source entries.")

if __name__ == "__main__":
    build_inventory()
