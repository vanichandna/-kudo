# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 10:14:58 2020

@author: Vani
"""
#imports all the libraries
import KudoSpeaks
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#class which contains all the web browser related apps
class browser_app:
    #initialize chrome webdriver
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("excludeSwitches", 
                                               ['enable-automation'])
        
        self.browser = webdriver.Chrome(executable_path=
                                        r"C:\Users\HP\Downloads\chromedriver", 
                                        options=chrome_options)
    
    #whatsapp automation
    def send_whatsapp(self, contact, msg):
        #web whatsapp is opened
        self.browser.get("https://web.whatsapp.com")
        
        #user is requested to scan QR code for login
        KudoSpeaks.kudo_speaks("Scan QR code and press ENTER")
        ch = input()
        
        #user is found and clicked
        selected_contact = WebDriverWait(self.browser,600).until(
            EC.element_to_be_clickable((
                By.XPATH, "//span[@title='"+contact+"']"))).click()
        
        #text box is selected and message is sent
        text_box = self.browser.find_element_by_xpath(
            '//*[@class="_2HE1Z _1hRBM focused"]')
        text_box.send_keys(msg + Keys.ENTER)
       
    #leads to playing song
    def play_song (self, song_name):
        #google is started
        self.browser.get("https://www.google.com")
        
        #song is searched
        search_song = self.browser.find_element_by_name("q").send_keys(
            song_name + ' song' + Keys.ENTER)
        
        #first link to autoplay the song is clicked
        find_song = WebDriverWait(self.browser, 600).until(
            EC.element_to_be_clickable((By.CLASS_NAME,"ellip")))
        find_song.click()
        time.sleep(3)
        self.browser.refresh()
    
    #leads to movies
    def play_movie(self, movie_name):
        #start google
        self.browser.get("https://www.google.com")
        
        #movie name is entered in search box and movie is searched
        search_movie = self.browser.find_element_by_name("q").send_keys(
            'watch ' + movie_name + Keys.ENTER)
        
        #first link to the movie is opened
        find_movie = self.browser.find_element_by_class_name("JkUS4b")
        find_movie.click()
       
    #closes the browser
    def close_browser(self):
        try:
            KudoSpeaks.kudo_speaks('Closing the browser')
            self.browser.close()
        except :
            KudoSpeaks.kudo_speaks("Browser already closed")


    
#leads to current weather update on google
  
class weather_forecast:
    #initialize chrome webdriver
    def __init__(self):
        KudoSpeaks.kudo_speaks('Please wait while I gather local weather information for you')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        self.browser = webdriver.Chrome(executable_path= 
                                        r"C:\Users\HP\Downloads\chromedriver", 
                                        options=chrome_options)
        
        #starts google
        self.browser.get("https://www.google.com")
        
        #enters keywords to search
        search = self.browser.find_element_by_name("q").send_keys(
                                            'weather forecast'
                                            + Keys.ENTER)
        
        #scrapes the necessary information and speaks
        temp = self.browser.find_element_by_xpath(
            './/span[@class="wob_t TVtOme"]').text
        
        KudoSpeaks.kudo_speaks('Temperature is '+temp+' degree Celsius')

        ppt = self.browser.find_element_by_xpath('.//span[@id="wob_pp"]').text
        KudoSpeaks.kudo_speaks('Precipitation is ' + ppt)

        humidity = self.browser.find_element_by_xpath(
            './/span[@id="wob_hm"]').text
        KudoSpeaks.kudo_speaks('Humidity is ' + humidity)        

        wind = self.browser.find_element_by_xpath('.//span[@id="wob_ws"]').text
        KudoSpeaks.kudo_speaks('Wind Speed is ' + wind)
        
        #if precipitation is more than 90%
        ppt = ppt[:-1]
        ppt = int(ppt)
        if ppt >= 90:
            KudoSpeaks.kudo_speaks('It is raining. Keep dry.')
            
        #if temperature is more than 35 degree celsium
        elif int(temp)>35:
            KudoSpeaks.kudo_speaks('Its too hot outside. Stay indoors.')
        
        #close browser
        self.browser.close()