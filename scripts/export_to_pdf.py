import os
import sys

WEB_ROOT = r"D:\Projects\Placement_Master_Handbook_Web"
DOCX_PATH = os.path.join(WEB_ROOT, "exports", "docx", "Sarthak_30_Day_Placement_Master_Handbook.docx")
PDF_PATH = os.path.join(WEB_ROOT, "exports", "pdf", "Sarthak_30_Day_Placement_Master_Handbook.pdf")

def convert_docx_to_pdf():
    print(f"--> Converting {DOCX_PATH} to {PDF_PATH} via Word Automation...")
    if not os.path.exists(DOCX_PATH):
        print(f"[-] Source DOCX not found at: {DOCX_PATH}")
        return False
        
    try:
        import win32com.client
        import pythoncom
        pythoncom.CoInitialize()
        
        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False
        word.DisplayAlerts = 0
        
        doc = word.Documents.Open(DOCX_PATH)
        # wdFormatPDF = 17
        doc.SaveAs(PDF_PATH, FileFormat=17)
        doc.Close()
        word.Quit()
        pythoncom.CoUninitialize()
        
        size_mb = os.path.getsize(PDF_PATH) / 1024 / 1024
        print(f"--> SUCCESS: Native PDF compiled ({size_mb:.2f} MB) at: {PDF_PATH}")
        return True
    except Exception as e:
        print(f"[-] Word conversion failed or Word not installed: {e}")
        return False

if __name__ == "__main__":
    convert_docx_to_pdf()
