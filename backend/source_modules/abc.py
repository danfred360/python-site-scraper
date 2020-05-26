'''
Author: Daniel Frederick
Date: May 26, 2020

abc news site specific web scraper
'''

'''
PASTEBIN

'''

from lxml import html
import requests
import json

    # exports standardized articles from query
    # query - string - search term
class ABCQuery:
    def __init__(self, query):
        self.query = query
        # list of article objects
        self.result_articles = self.getResultArticles()

    def getResultArticles(self):
        query_url_front = 'https://abcnews.go.com/meta/api/search?q='
        query_url_back = '&limit=10&sort=&type=Story&section=&totalrecords=true&offset=0'
        # --- get list of articles
        query_url = str(query_url_front) + str(self.query) + str(query_url_back)
        query_json = requests.get(query_url).content
        # format json so it can be parsed
        query_json = query_json.decode('utf-8')
        # parse json so it can be used as a dictionary
        parsed_query_json = json.loads(query_json)
        # get array of result article objects
        results = parsed_query_json['item']
        articles = []
        # loop through results and pick out articles only, then create an article instance and add it to an array
        for i in results:
            metatags = i
            article = Article(i['link'], metatags)
            articles.append(article)
        return articles
    

    # article class
class Article:
    def __init__(self, url, metatags):
        # dictionary of metatags
        self.metatags = metatags
        self.url = url
        self.title = metatags["title"]
        self.desc = metatags["description"]
        self.date = metatags["pubDate"]
        self.image = metatags["image"]
        self.article_content = self.getArticleContent()

        self.info = 'Source : ABC News\nTitle: {}\nDescription: {}\nDate Published: {}\nURL: {}'.format(self.title, self.desc, self.date, self.url)

    # returns a string of article content
    def getArticleContent(self):
        article_page =  requests.get(self.url)
        article_tree = html.fromstring(article_page.content)

        article_content_p_list = article_tree.xpath('//article[@class="Article__Content story"]//p')
        article_content = '' 
        for i in article_content_p_list:
            article_content = article_content + i.text_content()
        
        return article_content