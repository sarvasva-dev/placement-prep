import os
import shutil
import hashlib
import json

A_DRIVE = "A:\\"
WEB_ROOT = r"D:\Projects\Placement_Master_Handbook_Web"
ARCHIVE_ROOT = os.path.join(WEB_ROOT, "source_archive")

ACADEMIC_DIR = os.path.join(ARCHIVE_ROOT, "academic")
PROJECTS_DIR = os.path.join(ARCHIVE_ROOT, "projects")
RESUMES_DIR = os.path.join(ARCHIVE_ROOT, "resumes")
MANIFESTS_DIR = os.path.join(ARCHIVE_ROOT, "manifests")

# Ensure target directories exist
for p in [
    os.path.join(ACADEMIC_DIR, "5001_Knowledge_Management", "notes"),
    os.path.join(ACADEMIC_DIR, "5001_Knowledge_Management", "pyqs"),
    os.path.join(ACADEMIC_DIR, "5001_Knowledge_Management", "extracted"),
    os.path.join(ACADEMIC_DIR, "5002_Java_Web", "notes"),
    os.path.join(ACADEMIC_DIR, "5002_Java_Web", "pyqs"),
    os.path.join(ACADEMIC_DIR, "5002_Java_Web", "extracted"),
    os.path.join(ACADEMIC_DIR, "5003_Computer_Networks", "notes"),
    os.path.join(ACADEMIC_DIR, "5003_Computer_Networks", "pyqs"),
    os.path.join(ACADEMIC_DIR, "5003_Computer_Networks", "extracted"),
    os.path.join(ACADEMIC_DIR, "5004_Numerical_Methods", "notes"),
    os.path.join(ACADEMIC_DIR, "5004_Numerical_Methods", "pyqs"),
    os.path.join(ACADEMIC_DIR, "5004_Numerical_Methods", "extracted"),
    os.path.join(PROJECTS_DIR, "bulkbeat"),
    os.path.join(PROJECTS_DIR, "bevm"),
    os.path.join(PROJECTS_DIR, "csms"),
    RESUMES_DIR,
    MANIFESTS_DIR
]:
    os.makedirs(p, exist_ok=True)

def compute_hash(file_path):
    hasher = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception as e:
        return f"ERROR: {e}"

manifest = []

# Mapping from A: Drive files to clean archive destinations
COPY_MAP = [
    # 5001 Knowledge Management
    ("BCA_5001_Knowledge_Management_Unit_I_Detailed_Notes.pdf", os.path.join(ACADEMIC_DIR, "5001_Knowledge_Management", "notes"), "academic_notes"),
    ("BCA_5001_Knowledge_Management_Unit_I_Detailed_PYQ_Notes.pdf", os.path.join(ACADEMIC_DIR, "5001_Knowledge_Management", "notes"), "academic_notes"),
    ("BCA_5001_Knowledge_Management_Unit_II_Study_Guide.pdf", os.path.join(ACADEMIC_DIR, "5001_Knowledge_Management", "notes"), "academic_notes"),
    ("BCA_5001_Knowledge_Management_Unit_III_Detailed_Study_Guide.pdf", os.path.join(ACADEMIC_DIR, "5001_Knowledge_Management", "notes"), "academic_notes"),
    ("BCA_5001_Knowledge_Management_Unit_IV_Detailed_Study_Guide.pdf", os.path.join(ACADEMIC_DIR, "5001_Knowledge_Management", "notes"), "academic_notes"),
    
    # 5002 Java
    ("JAVAKPH.pdf", os.path.join(ACADEMIC_DIR, "5002_Java_Web", "notes"), "academic_notes"),
    
    # 5003 Computer Networks
    ("BCA_5003_Unit_I.pdf", os.path.join(ACADEMIC_DIR, "5003_Computer_Networks", "notes"), "academic_notes"),
    ("BCA-5003_Computer_Network_Unit_1_Study_Guide.pdf", os.path.join(ACADEMIC_DIR, "5003_Computer_Networks", "notes"), "academic_notes"),
    ("BCA_5003_Unit_II_Exact_Unit_I_Format_Detailed_Notes_PYQs.pdf", os.path.join(ACADEMIC_DIR, "5003_Computer_Networks", "notes"), "academic_notes"),
    ("BCA_5003_Unit_III_.pdf", os.path.join(ACADEMIC_DIR, "5003_Computer_Networks", "notes"), "academic_notes"),
    ("BCA_5003_Unit_IV.pdf", os.path.join(ACADEMIC_DIR, "5003_Computer_Networks", "notes"), "academic_notes"),
    ("BCA_5003_Unit_V.pdf", os.path.join(ACADEMIC_DIR, "5003_Computer_Networks", "notes"), "academic_notes"),
    ("BCA V Sem_ Computer Network_2022-23.pdf", os.path.join(ACADEMIC_DIR, "5003_Computer_Networks", "pyqs"), "university_pyq"),
    ("BCA V Sem_ Computer Network_2023-24.pdf", os.path.join(ACADEMIC_DIR, "5003_Computer_Networks", "pyqs"), "university_pyq"),
    ("BCA V Sem_Computer Network_2021.pdf", os.path.join(ACADEMIC_DIR, "5003_Computer_Networks", "pyqs"), "university_pyq"),

    # 5004 Numerical Methods
    ("5004 unit 1.pdf", os.path.join(ACADEMIC_DIR, "5004_Numerical_Methods", "notes"), "academic_notes"),
    ("BCA-5004-Unit-1-Roots-of-Equations-Notes.pdf", os.path.join(ACADEMIC_DIR, "5004_Numerical_Methods", "notes"), "academic_notes"),

    # Projects & Evidence
    ("Quotation_cum_MSA_Bulkbeat.pdf", os.path.join(PROJECTS_DIR, "bulkbeat"), "project_commercial_evidence"),
    ("pulse_users_20260807_1854.csv", os.path.join(PROJECTS_DIR, "bulkbeat"), "project_user_metrics"),
    ("users.csv", os.path.join(PROJECTS_DIR, "bulkbeat"), "project_user_metrics"),
    ("Component-Choice-FreeTierNotes-MonthlyCost.csv", os.path.join(PROJECTS_DIR, "bulkbeat"), "architecture_infrastructure"),

    # Resumes
    ("Sarthak_Srivastava_Resume.pdf", RESUMES_DIR, "historical_resume")
]

print("--> Archiving source files from A: drive into source_archive/...")
for filename, dest_dir, category in COPY_MAP:
    src_file = os.path.join(A_DRIVE, filename)
    dest_file = os.path.join(dest_dir, filename)
    
    if os.path.exists(src_file):
        try:
            # Copy without touching original
            shutil.copy2(src_file, dest_file)
            size = os.path.getsize(dest_file)
            sha256 = compute_hash(dest_file)
            manifest.append({
                "original_path": src_file,
                "copied_path": dest_file,
                "filename": filename,
                "category": category,
                "size_bytes": size,
                "sha256": sha256,
                "status": "archived_verified"
            })
            print(f"  [+] Archived: {filename} ({size / 1024:.1f} KB)")
        except Exception as e:
            print(f"  [-] Failed to copy {filename}: {e}")
    else:
        print(f"  [?] Not found on A: {filename}")

# Save the Source Manifest
manifest_file = os.path.join(MANIFESTS_DIR, "source_manifest.json")
with open(manifest_file, "w", encoding="utf-8") as f:
    json.dump({
        "total_files_archived": len(manifest),
        "source_archive_root": ARCHIVE_ROOT,
        "manifest": manifest
    }, f, indent=2)

print(f"\n--> Source Manifest successfully generated at: {manifest_file}")
print(f"--> Total source files archived: {len(manifest)}")
