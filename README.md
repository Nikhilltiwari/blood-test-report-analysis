##        Blood Test Report Analysis
Overview
This project analyzes blood test reports, summarizes the results, finds relevant health articles based on the analysis, and provides health recommendations. The system processes a sample blood test report, extracts relevant information, searches the web for articles tailored to the person's health needs, and offers health recommendations.

## Approach
1. Text Extraction:
      Used the PyMuPDF library to extract text from the PDF blood test report.
      Parsed the extracted text to identify key health metrics.
   
2 .Health Analysis:
      Developed a BloodTestAnalyzer class to process and analyze the extracted metrics.
      Implemented methods to identify abnormalities and summarize the report.
      
3. Article Search:
      Integrated OpenAI's API to search for health-related articles based on the identified health needs.
   
5. Health Recommendations:
     Provided health recommendations and links to relevant articles based on the analysis.

   
## Prerequisites
Python 3.7 or higher
Virtual environment (optional but recommended)


## Installation
1.  Clone the repository:
      git clone https://github.com/your-username/blood-test-report-analysis.git
      cd blood-test-report-analysis

2.  Create and activate a virtual environment (optional):
      python -m venv venv
      source venv/bin/activate
    
3. Install dependencies:
      pip install -r requirements.txt

4. Set up environment variables:
     Create a .env file in the root directory of your project.
     Add your OpenAI API key to the .env file:

     OPENAI_API_KEY=your_openai_api_key_here

   
##  How to Run
1.Ensure the .env file is correctly set up with your OpenAI API key.
2.Place the sample PDF report you want to analyze in a known location (e.g., C:/Users/nikhl/Downloads/sample report.pdf).
3.Run the script:
python main.py


 ## File Structure
# main.py: Entry point for running the analysis.
# models/health_assistant.py: Contains the HealthAssistant class to manage the overall analysis process.
# agents/blood_test_analyzer.py: Contains the BloodTestAnalyzer class to process and analyze blood test reports.
# utils/parser.py: Utility functions for parsing the text from PDF reports.
# .env: Environment file containing the OpenAI API key.
Example Usage

# Navigate to the project directory
cd blood-test-report-analysis

# Run the analysis
python main.py
After running the script, the system will process the provided PDF report, summarize the blood test results, search for relevant health articles, and provide health recommendations.

