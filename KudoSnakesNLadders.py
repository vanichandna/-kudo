# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 21:15:31 2020

@author: HP
"""
import KudoSpeaks
import random
import KudoHearMe

#snakes and ladders game
class snakes_n_ladders:

    #checks for snake at every move
    def check_snake(self, score):
        switcher = {
            34 : 1,
            25 : 5,
            47 : 19,
            87 : 57,
            99 : 69,
            65 : 52,
            91 : 61
                }
        if (score == 34 or score == 25 or score == 47 or score == 87 or score == 99
            or score == 65 or score == 91):
            KudoSpeaks.kudo_speaks('OOps snake just bit!')
        return switcher.get(score, score)

    #checks for ladder at every move
    def check_ladder(self, score):
        switcher = {
            3 : 51,
            6 : 27,
            20 : 70,
            36 : 55,
            68 : 98,
            63 : 95,
                }
        if (score == 3 or score == 6 or score == 20 or score == 36 or score == 68
            or score == 63):
            KudoSpeaks.kudo_speaks('Its a ladder!')
        return switcher.get(score, score)

    #shows score of both players
    def show_score(self, p1_name, p2_name, p1_score, p2_score):
        KudoSpeaks.kudo_speaks(p1_name + ' score is ' + str(p1_score))
        KudoSpeaks.kudo_speaks(p2_name + ' score is ' + str(p2_score))
        
    #function to play snakes and ladders game
    def play_snakes_n_ladders(self, user_name):
        #initializations
        p1_name = "Your"
        p2_name = 'My'
        p1_score = 0
        p2_score = 0
        score = p1_score
        turn  = 0
        
        #if turn == 0, it is player's turn, if turn ==1, it is computer's turn
        while 1:
            if turn == 1:
                score = p2_score
                KudoSpeaks.kudo_speaks('Its my turn')
            else:
                score = p1_score                
                KudoSpeaks.kudo_speaks(user_name + ', Its your turn')
                
            #player is given a choice to quit game in between
            if turn == 0:
                KudoSpeaks.kudo_speaks(
                    'Say YES to continue, else say NO to exit the game ')
                cont = KudoHearMe.hear_me().hear_me(user_name)
                if cont == 'no' or cont=='No' or cont=='NO':
                    break
                
            #dice is rolled
            dice = random.randint(1, 6)
            KudoSpeaks.kudo_speaks('Dice rolls to ' + str(dice))
            
            #score is updated 
            score = score + dice
            if score >= 100:
                score = 100
            if turn == 0:
                p1_score = score
            else:
                p2_score = score
                
            #if dice is 6, user gets another chance to roll the dice
            if (dice == 6):
                if turn==1:
                    KudoSpeaks.kudo_speaks('Yayyy..Dice rolled to 6.. I get another chance!')
                else:
                    KudoSpeaks.kudo_speaks('Yayyy..Dice rolled to 6.. You get another chance!')
                continue
            
            #snake and ladder is checked at every roll finish
            score = self.check_snake(score)
            score = self.check_ladder(score)
            if turn == 0:
                p1_score = score
            else:
                p2_score = score
            
            #if anyone reached 100 score, he wins
            if p1_score == 100:
                self.show_score(p1_name, p2_name, p1_score, p2_score)
                KudoSpeaks.kudo_speaks('Congrats ' + user_name + ' You won!')
                break
            if p2_score == 100:
                self.show_score(p1_name, p2_name, p1_score, p2_score)
                KudoSpeaks.kudo_speaks('I won')
                KudoSpeaks.kudo_speaks('Better luck next time')
                break
            self.show_score(p1_name, p2_name, p1_score, p2_score)
            turn = (turn + 1) % 2
        KudoSpeaks.kudo_speaks('It was great playing with you.')
