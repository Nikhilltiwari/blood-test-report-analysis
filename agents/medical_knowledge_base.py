from crewai import Agent
from transformers import T5ForConditionalGeneration, T5Tokenizer
from utils.data_processor import load_medical_knowledge
from pydantic import Field
import os

class MedicalKnowledgeBase(Agent):
    knowledge_base: dict = Field(default_factory=load_medical_knowledge)
    tokenizer: T5Tokenizer = Field(default_factory=lambda: T5Tokenizer.from_pretrained('t5-small'))
    model: T5ForConditionalGeneration = Field(default_factory=lambda: T5ForConditionalGeneration.from_pretrained('t5-small'))
    role: str = "Medical Knowledge Base"
    goal: str = "Provide medical insights based on analyzed blood test reports"
    backstory: str = "An AI agent trained to offer medical insights and knowledge."

    def __init__(self, **kwargs):
        super().__init__(openai_api_key=os.getenv('OPENAI_API_KEY'), **kwargs)

medical_knowledge_base = MedicalKnowledgeBase()
