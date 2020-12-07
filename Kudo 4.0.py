# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 19:22:48 2020

@author: Vani
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 08:31:50 2020

@author: Vani
"""

#imports all the files to be used
import KudoSpeaks
import KudoWebAutomation
import KudoHearMe
import KudoMovieGame
import KudoDobbleGame
import KudoSnakesNLadders
import KudoApps
import KudoNews
import pyjokes

#Kudo says welcome message
welcome_msg = 'Hi.. I am  Kudo.. What is your name?'
KudoSpeaks.kudo_speaks(welcome_msg)

#stores the user_name
user_name = 'User'

#inputs user's name
while 1:
    instruction = KudoHearMe.hear_me()
    instr_sentence = instruction.hear_me(user_name)
    if not instr_sentence:
        KudoSpeaks.kudo_speaks('Please try again')
        continue
    else:
        user_name = instr_sentence
        welcome_msg = 'Hello ' + instr_sentence
        KudoSpeaks.kudo_speaks(welcome_msg)
        break

while 1:
    #inputs speech of user and stores as text in instr_sentence
    instruction = KudoHearMe.hear_me()
    instr_sentence = instruction.hear_me(user_name)
    
    #if user doesn't speak, instr_sentence is empty resulting in following
    #code execution
    if not instr_sentence:
        KudoSpeaks.kudo_speaks("Please try again")
        KudoSpeaks.kudo_speaks('Here are all the things you can do:')
        KudoSpeaks.kudo_speaks('1. Check current weather conditions')
        KudoSpeaks.kudo_speaks('2. Play Games')
        KudoSpeaks.kudo_speaks('3. Listen to songs')
        KudoSpeaks.kudo_speaks('4. Watch movies')
        KudoSpeaks.kudo_speaks('5. Open Applications')
        KudoSpeaks.kudo_speaks('6. Send Whatsapp message')
        KudoSpeaks.kudo_speaks('7. Listen to News')
        KudoSpeaks.kudo_speaks('8. Hear a joke')
        KudoSpeaks.kudo_speaks('If you want to exit, say GoodBye')
        continue
    
    #Kudo responds to 'How are you?'
    elif "how are you" in instr_sentence.lower():
        KudoSpeaks.kudo_speaks("I am fine.. How are you?")
        
    #Kudo retrieves local weather conditions
    elif "weather" in instr_sentence.lower():
        open_app = KudoWebAutomation.weather_forecast()
        
    # 3 minigames
    elif "game" in instr_sentence.lower():
        KudoSpeaks.kudo_speaks(
            'I have following games..Which game would you like to play?')
        KudoSpeaks.kudo_speaks('1. Dobble Game')
        KudoSpeaks.kudo_speaks('2. Guess the movie')
        KudoSpeaks.kudo_speaks('3. Snakes & Ladders')
        game = KudoHearMe.hear_me()
        while 1:
            game_sentence = game.hear_me(user_name)
            
            #if user doesnt respond, name of the game is asked again
            if not game_sentence:
                KudoSpeaks.kudo_speaks('Try telling the game again')
                continue
            
            #Dobble game
            elif "dobble" in game_sentence.lower():
                KudoSpeaks.kudo_speaks('Lets play Dobble game')
                KudoSpeaks.kudo_speaks('You need to find same symbol from amongst 2 cards')
                playgame = KudoDobbleGame.dobble_game()
                playgame.play_game()
                
            #Movie Game
            elif "movie" in game_sentence.lower():
                KudoSpeaks.kudo_speaks('Lets play Guess the movie')
                KudoSpeaks.kudo_speaks('You need to guess a letter from English alphabet. ' 
                        + 'If the letter is present in the name of the movie, '
                        + 'it will be shown. You get 5 chances to enter an '
                        + 'invalid letter')
                playgame = KudoMovieGame.movie_game()
                playgame.play_guess_the_movie(user_name)
                
            #Snakes and Ladders Game
            elif game_sentence.find("Snakes") != -1 or game_sentence.find(
                "snakes") != -1:
                KudoSpeaks.kudo_speaks('Lets play Snakes and Ladders')
                playgame = KudoSnakesNLadders.snakes_n_ladders()
                playgame.play_snakes_n_ladders(user_name)
                
            #if the speech of user is not clear
            else :
                KudoSpeaks.kudo_speaks("Try telling the game again")
                continue
            
            #Checks if user wants to play another game
            KudoSpeaks.kudo_speaks('Do you want to play another game?')
            game_sentence = game.hear_me(user_name)
            
            #if user doesnt speak
            if not game_sentence:
                KudoSpeaks.kudo_speaks('Moving out of Game Zone')
                break
            
            #if user doesnt want to play another game
            elif "no" in game_sentence.lower():
                KudoSpeaks.kudo_speaks('Moving out of Game Zone')
                break
            
            #if user wants to play another game
            elif "yes" in game_sentence.lower():
                KudoSpeaks.kudo_speaks('Which game would you like to play?')
                KudoSpeaks.kudo_speaks('1. Dobble Game')
                KudoSpeaks.kudo_speaks('2. Guess the movie')
                KudoSpeaks.kudo_speaks('3. Snakes & Ladders')
                
    #user wants to listen to songs
    elif "music" in instr_sentence.lower() or "song" in instr_sentence.lower():
        KudoSpeaks.kudo_speaks("Which song do you want me to play?")
        song = KudoHearMe.hear_me()
        song_name = song.hear_me(user_name)
        
        #if user doesnt tell the song
        while not song_name:
            KudoSpeaks.kudo_speaks('Please tell the song name again')
            song_name = song.hear_me(user_name)
        
        #song is played
        open_app = KudoWebAutomation.browser_app()
        open_app.play_song(song_name)
        
        #close the browser
        KudoSpeaks.kudo_speaks('Say CLOSE to close the browser')
        song_name = str(song.hear_me(user_name))
        while not "close" in song_name.lower():
            KudoSpeaks.kudo_speaks('Couldnt understand. Pls say close to close the browser')
            song_name = song.hear_me(user_name)
        open_app.close_browser()
        
    #user wants to send message via whatsapp
    elif "whatsapp" in instr_sentence.lower() or "message" in instr_sentence.lower():
        #inputs recipient name, confirms it and stores in contact variable
        KudoSpeaks.kudo_speaks('Tell Recipient Name')
        hm = KudoHearMe.hear_me()
        contact = hm.hear_me(user_name)
        while 1:
            KudoSpeaks.kudo_speaks('If the recipient name is correct, say yes, else say no')
            hm_hm = hm.hear_me(user_name)
            if "yes" in hm_hm.lower():
                break
            KudoSpeaks.kudo_speaks('Tell Recipient Name')
            hm = KudoHearMe.hear_me()
            contact = hm.hear_me(user_name)
        contact = contact.capitalize()
        
        #inputs message
        KudoSpeaks.kudo_speaks('Tell the message')
        msg = hm.hear_me(user_name)        
        
        #app is opened and message is sent
        open_app = KudoWebAutomation.browser_app()
        open_app.send_whatsapp(contact, msg)
        
        #user is asked if he wants to close the browser
        KudoSpeaks.kudo_speaks('Say CLOSE to close the browser')
        hm_hm = hm.hear_me(user_name)
        while hm_hm.find("close") == -1:
            hm_hm = hm.hear_me(user_name)
        open_app.close_browser()
        
    #user wants to watch movie
    elif "movie" in instr_sentence.lower():
        #inputs movie name
        KudoSpeaks.kudo_speaks("Which movie you want to watch?")
        movie = KudoHearMe.hear_me()
        movie_name = movie.hear_me(user_name)
        
        #starts movie
        open_app = KudoWebAutomation.browser_app()
        open_app.play_movie(movie_name)
        
        #user is asked if he wants to close the browser
        KudoSpeaks.kudo_speaks('Say CLOSE to close the browser')
        movie_name = str(movie.hear_me(user_name))
        while not "close" in movie_name.lower():
            KudoSpeaks.kudo_speaks('Couldnt understand. Pls say close to close the browser')
            movie_name = movie.hear_me(user_name)
        open_app.close_browser()
    
    #exit Kudo
    elif "goodbye" in instr_sentence.lower() or "bye" in instr_sentence.lower():
        #exit Kudo
        KudoSpeaks.kudo_speaks('Have a nice day..Goodbye..')
        break
    
    #opens windows applications
    elif "open" in instr_sentence.lower() or "application" in instr_sentence.lower():
        #lists out various apps it can open
        app = KudoApps.apps_container()
        KudoSpeaks.kudo_speaks("To open notepad, say notepad. To open calculator, say "
                    + "calculator. To open MS Paint, say paint. To open MS "
                    + "Word, say word. "
                    + "To open MS Excel, say Excel. To open MS Powerpoint, "
                    + "say Powerpoint.")
        
        #user says choice
        hm = KudoHearMe.hear_me()
        app_name = hm.hear_me(user_name)
        
        #when user did not speak
        while not app_name:
            KudoSpeaks.kudo_speaks('I did not understand. Please say again')
            app_name = hm.hear_me(user_name)

        #opens notepad
        if "notepad" in app_name.lower():
            app.notepad_app()
            
        #opens MS Excel
        elif "excel" in app_name.lower():
            app.excel_app()
            
        #opens calculator
        elif "calculator" in app_name.lower():
            app.calc_app()
            
        #opens MS paint
        elif "paint" in app_name.lower():
            app.paint_app()
            
        #opens MS word
        elif "word" in app_name.lower():
            app.word_app()
            
        #opens MS powerpoint
        elif "powerpoint" in app_name.lower():
            app.ppt_app()
            
        #if the app name is not in the list
        else:
            KudoSpeaks.kudo_speaks("I cannot open " + app_name)
            
    #tells a boring joke
    elif "joke" in instr_sentence.lower():
        while 1:
            KudoSpeaks.kudo_speaks(pyjokes.get_joke())
            KudoSpeaks.kudo_speaks('Do you want to hear another one?')
            instr_sentence = instruction.hear_me(user_name)
            if "no" in instr_sentence.lower():
                break
            
    #tells interesting news
    elif "news" in instr_sentence.lower():
        while 1:
            KudoSpeaks.kudo_speaks('Which news do you want to hear?')
            KudoSpeaks.kudo_speaks('For national news, say INDIA. For international news,'
                       + ' say WORLD. For business news, say BUSINESS. '
                       + 'For market news, say MARKET. For Science and '
                       + 'Technology news, say SCIENCE. For Sports news, say '
                       + 'SPORTS')
            instr_sentence = instruction.hear_me(user_name)
        
            #if user doesnt speak
            if not instr_sentence:
                KudoSpeaks.kudo_speaks('I didnt understand')
                continue
            
            #tells top 5 national news
            elif "india" in instr_sentence.lower():
                KudoNews.news_app().india_news()
                KudoSpeaks.kudo_speaks('Do you want to hear more news?')
                instr_sentence = instruction.hear_me(user_name)
                if "no" in instr_sentence.lower():
                    break
                
            #says top 5 international news
            elif "world" in instr_sentence.lower():
                KudoNews.news_app().world_news()
                KudoSpeaks.kudo_speaks('Do you want to hear more news?')
                instr_sentence = instruction.hear_me(user_name)
                if "no" in instr_sentence.lower():
                    break
                
            #says top 5 business news
            elif "business" in instr_sentence.lower():
                KudoNews.news_app().business_news()
                KudoSpeaks.kudo_speaks('Do you want to hear more news?')
                instr_sentence = instruction.hear_me(user_name)
                if "no" in instr_sentence.lower():
                    break
                
            #tells top 5 market news
            elif "market" in instr_sentence.lower():
                KudoNews.news_app().market_news()
                KudoSpeaks.kudo_speaks('Do you want to hear more news?')
                instr_sentence = instruction.hear_me(user_name)
                if "no" in instr_sentence.lower():
                    break
                
            #tells top 5 science news
            elif "science" in instr_sentence.lower():
                KudoNews.news_app().science_news()
                KudoSpeaks.kudo_speaks('Do you want to hear more news?')
                instr_sentence = instruction.hear_me(user_name)
                if "no" in instr_sentence.lower():
                    break
                
            #tells top 5 sports news
            elif "sports" in instr_sentence.lower():
                KudoNews.news_app().sports_news()    
                KudoSpeaks.kudo_speaks('Do you want to hear more news?')
                instr_sentence = instruction.hear_me(user_name)
                if "no" in instr_sentence.lower():
                    break
                
            #if no keyword is captured
            else :
                KudoSpeaks.kudo_speaks('I did not understand')
    #tells all the things Kudo can do and repeats the loop         
    else:        
        KudoSpeaks.kudo_speaks('Here are all the things you can do:')
        KudoSpeaks.kudo_speaks('1. Check current weather conditions')
        KudoSpeaks.kudo_speaks('2. Play Games')
        KudoSpeaks.kudo_speaks('3. Listen to songs')
        KudoSpeaks.kudo_speaks('4. Watch movies')
        KudoSpeaks.kudo_speaks('5. Open Windows Applications')
        KudoSpeaks.kudo_speaks('6. Send Whatsapp message')
        KudoSpeaks.kudo_speaks('7. Listen to News')
        KudoSpeaks.kudo_speaks('8. Hear a joke')
        KudoSpeaks.kudo_speaks('If you want to exit, say GoodBye')