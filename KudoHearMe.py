# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 11:24:27 2020

@author: Vani
"""
#importing libraries
import KudoSpeaks
import speech_recognition as sr

#speech recognition class
class hear_me:
    
    #initialize recognizer
    def __init__(self):
        self.r = sr.Recognizer()

    #records voice and converts to text and sends the text  
    def hear_me(self, user_name):
        speak = input('Press Enter to speak')
        
        #takes input from mic
        with sr.Microphone() as source:
            audio = self.r.listen(source)
        try:
            #converts speech to text
            speech = self.r.recognize_google(audio)
            print(user_name, ":", speech)
        except LookupError:
            KudoSpeaks.kudo_speaks("could not understand audio")
            return 0
        except sr.UnknownValueError:
            KudoSpeaks.kudo_speaks("couldnt find matching word")
            return 0
        except sr.RequestError:
            KudoSpeaks.kudo_speaks("Unable to generate text from audio")
            return 0
        except UnboundLocalError:
            KudoSpeaks.kudo_speaks("Unable to understand, try again")
            return 0
        return speech