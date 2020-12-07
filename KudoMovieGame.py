# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 21:06:20 2020

@author: HP
"""
#importing libraries
import string
import KudoSpeaks
import random

#module for guess the movie game
class movie_game:
    
    #contains movie database
    def __init__(self):
        self.movies = ['dangal','jungle book','aladdin','manikarnika',
                       'dil bechara', 'harry potter','chhalaang',
                       'the lord of the rings','oceans eleven', 'inception',
                       'veer zaara','lights out','bunty aur bably','joker', 
                       'mardaani','english vinglish','the godfather',
                       'fight club','star wars', 
                       'the good the bad and the ugly','interstellar',
                       'gulabo sitabo', 'chakde india',
                       'sonu ke titu ki sweety']

    #updates movie question by add the letters guessed correctly by the user
    def update_mov(self, letter, movie, enc_movie):
        temp = []
        for i in range(len(movie)):
            if movie[i] == letter:
                temp.append(movie[i])
            else:
                temp.append(enc_movie[i])
        m = ''.join(temp)
        return m

    #selects movie name randomly from the database, encrypts the movie and 
    #allows user to guess the movie letter by letter
    def play_guess_the_movie(self, player_name):
        #all the tried letters are stored
        tried_letters = []*25
        
        #movie is picked randomly from the list of movies[]
        mov = random.choice(self.movies)
        
        #all the letters of the movie are marked by a '*'
        temp = []
        for i in mov:
            if i == ' ':
                temp.append(i)
            else:
                temp.append('*')
        enc_mov = ''.join(temp)
        
        #wrong letters can be attempted at max 5 times
        times = 5
        while  times:
            #checks if all the letters are guessed by the the player
            if mov == enc_mov:
                break
            print (enc_mov)
            KudoSpeaks.kudo_speaks('Guess the letter:')
            
            #input the letter from the player convert it into lowercase
            letter = input()
            if letter not in string.ascii_letters:
                KudoSpeaks.kudo_speaks('Only letters are accepted')
                continue
            letter.lower()
            
            #if letter is not in previously guessed letters and is present
            #in the movie name, then the * are appropriately replaced and 
            #letter is added to the guessed letter list
            if mov.count(letter) and not tried_letters.count(letter):
                KudoSpeaks.kudo_speaks(letter + ' is present.')
                enc_mov = self.update_mov(letter, mov, enc_mov)
                tried_letters.append(letter)
                
            #if the letter is already guessed
            elif tried_letters.count(letter):
                KudoSpeaks.kudo_speaks('Letter already tried, Try another one')
                
            #if the letter is not already guessed and is not present in the 
            #movie name, it is added to the guessed letter list and times is 
            #decremented
            else:
                tried_letters.append(letter)
                times = times - 1
                if times:
                    KudoSpeaks.kudo_speaks('Oops.. Try another letter')
                    KudoSpeaks.kudo_speaks(str(times) + ' incorrect letters are allowed')
        
        #if at the end of the game, movie is not guessed
        if enc_mov != mov:
            KudoSpeaks.kudo_speaks('Movie is ' + mov)
            KudoSpeaks.kudo_speaks('Its ok.. Try another time..')
            
        #if at the end of the game, movie is correctly guessed
        else:
            print(mov)
            KudoSpeaks.kudo_speaks('Congratulations. You won!')
