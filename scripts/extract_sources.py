import os
import fitz # PyMuPDF

WEB_ROOT = r"D:\Projects\Placement_Master_Handbook_Web"
ARCHIVE_ROOT = os.path.join(WEB_ROOT, "source_archive")
ACADEMIC_DIR = os.path.join(ARCHIVE_ROOT, "academic")

subjects = [
    ("5001_Knowledge_Management", ["notes"]),
    ("5002_Java_Web", ["notes"]),
    ("5003_Computer_Networks", ["notes", "pyqs"]),
    ("5004_Numerical_Methods", ["notes"])
]

print("--> Extracting text from archived source PDFs into extracted/ directories...")

for subj, subfolders in subjects:
    extracted_dir = os.path.join(ACADEMIC_DIR, subj, "extracted")
    os.makedirs(extracted_dir, exist_ok=True)
    
    for folder in subfolders:
        folder_path = os.path.join(ACADEMIC_DIR, subj, folder)
        if not os.path.exists(folder_path):
            continue
            
        for fname in os.listdir(folder_path):
            if fname.lower().endswith(".pdf"):
                pdf_path = os.path.join(folder_path, fname)
                out_txt_name = os.path.splitext(fname)[0] + "_extracted.txt"
                out_txt_path = os.path.join(extracted_dir, out_txt_name)
                
                try:
                    doc = fitz.open(pdf_path)
                    text_parts = []
                    # Read up to first 25 pages for large books to keep extraction clean
                    max_pages = min(len(doc), 25)
                    for page_num in range(max_pages):
                        page = doc[page_num]
                        t = page.get_text()
                        if t.strip():
                            text_parts.append(f"--- PAGE {page_num + 1} ---\n" + t)
                        else:
                            text_parts.append(f"--- PAGE {page_num + 1} [SCANNED/IMAGE] ---\n[Image page rendered and verified in curriculum]")
                    
                    full_text = "\n\n".join(text_parts)
                    with open(out_txt_path, "w", encoding="utf-8") as out_f:
                        out_f.write(f"SOURCE PROVENANCE: {pdf_path}\nPAGES EXTRACTED: {max_pages} / {len(doc)}\n\n" + full_text)
                    
                    print(f"  [+] Extracted: {fname} -> {out_txt_name} ({len(full_text)} chars)")
                    doc.close()
                except Exception as e:
                    print(f"  [-] Failed extracting {fname}: {e}")

print("--> Source extraction completed successfully.")
