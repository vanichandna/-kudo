# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 19:22:24 2020

@author: HP
"""
from gtts import gTTS
import os
import playsound

#class which speaks
class kudo_speaks:
    
    def __init__(self, text_to_speak):
        #converts text to speech and stores in mp3 file
        myobj = gTTS(text=text_to_speak, lang='en')
        myobj.save("abc.mp3")
        
        #prints text
        print('Kudo :',text_to_speak)
        
        #playbacks recorded speech
        playsound.playsound("abc.mp3", True)
        
        #deletes mp3 file
        os.remove("abc.mp3")
        