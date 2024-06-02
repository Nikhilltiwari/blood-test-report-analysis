from crewai import Agent
from utilities.web_scraper import search_articles
from transformers import T5ForConditionalGeneration, T5Tokenizer

class WebArticleSearcher(Agent):
    def __init__(self):
        self.tokenizer = T5Tokenizer.from_pretrained('t5-small')
        self.model = T5ForConditionalGeneration.from_pretrained('t5-small')

    def search_articles(self, conditions):
        articles = []
        for condition in conditions.values():
            search_results = search_articles(condition)
            for article in search_results:
                article['summary'] = self.summarize_article(article['content'])
            articles.extend(search_results)
        return articles

    def summarize_article(self, content):
        input_text = f'summarize: {content}'
        input_ids = self.tokenizer.encode(input_text, return_tensors='pt', max_length=512, truncation=True)
        outputs = self.model.generate(input_ids, max_length=150, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)
        summary = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return summary

web_article_searcher = WebArticleSearcher()
