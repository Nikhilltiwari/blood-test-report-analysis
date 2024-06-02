from crewai import Agent
from transformers import T5ForConditionalGeneration, T5Tokenizer
from utilities.data_processor import load_medical_knowledge

class MedicalKnowledgeBase(Agent):
    def __init__(self):
        self.knowledge_base = load_medical_knowledge()
        self.tokenizer = T5Tokenizer.from_pretrained('t5-small')
        self.model = T5ForConditionalGeneration.from_pretrained('t5-small')

    def analyze_conditions(self, abnormalities):
        conditions = {}
        for test, status in abnormalities.items():
            condition = self.knowledge_base.get(test, {}).get(status, 'Unknown condition')
            conditions[test] = condition
        return conditions

    def extract_information(self, text, question):
        input_text = f'question: {question} context: {text}'
        input_ids = self.tokenizer.encode(input_text, return_tensors='pt')
        outputs = self.model.generate(input_ids)
        answer = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return answer

medical_knowledge_base = MedicalKnowledgeBase()

