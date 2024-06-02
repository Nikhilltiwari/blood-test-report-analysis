# main.py
from models.health_assistant import HealthAssistant

def main():
    report_content = """Hemoglobin 15.00 g/dL 13.00 - 17.00
    Packed Cell Volume (PCV) 45.00 % 40.00 - 50.00
    RBC Count 4.50 mill/mm3 4.50 - 5.50"""
    
    assistant = HealthAssistant()
    result = assistant.process_blood_test(report_content)
    print(result)

if __name__ == "__main__":
    main()
