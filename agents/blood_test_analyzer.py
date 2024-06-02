from crewai import Agent
from utils.parser import parse_blood_test_report
from utils.data_processor import identify_abnormalities
from sklearn.ensemble import IsolationForest
import numpy as np
from pydantic import Field
import os

class BloodTestAnalyzer(Agent):
    model: IsolationForest = Field(default_factory=lambda: IsolationForest(contamination=0.1))
    role: str = "Blood Test Analyzer"
    goal: str = "Analyze blood test reports and identify abnormalities"
    backstory: str = "An AI agent trained to analyze blood test reports and detect anomalies."

    def __init__(self, **kwargs):
        super().__init__(openai_api_key=os.getenv('OPENAI_API_KEY'), **kwargs)
        self.model.fit(self.load_training_data())

    def load_training_data(self):
        # Ensure the training data has the same number of features as the expected input
        return np.array([[15.0, 45.0, 4.5], [14.0, 44.0, 4.6]])

    def parse_blood_test(self, pdf_path):
        return parse_blood_test_report(pdf_path)

    def identify_abnormalities(self, extracted_info):
        # Only consider numeric values
        numeric_values = [value for value in extracted_info.values() if isinstance(value, (int, float))]
        # Ensure the input data has the same number of features as the training data
        if len(numeric_values) != 3:
            raise ValueError(f"Expected 3 features, but got {len(numeric_values)} features.")
        is_anomaly = self.model.predict([numeric_values])[0]
        abnormalities = {}
        if is_anomaly == -1:
            for test, value in extracted_info.items():
                if isinstance(value, (int, float)):
                    abnormalities[test] = 'Anomalous'
        return abnormalities

blood_test_analyzer = BloodTestAnalyzer()
