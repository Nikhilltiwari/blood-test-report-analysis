# utils/parser.py
import re
import fitz  # PyMuPDF
from typing import Dict, Any, List, Tuple

def parse_blood_test_report(pdf_path: str) -> Tuple[Dict[str, Any], List[float]]:
    extracted_info = {}
    numeric_values = []

    # Open the PDF file
    doc = fitz.open(pdf_path)

    text = ""
    for page in doc:
        text += page.get_text()

    print("Extracted Text from PDF:\n", text)  # Debugging statement

    # Define test patterns
    test_patterns = {
        'Hemoglobin': r'Hemoglobin\s*\(Photometry\)\s+([\d.]+)\s*g/dL',
        'PCV': r'Packed Cell Volume\s*\(PCV\)\s*\(Calculated\)\s+([\d.]+)\s*%',
        'RBC Count': r'RBC Count\s*\(Electrical Impedence\)\s+([\d.]+)\s*mill/mm3',
        'MCV': r'MCV\s*\(Electrical Impedence\)\s+([\d.]+)\s*fL',
        'MCH': r'MCH\s*\(Calculated\)\s+([\d.]+)\s*pg',
        'MCHC': r'MCHC\s*\(Calculated\)\s+([\d.]+)\s*g/dL',
        'RDW': r'Red Cell Distribution Width\s*\(RDW\)\s*\(Electrical Impedence\)\s+([\d.]+)\s*%',
        'TLC': r'Total Leukocyte Count\s*\(Electrical Impedence\)\s+([\d.]+)\s*thou/mm3',
        'Platelet Count': r'Platelet Count\s*\(Electrical impedence\)\s+([\d.]+)\s*thou/mm3',
        'MPV': r'Mean Platelet Volume\s*\(Electrical Impedence\)\s+([\d.]+)\s*fL',
        'Creatinine': r'Creatinine\s*\(Modified Jaffe,Kinetic\)\s+([\d.]+)\s*mg/dL',
        'Urea': r'Urea\s*\(Urease UV\)\s+([\d.]+)\s*mg/dL',
        'BUN': r'Urea Nitrogen\s+Blood\s*\(Calculated\)\s+([\d.]+)\s*mg/dL',
        'Cholesterol': r'Cholesterol,\s+Total\s*\(CHO-POD\)\s+([\d.]+)\s*mg/dL',
        'Triglycerides': r'Triglycerides\s*\(GPO-POD\)\s+([\d.]+)\s*mg/dL',
        'HDL': r'HDL\s+Cholesterol\s*\(Enzymatic Immunoinhibition\)\s+([\d.]+)\s*mg/dL',
        'LDL': r'LDL Cholesterol,\s+Calculated\s*\(Calculated\)\s+([\d.]+)\s*mg/dL',
        'VLDL': r'VLDL Cholesterol,\s+Calculated\s*\(Calculated\)\s+([\d.]+)\s*mg/dL',
        'Vitamin D': r'Vitamin\sD,\s+25\s+-\s+Hydroxy\s+([\d.]+)\s*nmol/L',
        'Vitamin B12': r'Vitamin\s+B12;\s+cyanocobalamin\s+([\d.]+)\s*pg/mL',
    }

    for test_name, pattern in test_patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            value = match.group(1)
            extracted_info[test_name] = float(value)
            numeric_values.append(float(value))
            print(f"Extracted {test_name}: {value}")  # Debugging statement
        else:
            print(f"Pattern not found for {test_name}")  # Debugging statement

    print("Final Extracted Info:", extracted_info)  # Debugging statement
    print("Final Numeric Values:", numeric_values)  # Debugging statement

    return extracted_info, numeric_values

if __name__ == "__main__":
    # Testing with a sample file
    pdf_path = 'C:/Users/nikhl/Downloads/sample report.pdf'  
    extracted_info, numeric_values = parse_blood_test_report(pdf_path)
    print("Extracted Info:", extracted_info)
    print("Numeric Values:", numeric_values)

