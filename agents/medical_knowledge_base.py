# agents/medical_knowledge_base.py
from crewai import Agent

class MedicalKnowledgeBase(Agent):
    def __init__(self):
        self.knowledge_base = self.load_medical_knowledge()

    def load_medical_knowledge(self):
        return {
            'Hemoglobin': {'low': 'Anemia', 'high': 'Polycythemia'},
            'Packed Cell Volume (PCV)': {'low': 'Anemia', 'high': 'Polycythemia'},
            'RBC Count': {'low': 'Anemia', 'high': 'Polycythemia'},
            # Add other conditions as needed
        }

    def analyze_conditions(self, abnormalities):
        conditions = {}
        for test, status in abnormalities.items():
            condition = self.knowledge_base.get(test, {}).get(status, 'Unknown condition')
            conditions[test] = condition
        return conditions
