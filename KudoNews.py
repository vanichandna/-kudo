# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 09:04:46 2020

@author: Vani
"""
#importing libraries
import KudoSpeaks
from selenium import webdriver

#class to open news app
class news_app:
    
    #driver is initiated
    def __init__(self):
        KudoSpeaks.kudo_speaks('Please wait while I retrieve top 5 news for you')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        self.browser = webdriver.Chrome(executable_path=
                                        r"C:\Users\HP\Downloads\chromedriver",
                                        options=chrome_options)
    
    #national news function
    def india_news(self):
        self.browser.get("https://www.thestatesman.com/india")
        self.news_headlines = self.browser.find_elements_by_class_name("card__title")
        self.get_news()
    
    #function to retrieve world news
    def world_news(self):
        self.browser.get("https://in.reuters.com/news/world")
        self.news_headlines = self.browser.find_elements_by_class_name("story-title")
        self.get_news()
    
    #function to retrieve business news
    def business_news(self):
        self.browser.get("https://in.reuters.com/finance")
        self.news_headlines = self.browser.find_elements_by_class_name("story-title")
        self.get_news()

    #function to retrieve market news
    def market_news(self):
        self.browser.get("https://in.reuters.com/finance/markets/india-stock-market")
        self.news_headlines = self.browser.find_elements_by_class_name("story-title")
        self.get_news()
    
    #function to retrieve science news
    def science_news(self):
        self.browser.get("https://in.reuters.com/news/science")
        self.news_headlines = self.browser.find_elements_by_class_name("story-title")
        self.get_news()
    
    #function to retrieve sports news
    def sports_news(self):
        self.browser.get("https://in.reuters.com/news/sports")
        self.news_headlines = self.browser.find_elements_by_class_name("story-title")
        self.get_news()
    
    #function to print news and for kudo to speak news
    def get_news(self):
        headlines = []
        num = 1
        for headline in self.news_headlines:
            headlines.append(headline.text)
            KudoSpeaks.kudo_speaks(str(num) +'. '+ headline.text)
            num = num + 1
            if num==6:
                break
        self.browser.close()