import requests
from bs4 import BeautifulSoup

def search_articles(condition):
    search_query = f"{condition} health tips"
    url = f"https://www.google.com/search?q={search_query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    articles = []
    for item in soup.select('.BVG0Nb'):
        title = item.get_text()
        link = item.find('a')['href']
        articles.append({"title": title, "link": link})
    
    return articles
