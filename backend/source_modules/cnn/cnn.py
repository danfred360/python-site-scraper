'''
Author: Daniel Frederick
Date: May 21, 2020

cnn site specific web scraper
'''

'''
PASTEBIN

print('\nGetting site code from ' + url + ' ...')
        self.page = requests.get(url)
        self.tree = html.fromstring(self.page.content)

# returns array of titles
    def titles(self):
        print('Scraping titles ... ')
        return self.tree.xpath('//div[@class="wd_title"]/a/text()')

'''

from lxml import html
import requests
import os
import datetime

url = 'https://www.cnn.com/'
query_url = 'https://www.cnn.com/search?q='

    # query - string - search term
    # results - int - number of results desired - default five results
class CNN:
    def __init__(self, query, results=5):
        self.query = query
        self.results = results

        # query cnn's site
        print('Querying CNN\'s site \nQuery -> ' + self.query + '\nNumber of results desired -> ' + str(results) + '\n') #---

        # get list of articles
        results_url = str(query_url) + str(self.query)
        
        self.results_page = requests.get(results_url)
        self.results_tree = html.fromstring(self.results_page.content)

        # get array of result article urls
        '''
        self.result_article_urls = self.results_tree.xpath(
            '/div[@class="cnn-search__results-list"]//div'
            )
        '''
        self.result_article_urls = self.results_tree.xpath('//div/text()')

    
    # scrapes article and returns content
    # article_url - string - url of article to scrape
    def scrapeArticle(self, article_url):
        pass

# run stuff ------------------------------------------------------------------------------------------------------------------
print('\n-------------------------------------------------------------------------------------------------------------\n')
temp = CNN('trump')
print('result urls -> ')
print(temp.result_article_urls)