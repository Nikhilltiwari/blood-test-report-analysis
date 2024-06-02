# main.py
import sys
import os

# Add the project directory to the sys.path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_dir)

from models.health_assistant import HealthAssistant

def main():
    pdf_path = "path/to/sample_report.pdf"  # Update with the actual path to your sample report
    
    assistant = HealthAssistant()
    result = assistant.process_blood_test(pdf_path)
    print(result)

if __name__ == "__main__":
    main()
