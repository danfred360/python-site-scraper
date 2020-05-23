'''
Author: Daniel Frederick
Date: May 21, 2020

fox news site specific web scraper - beautifulsoup 4 instead of lxml
'''

'''
PASTEBIN

https://api.foxnews.com/search/web?q=trump&siteSearch=foxnews.com&siteSearchFilter=i&callback=__jp1
'''

from lxml import html
from bs4 import BeautifulSoup
import requests
import os
import datetime
import json

url = 'https://www.foxnews.com/'

    # exports standardized articles from query
    # query - string - search term
class Query:
    def __init__(self, query):
        self.query = query
        self.query_url_front = 'https://api.foxnews.com/search/web?q='
        self.query_url_back = '&siteSearch=foxnews.com&siteSearchFilter=i&callback=__jp1'

        self.result_articles = self.getResultArticles()

    def getResultArticles(self):
        # --- get list of articles
        query_url = str(self.query_url_front) + str(self.query) + str(self.query_url_back)
        query_json = requests.get(query_url).content
        # format json so it can be parsed
        query_json = query_json.decode('utf-8')[22:-3]
        # parse json so it can be used as a dictionary
        parsed_query_json = json.loads(query_json)
        # get array of result article objects
        results = parsed_query_json['items']
        articles = []

        for i in results:
            metatags = i['pagemap']['metatags'][0]
            print(metatags['pagetype'])
            if i['pagemap']['metatags'][0]['pagetype'] == 'category':
                continue
            else:
                article = Article(i['link'], i['pagemap']['metatags'])
                articles.append(article)
        return articles
    

class Article:
    def __init__(self, url, metatags):
        pass

# run stuff ------------------------------------------------------------------------------------------------------------------
print('\n-------------------------------------------------------------------------------------------------------------\n')
temp = Query('trump')
print(len(temp.result_articles))