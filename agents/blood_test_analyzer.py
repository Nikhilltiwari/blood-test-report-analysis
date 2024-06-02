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
        return np.array([[15.0, 45.0, 4.5], [14.0, 44.0, 4.6]])

    def parse_blood_test(self, pdf_path):
        return parse_blood_test_report(pdf_path)

    def identify_abnormalities(self, extracted_info):
        values = list(extracted_info.values())
        is_anomaly = self.model.predict([values])[0]
        abnormalities = {}
        if is_anomaly == -1:
            for test, value in extracted_info.items():
                abnormalities[test] = 'Anomalous'
        return abnormalities

blood_test_analyzer = BloodTestAnalyzer()

