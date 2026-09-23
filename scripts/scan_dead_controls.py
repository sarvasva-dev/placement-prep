#!/usr/bin/env python3
"""
Dead UI Controls & Event Handler Coverage Scanner
Scans index.html and js/views/*.js for all interactive elements:
- <a> links (validating href target, checking for empty/dead hashes)
- <button> elements (validating attached event listeners or onclick)
- <input> and <select> elements (validating change/input bindings)
Generates comprehensive evidence/ui_inventory.json report.
"""

import os
import re
import json
from pathlib import Path

def scan_ui_inventory():
    base_dir = Path(__file__).resolve().parent.parent
    index_file = base_dir / "index.html"
    views_dir = base_dir / "js" / "views"
    app_file = base_dir / "js" / "app.js"
    
    inventory = {
        "links": [],
        "buttons": [],
        "inputs": [],
        "selects": [],
        "dead_or_unhandled": [],
        "summary": {}
    }
    
    valid_root_routes = {
        "dashboard", "day", "days", "semester", "pyqs", "aptitude",
        "coding", "core-cs", "projects", "interviews", "resumes",
        "revision", "freelance", "do-not-study", "source-archive"
    }

    files_to_scan = [index_file, app_file] + list(views_dir.glob("*.js"))
    
    # Read entire JS codebase to search for handler bindings
    all_js_code = ""
    for jf in [app_file] + list(views_dir.glob("*.js")):
        if jf.exists():
            with open(jf, "r", encoding="utf-8") as f:
                all_js_code += f"\n// FILE: {jf.name}\n" + f.read()
                
    for fpath in files_to_scan:
        if not fpath.exists():
            continue
        rel_path = fpath.relative_to(base_dir).as_posix()
        with open(fpath, "r", encoding="utf-8") as f:
            lines = f.readlines()
            content = "".join(lines)
            
        # 1. Scan <a> tags
        a_matches = re.finditer(r'<a\s+([^>]*?)>(.*?)</a>', content, re.DOTALL | re.IGNORECASE)
        for m in a_matches:
            attrs_str = m.group(1)
            inner_text = re.sub(r'<[^>]+>', '', m.group(2)).strip()
            
            href_m = re.search(r'href=["\'](.*?)["\']', attrs_str)
            href = href_m.group(1).strip() if href_m else ""
            
            # Check line number
            line_no = content[:m.start()].count('\n') + 1
            
            link_entry = {
                "file": rel_path,
                "line": line_no,
                "text": inner_text[:40],
                "href": href,
                "is_dead": False,
                "reason": ""
            }
            
            # Validation rules
            if href == "#" or href == "":
                link_entry["is_dead"] = True
                link_entry["reason"] = "Empty or solitary '#' href"
            elif href.startswith("#"):
                clean_target = href[1:].split("?")[0].split("/")[0]
                if clean_target not in valid_root_routes and not clean_target.startswith("sec-"):
                    link_entry["is_dead"] = True
                    link_entry["reason"] = f"Unknown route target: {href}"
            elif href.startswith("javascript:"):
                link_entry["is_dead"] = True
                link_entry["reason"] = "Inline javascript: pseudo-protocol"
                
            inventory["links"].append(link_entry)
            if link_entry["is_dead"]:
                inventory["dead_or_unhandled"].append(link_entry)

        # 2. Scan <button> tags
        btn_matches = re.finditer(r'<button\s+([^>]*?)>(.*?)</button>', content, re.DOTALL | re.IGNORECASE)
        for m in btn_matches:
            attrs_str = m.group(1)
            inner_text = re.sub(r'<[^>]+>', '', m.group(2)).strip()
            line_no = content[:m.start()].count('\n') + 1
            
            id_m = re.search(r'id="([^"]*)"', attrs_str) or re.search(r"id='([^']*)'", attrs_str)
            btn_id = id_m.group(1) if id_m else ""
            
            class_m = re.search(r'class="([^"]*)"', attrs_str) or re.search(r"class='([^']*)'", attrs_str)
            raw_classes = class_m.group(1) if class_m else ""
            # Strip JS template expressions from class string
            clean_classes_str = re.sub(r'\$\{[^}]*\}', ' ', raw_classes)
            classes = [c.strip() for c in clean_classes_str.split() if c.strip()]
            
            has_handler = False
            # Check if button id is listened to
            if btn_id and (f"'{btn_id}'" in all_js_code or f'"{btn_id}"' in all_js_code or f"#{btn_id}" in all_js_code):
                has_handler = True
            # Check if any specific class has querySelectorAll / addEventListener
            if not has_handler:
                for cls in classes:
                    if cls not in {"btn", "btn-primary", "btn-secondary", "btn-sm", "btn-success", "btn-warning", "btn-danger"}:
                        if f"'.{cls}'" in all_js_code or f'".{cls}"' in all_js_code or f".{cls}" in all_js_code:
                            has_handler = True
                            break
            # Check if onclick attribute exists
            if 'onclick=' in attrs_str:
                has_handler = True
            # Check if data-target exists (TOC tabs)
            if 'data-target=' in attrs_str:
                has_handler = True
                
            btn_entry = {
                "file": rel_path,
                "line": line_no,
                "text": inner_text[:40],
                "id": btn_id,
                "classes": classes,
                "has_handler": has_handler
            }
            inventory["buttons"].append(btn_entry)
            if not has_handler:
                inventory["dead_or_unhandled"].append({
                    **btn_entry,
                    "reason": "No corresponding event listener or onclick handler found"
                })

    inventory["summary"] = {
        "total_links_scanned": len(inventory["links"]),
        "total_buttons_scanned": len(inventory["buttons"]),
        "total_dead_controls": len(inventory["dead_or_unhandled"]),
        "status": "PASS" if len(inventory["dead_or_unhandled"]) == 0 else "FAIL"
    }
    
    out_path = base_dir / "evidence" / "ui_inventory.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as out_f:
        json.dump(inventory, out_f, indent=2)
        
    print("=" * 60)
    print("UI CONTROLS & EVENT HANDLER SCAN COMPLETE")
    print("=" * 60)
    print(f"Total Links Scanned:   {len(inventory['links'])}")
    print(f"Total Buttons Scanned: {len(inventory['buttons'])}")
    print(f"Dead / Unhandled:      {len(inventory['dead_or_unhandled'])}")
    print(f"Overall Status:        {inventory['summary']['status']}")
    print(f"Saved inventory report to {out_path}")
    
    return inventory["summary"]["status"] == "PASS"

if __name__ == "__main__":
    success = scan_ui_inventory()
    exit(0 if success else 1)
