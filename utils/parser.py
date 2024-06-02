# utils/parser.py
import re
from typing import Dict, Any

def parse_blood_test_report(pdf_path: str) -> Dict[str, Any]:
    extracted_info = {}
    numeric_values = []
    
    with open(pdf_path, 'r') as file:
        lines = file.readlines()
    
    test_patterns = {
        'Hemoglobin': r'Hemoglobin\s+(\d+\.\d+)\s+g/dL',
        'PCV': r'Packed Cell Volume \(PCV\)\s+(\d+\.\d+)\s+%',
        'RBC Count': r'RBC Count\s+(\d+\.\d+)\s+mill/mm3',
        'MCV': r'MCV\s+(\d+\.\d+)\s+fL',
        'MCH': r'MCH\s+(\d+\.\d+)\s+pg',
        'MCHC': r'MCHC\s+(\d+\.\d+)\s+g/dL',
        'RDW': r'Red Cell Distribution Width \(RDW\)\s+(\d+\.\d+)\s+%',
        'TLC': r'Total Leukocyte Count\s+(\d+\.\d+)\s+thou/mm3',
        'Platelet Count': r'Platelet Count\s+(\d+\.\d+)\s+thou/mm3',
        'MPV': r'Mean Platelet Volume\s+(\d+\.\d+)\s+fL',
        'Creatinine': r'Creatinine\s+(\d+\.\d+)\s+mg/dL',
        'Urea': r'Urea\s+(\d+\.\d+)\s+mg/dL',
        'BUN': r'Urea Nitrogen\s+Blood\s+(\d+\.\d+)\s+mg/dL',
        'Cholesterol': r'Cholesterol,\s+Total\s+(\d+\.\d+)\s+mg/dL',
        'Triglycerides': r'Triglycerides\s+(\d+\.\d+)\s+mg/dL',
        'HDL': r'HDL\s+Cholesterol\s+(\d+\.\d+)\s+mg/dL',
        'LDL': r'LDL\s+Cholesterol,\s+Calculated\s+(\d+\.\d+)\s+mg/dL',
        'VLDL': r'VLDL\s+Cholesterol,\s+Calculated\s+(\d+\.\d+)\s+mg/dL',
        'Vitamin D': r'VITAMIN\s+D,\s+25\s+-\s+HYDROXY\s+(\d+\.\d+)\s+nmol/L',
        'Vitamin B12': r'VITAMIN\s+B12;\s+CYANOCOBALAMIN\s+(\d+\.\d+)\s+pg/mL',
    }

    for line in lines:
        for test_name, pattern in test_patterns.items():
            match = re.search(pattern, line)
            if match:
                value = match.group(1)
                extracted_info[test_name] = float(value)
                numeric_values.append(float(value))
    
    return extracted_info, numeric_values

if __name__ == "__main__":
    # Testing with a sample file
    pdf_path = 'sample_report.txt'  # Change this to the path of the sample report file
    extracted_info, numeric_values = parse_blood_test_report(pdf_path)
    print("Extracted Info:", extracted_info)
    print("Numeric Values:", numeric_values)

