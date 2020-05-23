import requests
from lxml import html

url = 'https://www.foxnews.com/politics/trump-announces-that-houses-of-worship-are-essential-calls-on-governors-to-open-them-up'

class Article:
    def __init__(self, url):
        article_page =  requests.get(url)
        article_tree = html.fromstring(article_page.content)

        article_content_p_list = article_tree.xpath('//div[@class="article-content"]//p')
        article_content = '' 
        for i in article_content_p_list:
            article_content = article_content + i.text_content()
        print(article_content)


temp = Article(url)