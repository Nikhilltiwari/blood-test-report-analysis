from crewai import Agent
from utilities.data_processor import generate_recommendations
from transformers import T5ForConditionalGeneration, T5Tokenizer

class HealthRecommendationGenerator(Agent):
    def __init__(self):
        self.tokenizer = T5Tokenizer.from_pretrained('t5-small')
        self.model = T5ForConditionalGeneration.from_pretrained('t5-small')

    def generate_recommendations(self, conditions, articles):
        recommendations = generate_recommendations(conditions, articles)
        for rec in recommendations:
            rec['summary'] = self.summarize_recommendation(rec['details'])
        return recommendations

    def summarize_recommendation(self, content):
        input_text = f'summarize: {content}'
        input_ids = self.tokenizer.encode(input_text, return_tensors='pt', max_length=512, truncation=True)
        outputs = self.model.generate(input_ids, max_length=150, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)
        summary = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return summary

health_recommendation_generator = HealthRecommendationGenerator()

