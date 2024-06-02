# agents/health_recommendation_generator.py
from crewai import Agent

class HealthRecommendationGenerator(Agent):
    def generate_recommendations(self, conditions, articles):
        recommendations = []
        for test, condition in conditions.items():
            rec = f"For {condition}, consider the following:"
            rec += self.extract_advice_from_articles(condition, articles)
            recommendations.append(rec)
        return recommendations

    def extract_advice_from_articles(self, condition, articles):
        advice = ""
        for article in articles:
            if condition in article['title']:
                advice += f"\n- {article['title']}: {article['link']}"
        return advice
