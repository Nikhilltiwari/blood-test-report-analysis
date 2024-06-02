# utilities/parser.py
import fitz  # PyMuPDF
import re

def parse_blood_test_report(pdf_path):
    # Open the PDF file
    document = fitz.open(pdf_path)
    
    # Initialize an empty string to hold the text
    text = ""
    
    # Extract text from each page
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()

    # Define a regex pattern to extract test names and results
    pattern = re.compile(r'(\w[\w\s]+?)\s+(\d+\.\d+)\s+\w+/\w+\s+\d+\.\d+\s+-\s+\d+\.\d+')
    
    # Extract test names and results
    results = {}
    for match in pattern.finditer(text):
        test_name, result = match.groups()
        results[test_name.strip()] = float(result)
    
    return results
