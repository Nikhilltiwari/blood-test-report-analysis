# agents/blood_test_analyzer.py
from crewai import Agent
from utils.parser import parse_blood_test_report
from sklearn.ensemble import IsolationForest

class BloodTestAnalyzer(Agent):
    role: str = "Blood Test Analyzer"
    goal: str = "Analyze blood test reports and identify abnormalities"
    backstory: str = "You are a highly skilled medical analyzer designed to interpret blood test reports."

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        object.__setattr__(self, 'model', IsolationForest(contamination=0.1))

    def parse_blood_test(self, pdf_path):
        extracted_info, numeric_values = parse_blood_test_report(pdf_path)
        return extracted_info, numeric_values

    def identify_abnormalities(self, extracted_info):
        numeric_values = list(extracted_info.values())
        if len(numeric_values) < 3:
            raise ValueError(f"Expected at least 3 features, but got {len(numeric_values)} features.")
        is_anomaly = self.model.predict([numeric_values])[0]
        return {"is_anomaly": is_anomaly}

blood_test_analyzer = BloodTestAnalyzer()

if __name__ == "__main__":
    pdf_path = "C:/Users/nikhl/Downloads/sample report.pdf" 
    extracted_info, numeric_values = blood_test_analyzer.parse_blood_test(pdf_path)
    print("Extracted Info:", extracted_info)
    print("Numeric Values:", numeric_values)





