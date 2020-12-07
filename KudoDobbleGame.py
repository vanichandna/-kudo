# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 21:14:10 2020

@author: HP
"""
import KudoSpeaks
import string
import random

#module to play dobble game
class dobble_game:
    #initializes symbols to be used in the game
    def __init__(self):
        self.symbols = list(string.punctuation)

    #function randomizes the symbols such that 2 cards contain exactly 1 
    #common symbol
    def play_game(self):
        card1 = [0] * 5
        card2 = [0] * 5
        pos1 = random.randint(0, 4)
        pos2 = random.randint(0, 4)
        
        #if two positions are same
        if pos1 == pos2:
            card1[pos1] = random.choice(self.symbols)
            card2[pos1] = card1[pos1]
            self.symbols.remove(card1[pos1])
            
        #if 2 positions are different
        else:
            card1[pos1] = random.choice(self.symbols)
            card2[pos2] = card1[pos1]
            #removes already retrieved symbol from the list
            self.symbols.remove(card1[pos1])
            #adding other symbols on the 2 positions left respectively on the 
            #2 cards
            card1[pos2] = random.choice(self.symbols)
            self.symbols.remove(card1[pos2])
            card2[pos1] = random.choice(self.symbols)
            self.symbols.remove(card2[pos1])
            
        #remaining positions are filled in the cards and respective symbols 
        #are subsequently removed from the list to avoid repetition
        i = 0
        while i < 5:
            if i != pos1 and i != pos2:
                card1[i] = random.choice(self.symbols)
                self.symbols.remove(card1[i])
                card2[i] = random.choice(self.symbols)
                self.symbols.remove(card2[i])
            i = i + 1

        #display the cards
        print(card1)
        print(card2)

        ch = input("find same symbol: ")
        #if the symbol inputted matches the common symbol
        if ch == card1[pos1]:
            KudoSpeaks.kudo_speaks("Congratulations.. u won")
        else:
            KudoSpeaks.kudo_speaks("Oops.. try again")
            KudoSpeaks.kudo_speaks('The common symbol is ' + card1[pos1])
            
