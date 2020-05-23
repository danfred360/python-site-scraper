'''
Author: Daniel Frederick
Date: May 21, 2020

fox news site specific web scraper
'''

'''
PASTEBIN

https://api.foxnews.com/search/web?q=trump&siteSearch=foxnews.com&siteSearchFilter=i&callback=__jp1
'''

from lxml import html
import requests
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
        # loop through results and pick out articles only, then create an article instance and add it to an array
        for i in results:
            metatags = i['pagemap']['metatags'][0]
            if i['pagemap']['metatags'][0]['pagetype'] == 'category':
                continue
            else:
                article = Article(i['link'], i['pagemap']['metatags'][0])
                articles.append(article)
        return articles
    

    # article class
class Article:
    def __init__(self, url, metatags):
        self.metatags = metatags
        self.url = url
        self.article_content = self.getArticleContent()

    # returns a string of article content
    def getArticleContent(self):
        article_page =  requests.get(url)
        article_tree = html.fromstring(article_page.content)

        article_content_p_list = article_tree.xpath('//div[@class="article-content"]//p')
        article_content = '' 
        for i in article_content_p_list:
            article_content = article_content + i.text_content()
        
        return article_content



# run stuff ------------------------------------------------------------------------------------------------------------------
print('\n-------------------------------------------------------------------------------------------------------------\n')
temp = Query('trump')
for i in temp.result_articles:
    print(i.metatags['og:title'])
    print('\n')