import fitz  # PyMuPDF

def parse_blood_test_report(pdf_path):
    # Open the PDF file
    document = fitz.open(pdf_path)
    text = ""
    for page_num in range(document.page_count):
        page = document.load_page(page_num)
        text += page.get_text()
    
    # Simple text parsing logic (can be improved)
    extracted_info = {}
    lines = text.split('\n')
    for line in lines:
        if ':' in line:
            key, value = line.split(':', 1)
            extracted_info[key.strip()] = float(value.strip())
    
    return extracted_info
