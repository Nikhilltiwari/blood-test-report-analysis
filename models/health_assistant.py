from agents.blood_test_analyzer import blood_test_analyzer
from agents.medical_knowledge_base import medical_knowledge_base
from agents.web_article_searcher import web_article_searcher
from agents.health_recommendation_generator import health_recommendation_generator

class HealthAssistant:
    def __init__(self):
        self.analyzer = blood_test_analyzer
        self.knowledge_base = medical_knowledge_base
        self.searcher = web_article_searcher
        self.generator = health_recommendation_generator

    def process_blood_test(self, pdf_path):
        # Step 1: Analyze the blood test report
        extracted_info = self.analyzer.parse_blood_test(pdf_path)
        abnormalities = self.analyzer.identify_abnormalities(extracted_info)

        # Step 2: Identify health conditions
        conditions = self.knowledge_base.analyze_conditions(abnormalities)

        # Step 3: Search for relevant articles
        articles = self.searcher.search_articles(conditions)

        # Step 4: Generate health recommendations
        recommendations = self.generator.generate_recommendations(conditions, articles)
        
        return {
            "summary": extracted_info,
            "abnormalities": abnormalities,
            "conditions": conditions,
            "articles": articles,
            "recommendations": recommendations
        }
