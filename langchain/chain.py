# langchain/chains.py
from langchain import Chain, SequentialChain
from langchain.llms import OpenAI, HuggingFaceHub
from agents.blood_test_analyzer import BloodTestAnalyzer
from agents.medical_knowledge_base import MedicalKnowledgeBase
from agents.web_article_searcher import WebArticleSearcher
from agents.health_recommendation_generator import HealthRecommendationGenerator

# Initialize models
openai_model = OpenAI(api_key='your-openai-api-key')
huggingface_model = HuggingFaceHub(model_id="t5-small")

# Blood Test Analyzer Chain
blood_test_analyzer_chain = Chain(
    name="BloodTestAnalyzerChain",
    input_keys=["pdf_path"],
    output_keys=["extracted_info"],
    executor=BloodTestAnalyzer().parse_blood_test
)

# Medical Knowledge Base Chain
medical_knowledge_base_chain = Chain(
    name="MedicalKnowledgeBaseChain",
    input_keys=["abnormalities"],
    output_keys=["conditions"],
    executor=MedicalKnowledgeBase().analyze_conditions
)

# Web Article Searcher Chain
web_article_searcher_chain = Chain(
    name="WebArticleSearcherChain",
    input_keys=["conditions"],
    output_keys=["articles"],
    executor=WebArticleSearcher().search_articles
)

# Health Recommendation Generator Chain
health_recommendation_generator_chain = Chain(
    name="HealthRecommendationGeneratorChain",
    input_keys=["conditions", "articles"],
    output_keys=["recommendations"],
    executor=HealthRecommendationGenerator().generate_recommendations
)

# Sequential Chain for the entire workflow
health_assistant_chain = SequentialChain(
    chains=[
        blood_test_analyzer_chain,
        medical_knowledge_base_chain,
        web_article_searcher_chain,
        health_recommendation_generator_chain
    ],
    input_keys=["pdf_path"],
    output_keys=["recommendations"]
)
