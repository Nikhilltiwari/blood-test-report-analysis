
import os
from dotenv import load_dotenv

# Loading environment variables from .env file
load_dotenv()

from models.health_assistant import HealthAssistant

def main():
    pdf_path = "C:/Users/nikhl/Downloads/sample report.pdf"  
    
    assistant = HealthAssistant()
    result = assistant.process_blood_test(pdf_path)
    print(result)

if __name__ == "__main__":
    main()
