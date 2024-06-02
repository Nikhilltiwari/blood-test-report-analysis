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
            key = key.strip()
            value = value.strip()
            if value:
                try:
                    extracted_info[key] = float(value)
                except ValueError:
                    extracted_info[key] = value
            else:
                extracted_info[key] = None

   
    important_metrics = ["BUN/creatinine ratio", "Hemoglobin", "Cholesterol"]
    refined_info = {k: v for k, v in extracted_info.items() if any(metric in k for metric in important_metrics)}

    # Log extracted information for debugging purposes
    print("Extracted Info:", refined_info)

    return refined_info
