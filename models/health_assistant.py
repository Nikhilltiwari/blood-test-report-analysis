# models/health_assistant.py
from agents.blood_test_analyzer import BloodTestAnalyzer
from agents.medical_knowledge_base import MedicalKnowledgeBase
from agents.web_article_searcher import WebArticleSearcher
from agents.health_recommendation_generator import HealthRecommendationGenerator

class HealthAssistant:
    def __init__(self):
        self.analyzer = BloodTestAnalyzer()
        self.knowledge_base = MedicalKnowledgeBase()
        self.searcher = WebArticleSearcher()
        self.generator = HealthRecommendationGenerator()

    def process_blood_test(self, blood_test_report):
        # Step 1: Analyze the blood test report
        extracted_info = self.analyzer.parse_blood_test(blood_test_report)
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
