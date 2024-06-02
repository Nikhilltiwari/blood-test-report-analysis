# langchain/chains.py
from langchain.chains import SequentialChain, LLMChain
from langchain_community.llms import OpenAI, HuggingFaceHub
from agents.blood_test_analyzer import BloodTestAnalyzer
from agents.medical_knowledge_base import MedicalKnowledgeBase
from agents.web_article_searcher import WebArticleSearcher
from agents.health_recommendation_generator import HealthRecommendationGenerator

# Initialize models
openai_model = OpenAI(api_key='your-openai-api-key')
huggingface_model = HuggingFaceHub(model_id="t5-small")

# Blood Test Analyzer Chain
blood_test_analyzer_chain = LLMChain(
    llm=BloodTestAnalyzer(),
    prompt="Analyze the blood test report and extract relevant information."
)

# Medical Knowledge Base Chain
medical_knowledge_base_chain = LLMChain(
    llm=MedicalKnowledgeBase(),
    prompt="Analyze the abnormalities and identify relevant health conditions."
)

# Web Article Searcher Chain
web_article_searcher_chain = LLMChain(
    llm=WebArticleSearcher(),
    prompt="Search for relevant articles based on the identified health conditions."
)

# Health Recommendation Generator Chain
health_recommendation_generator_chain = LLMChain(
    llm=HealthRecommendationGenerator(),
    prompt="Generate personalized health recommendations based on the conditions and articles."
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
