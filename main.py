
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from models.health_assistant import HealthAssistant

def main():
    pdf_path = "C:/Users/nikhl/Downloads/sample report.pdf"
    
    assistant = HealthAssistant()
    result = assistant.process_blood_test(pdf_path)
    if "error" in result:
        print(f"Error processing blood test report: {result['error']}")
    else:
        print(result)

if __name__ == "__main__":
    main()


