from langchain.chains import SequentialChain, LLMChain
from langchain_community.llms import OpenAI, HuggingFaceHub
from agents.blood_test_analyzer import blood_test_analyzer
from agents.medical_knowledge_base import medical_knowledge_base
from agents.web_article_searcher import web_article_searcher
from agents.health_recommendation_generator import health_recommendation_generator

# Initialize models
openai_model = OpenAI(api_key='your-openai-api-key')
huggingface_model = HuggingFaceHub(model_id="t5-small")

# Blood Test Analyzer Chain
blood_test_analyzer_chain = LLMChain(
    llm=blood_test_analyzer,
    prompt="Analyze the blood test report and extract relevant information."
)

# Medical Knowledge Base Chain
medical_knowledge_base_chain = LLMChain(
    llm=medical_knowledge_base,
    prompt="Analyze the abnormalities and identify relevant health conditions."
)

# Web Article Searcher Chain
web_article_searcher_chain = LLMChain(
    llm=web_article_searcher,
    prompt="Search for relevant articles based on the identified health conditions."
)

# Health Recommendation Generator Chain
health_recommendation_generator_chain = LLMChain(
    llm=health_recommendation_generator,
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

