#from agents.blood_test_analyzer import blood_test_analyzer
from agents.medical_knowledge_base import medical_knowledge_base
from agents.web_article_searcher import web_article_searcher
from agents.health_recommendation_generator import health_recommendation_generator
from langchain.chains import SequentialChain, LLMChain

# Define the LangChain chains
blood_test_analyzer_chain = LLMChain(
    llm=blood_test_analyzer,
    prompt="Analyze the blood test report and extract relevant information."
)

medical_knowledge_base_chain = LLMChain(
    llm=medical_knowledge_base,
    prompt="Analyze the abnormalities and identify relevant health conditions."
)

web_article_searcher_chain = LLMChain(
    llm=web_article_searcher,
    prompt="Search for relevant articles based on the identified health conditions."
)

health_recommendation_generator_chain = LLMChain(
    llm=health_recommendation_generator,
    prompt="Generate personalized health recommendations based on the conditions and articles."
)

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

from langchain.chains import health_assistant_chain

class HealthAssistant:
    def __init__(self):
        self.chain = health_assistant_chain

    def process_blood_test(self, pdf_path):
        # Execute the chain with the given input
        result = self.chain.run({"pdf_path": pdf_path})
        return result
