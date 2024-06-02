import fitz  # PyMuPDF
import re

def parse_blood_test_report(pdf_path):
    # Open the PDF file
    document = fitz.open(pdf_path)
    text = ""
    for page_num in range(document.page_count):
        page = document.load_page(page_num)
        text += page.get_text()

    # Define a list of important metrics to look for
    important_metrics = {
        "BUN/creatinine ratio": None,
        "Hemoglobin": None,
        "Cholesterol": None,
        "Glucose": None,
        "Triglycerides": None
    }

    # Use regular expressions to match key metrics
    patterns = {
        "BUN/creatinine ratio": re.compile(r"BUN/creatinine ratio\s*[:\-]?\s*([\d\.]+)"),
        "Hemoglobin": re.compile(r"Hemoglobin\s*[:\-]?\s*([\d\.]+)"),
        "Cholesterol": re.compile(r"Cholesterol\s*[:\-]?\s*([\d\.]+)"),
        "Glucose": re.compile(r"Glucose\s*[:\-]?\s*([\d\.]+)"),
        "Triglycerides": re.compile(r"Triglycerides\s*[:\-]?\s*([\d\.]+)")
    }

    # Search text for matches
    for metric, pattern in patterns.items():
        match = pattern.search(text)
        if match:
            try:
                important_metrics[metric] = float(match.group(1))
            except ValueError:
                important_metrics[metric] = None

    # Remove None values
    extracted_info = {k: v for k, v in important_metrics.items() if v is not None}

    # Log extracted information for debugging purposes
    print("Extracted Info:", extracted_info)

    return extracted_info
