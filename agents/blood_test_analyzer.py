from crewai import Agent
from utilities.parser import parse_blood_test_report
from utilities.data_processor import identify_abnormalities
from sklearn.ensemble import IsolationForest
import numpy as np

class BloodTestAnalyzer(Agent):
    def __init__(self):
        self.model = IsolationForest(contamination=0.1)
        self.model.fit(self.load_training_data())

    def load_training_data(self):
        # Load historical blood test data for training the model
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
