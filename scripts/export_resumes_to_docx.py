#!/usr/bin/env python3
"""
scripts/export_resumes_to_docx.py
Generates professional ATS-optimized Microsoft Word (.docx) editions for each resume profile:
- Sarthak_Backend_Resume.docx
- Sarthak_Software_Engineer_Resume.docx
- Sarthak_Data_AI_Resume.docx
Ensures single-page A4 density, standard fonts, and zero extra blank pages.
"""

import os
import sys
import json
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

WEB_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESUMES_JSON = os.path.join(WEB_ROOT, "content", "resumes", "resumes_all.json")
EXPORTS_DIR = os.path.join(WEB_ROOT, "exports", "resumes")
os.makedirs(EXPORTS_DIR, exist_ok=True)

PROFILES = [
    ("python_backend", "Sarthak_Backend_Resume.docx"),
    ("software_engineer", "Sarthak_Software_Engineer_Resume.docx"),
    ("data_ai", "Sarthak_Data_AI_Resume.docx")
]

def set_cell_margins(cell, top=50, bottom=50, left=50, right=50):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def add_heading_with_border(doc, title):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(5)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    
    run = p.add_run(title)
    run.font.name = "Arial"
    run.font.size = Pt(9.5)
    run.font.bold = True
    run.font.color.rgb = RGBColor(15, 23, 42)
    
    # Add bottom border XML
    pPr = p._element.get_or_add_pPr()
    pBdr = parse_xml(r'<w:pBdr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
                     r'<w:bottom w:val="single" w:sz="6" w:space="1" w:color="64748B"/>'
                     r'</w:pBdr>')
    pPr.append(pBdr)

def build_docx_for_profile(profile_key, filename):
    with open(RESUMES_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    r = data.get(profile_key)
    if not r:
        print(f"[-] Profile {profile_key} not found")
        return False

    doc = Document()
    
    # Set tight A4 margins
    section = doc.sections[0]
    section.page_width = Inches(8.27)
    section.page_height = Inches(11.69)
    section.top_margin = Inches(0.4)
    section.bottom_margin = Inches(0.4)
    section.left_margin = Inches(0.45)
    section.right_margin = Inches(0.45)
    
    # 1. Header
    p_name = doc.add_paragraph()
    p_name.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_name.paragraph_format.space_before = Pt(0)
    p_name.paragraph_format.space_after = Pt(1)
    
    run_name = p_name.add_run(r["contact"]["name"])
    run_name.font.name = "Arial"
    run_name.font.size = Pt(17)
    run_name.font.bold = True
    run_name.font.color.rgb = RGBColor(15, 23, 42)
    
    p_tag = doc.add_paragraph()
    p_tag.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_tag.paragraph_format.space_before = Pt(0)
    p_tag.paragraph_format.space_after = Pt(2)
    run_tag = p_tag.add_run(r["contact"].get("tagline", ""))
    run_tag.font.name = "Arial"
    run_tag.font.size = Pt(8.8)
    run_tag.font.bold = True
    run_tag.font.color.rgb = RGBColor(30, 58, 138)
    
    p_contact = doc.add_paragraph()
    p_contact.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_contact.paragraph_format.space_before = Pt(0)
    p_contact.paragraph_format.space_after = Pt(5)
    
    c = r["contact"]
    contact_parts = [
        f"{c['location']}",
        f"{c['email']}",
        f"{c['phone']}",
        f"{c['website'].replace('https://', '')}",
        f"{c['github'].replace('https://', '')}",
        f"{c['linkedin'].replace('https://', '')}"
    ]
    run_c = p_contact.add_run("   |   ".join(contact_parts))
    run_c.font.name = "Arial"
    run_c.font.size = Pt(8.2)
    run_c.font.color.rgb = RGBColor(71, 85, 105)
    
    # Add bottom border under contact
    pPr = p_contact._element.get_or_add_pPr()
    pBdr = parse_xml(r'<w:pBdr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
                     r'<w:bottom w:val="single" w:sz="12" w:space="3" w:color="0F172A"/>'
                     r'</w:pBdr>')
    pPr.append(pBdr)

    # 2. Professional Summary
    add_heading_with_border(doc, "PROFESSIONAL SUMMARY")
    p_sum = doc.add_paragraph()
    p_sum.paragraph_format.space_before = Pt(1)
    p_sum.paragraph_format.space_after = Pt(4)
    run_sum = p_sum.add_run(r["summary"])
    run_sum.font.name = "Arial"
    run_sum.font.size = Pt(8.5)
    run_sum.font.color.rgb = RGBColor(51, 65, 85)

    # 3. Technical Skills
    add_heading_with_border(doc, "TECHNICAL SKILLS")
    for cat, sk in r["skills"].items():
        p_sk = doc.add_paragraph()
        p_sk.paragraph_format.space_before = Pt(0)
        p_sk.paragraph_format.space_after = Pt(1)
        r_cat = p_sk.add_run(f"{cat}: ")
        r_cat.font.name = "Arial"
        r_cat.font.size = Pt(8.3)
        r_cat.font.bold = True
        r_cat.font.color.rgb = RGBColor(15, 23, 42)
        
        r_val = p_sk.add_run(sk)
        r_val.font.name = "Arial"
        r_val.font.size = Pt(8.3)
        r_val.font.color.rgb = RGBColor(51, 65, 85)

    # 4. Work Experience
    if r.get("work_experience"):
        add_heading_with_border(doc, "WORK EXPERIENCE")
        for exp in r["work_experience"]:
            p_exp = doc.add_paragraph()
            p_exp.paragraph_format.space_before = Pt(2)
            p_exp.paragraph_format.space_after = Pt(0)
            p_exp.paragraph_format.keep_with_next = True
            
            r_role = p_exp.add_run(exp["role"])
            r_role.font.name = "Arial"
            r_role.font.size = Pt(8.8)
            r_role.font.bold = True
            r_role.font.color.rgb = RGBColor(15, 23, 42)
            
            r_comp = p_exp.add_run(f" · {exp['company']}")
            r_comp.font.name = "Arial"
            r_comp.font.size = Pt(8.3)
            r_comp.font.bold = True
            r_comp.font.color.rgb = RGBColor(30, 58, 138)
            
            r_meta = p_exp.add_run(f"    ({exp['duration']} | {exp['location']})")
            r_meta.font.name = "Arial"
            r_meta.font.size = Pt(7.8)
            r_meta.font.color.rgb = RGBColor(100, 116, 139)
            
            for b in exp["bullets"]:
                p_b = doc.add_paragraph(style='List Bullet')
                p_b.paragraph_format.space_before = Pt(0)
                p_b.paragraph_format.space_after = Pt(1)
                r_b = p_b.add_run(b)
                r_b.font.name = "Arial"
                r_b.font.size = Pt(8.3)
                r_b.font.color.rgb = RGBColor(31, 41, 55)

    # 5. Key Engineering Projects
    add_heading_with_border(doc, "KEY ENGINEERING PROJECTS")
    for proj in r.get("experience_and_projects", []):
        p_proj = doc.add_paragraph()
        p_proj.paragraph_format.space_before = Pt(2)
        p_proj.paragraph_format.space_after = Pt(0)
        p_proj.paragraph_format.keep_with_next = True
        
        r_pname = p_proj.add_run(proj["name"])
        r_pname.font.name = "Arial"
        r_pname.font.size = Pt(8.8)
        r_pname.font.bold = True
        r_pname.font.color.rgb = RGBColor(15, 23, 42)
        
        r_prole = p_proj.add_run(f" — {proj['role']}")
        r_prole.font.name = "Arial"
        r_prole.font.size = Pt(8)
        r_prole.font.color.rgb = RGBColor(71, 85, 105)
        
        for b in proj["bullets"]:
            p_b = doc.add_paragraph(style='List Bullet')
            p_b.paragraph_format.space_before = Pt(0)
            p_b.paragraph_format.space_after = Pt(1)
            r_b = p_b.add_run(b)
            r_b.font.name = "Arial"
            r_b.font.size = Pt(8.3)
            r_b.font.color.rgb = RGBColor(31, 41, 55)

    # 6. Education
    add_heading_with_border(doc, "EDUCATION")
    p_edu = doc.add_paragraph()
    p_edu.paragraph_format.space_before = Pt(1)
    p_edu.paragraph_format.space_after = Pt(2)
    
    r_deg = p_edu.add_run(r["education"]["degree"])
    r_deg.font.name = "Arial"
    r_deg.font.size = Pt(8.5)
    r_deg.font.bold = True
    r_deg.font.color.rgb = RGBColor(15, 23, 42)
    
    r_inst = p_edu.add_run(f" — {r['education']['institution']}")
    r_inst.font.name = "Arial"
    r_inst.font.size = Pt(8.3)
    r_inst.font.color.rgb = RGBColor(51, 65, 85)
    
    r_yr = p_edu.add_run(f"    ({r['education']['duration']} | {r['education']['academic_standing']})")
    r_yr.font.name = "Arial"
    r_yr.font.size = Pt(8)
    r_yr.font.color.rgb = RGBColor(100, 116, 139)

    # 7. Certifications & Honors
    if r.get("certifications"):
        add_heading_with_border(doc, "CERTIFICATIONS & HONORS")
        certs = r["certifications"]
        mid = (len(certs) + 1) // 2
        col1 = certs[:mid]
        col2 = certs[mid:]
        
        table = doc.add_table(rows=0, cols=2)
        table.alignment = WD_ALIGN_PARAGRAPH.LEFT
        table.autofit = False
        
        for i in range(max(len(col1), len(col2))):
            row = table.add_row()
            cell_left = row.cells[0]
            cell_right = row.cells[1]
            cell_left.width = Inches(3.68)
            cell_right.width = Inches(3.68)
            set_cell_margins(cell_left, top=10, bottom=10, left=0, right=10)
            set_cell_margins(cell_right, top=10, bottom=10, left=0, right=10)
            
            p_l = cell_left.paragraphs[0]
            p_l.paragraph_format.space_before = Pt(0)
            p_l.paragraph_format.space_after = Pt(1)
            if i < len(col1):
                r_b = p_l.add_run("• ")
                r_b.font.name = "Arial"
                r_b.font.size = Pt(8.1)
                r_b.font.bold = True
                r_b.font.color.rgb = RGBColor(15, 23, 42)
                r_t = p_l.add_run(col1[i])
                r_t.font.name = "Arial"
                r_t.font.size = Pt(8.1)
                r_t.font.color.rgb = RGBColor(51, 65, 85)
                
            p_r = cell_right.paragraphs[0]
            p_r.paragraph_format.space_before = Pt(0)
            p_r.paragraph_format.space_after = Pt(1)
            if i < len(col2):
                r_b = p_r.add_run("• ")
                r_b.font.name = "Arial"
                r_b.font.size = Pt(8.1)
                r_b.font.bold = True
                r_b.font.color.rgb = RGBColor(15, 23, 42)
                r_t = p_r.add_run(col2[i])
                r_t.font.name = "Arial"
                r_t.font.size = Pt(8.1)
                r_t.font.color.rgb = RGBColor(51, 65, 85)

    out_path = os.path.join(EXPORTS_DIR, filename)
    doc.save(out_path)
    print(f"--> Saved {filename} ({os.path.getsize(out_path) / 1024:.1f} KB)")
    return True

def main():
    print("=" * 70)
    print("EXPORTING RESUMES TO MICROSOFT WORD (.DOCX)")
    print("=" * 70)
    for p_key, fname in PROFILES:
        build_docx_for_profile(p_key, fname)
    print("[+] All resume DOCX files successfully exported!")

if __name__ == "__main__":
    main()
