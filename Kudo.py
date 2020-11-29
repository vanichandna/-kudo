import string
import random
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#class which contains all the web browser related apps
class browser_app:
    #initialize chrome webdriver
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        self.browser = webdriver.Chrome(executable_path = r"C:\Users\HP\Downloads\chromedriver", options=chrome_options)
        
    #leads to song on gaana.com
    def play_song (self, song_name):
        self.browser.get("https://www.gaana.com")
        find_song = self.browser.find_element_by_id("sb")
        find_song.send_keys(song_name + Keys.ENTER)

    #leads to movies/videos on youtube
    def play_movie (self, movie_name):
        self.browser.get("https://www.youtube.com")
        find_movie = self.browser.find_element_by_name("search_query")
        find_movie.send_keys(movie_name+Keys.ENTER)

    #leads to current weather update on google
    def weather_forecast (self):
        self.browser.get("https://www.google.com")
        search = self.browser.find_element_by_name("q").send_keys('weather forecast' + Keys.ENTER)
        
#speech recognition class
class hear_me:
    
    #initialize recognizer
    def __init__(self):
        self.r = sr.Recognizer()

    #records voice and converts to text and sends the text
    def hear_me(self):
        speak = input('Press Enter to speak')
        with sr.Microphone() as source:
            audio = self.r.listen(source)
        try:
            speech = self.r.recognize_google(audio)
            print("Vani: "+self.r.recognize_google(audio))
        except LookupError:
            print("could not understand audio")
        except sr.UnknownValueError:
            print("couldnt find matching word")
        except sr.RequestError:
            print ("Unable to generate text from audio")
        return speech

#module for guess the movie game
class movie_game:
    #contains movie database
    def __init__(self):
        self.movies=['dangal','jungle book','aladdin','manikarnika','dil bechara',
        'harry potter','chhalaang','the lord of the rings','oceans eleven',
        'inception','veer zaara','lights out','bunty aur bably','joker',
        'mardaani','english vinglish','the godfather','fight club','star wars',
        'the good the bad and the ugly','interstellar','gulabo sitabo',
        'chakde india','sonu ke titu ki sweety']

    #updates movie question by add the letters guessed correctly by the user
    def update_mov(self, letter, movie, enc_movie):
        temp=[]
        for i in range(len(movie)):
            if movie[i]==letter:
                temp.append(movie[i])
            else:
                temp.append(enc_movie[i])
        m = ''.join(temp)
        return m

    #selects movie name randomly from the database, encrypts the movie and 
    #allows user to guess the movie letter by letter
    def play_guess_the_movie(self):
        mov = random.choice(self.movies)
        temp = []
        for i in mov:
            if i==' ':
                temp.append(i)
            else:
                temp.append('*')
        enc_mov = ''.join(temp)
        times = 5
        while  times:
            if mov == enc_mov:
                break
            print (enc_mov)
            letter = input('Guess the letter: ')
            if mov.count(letter):
                enc_mov = self.update_mov(letter, mov, enc_mov)
            else:
                print('Oops.. Try another letter')
                times = times - 1
                print(times, ' incorrect letters are allowed')
        
        if enc_mov != mov:
            print('Movie is ', mov)
            print('It\'s ok.. Try another time..')
        else:
            print (mov)
            print('Congrats..you won!!')

#module to play dobble game
class dobble_game:
    #initializes symbols to be used in the game
    def __init__(self):
        self.symbols = list(string.punctuation)

    #function randomizes the symbols such that 2 cards contain exactly 1 
    #common symbol
    def play_game(self):
        card1=[0]*5
        card2=[0]*5
        pos1=random.randint(0,4)
        pos2=random.randint(0,4)
        if (pos1==pos2):
            card1[pos1]=random.choice(self.symbols)
            card2[pos1]=card1[pos1]
            self.symbols.remove(card1[pos1])
        else:
            card1[pos1]=random.choice(self.symbols)
            card2[pos2]=card1[pos1]
            self.symbols.remove(card1[pos1])
            card1[pos2]=random.choice(self.symbols)
            self.symbols.remove(card1[pos2])
            card2[pos1]=random.choice(self.symbols)
            self.symbols.remove(card2[pos1])
        i=0
        while (i<5):
            if (i!=pos1 and i!=pos2):
                card1[i]=random.choice(self.symbols)
                self.symbols.remove(card1[i])
                card2[i]=random.choice(self.symbols)
                self.symbols.remove(card2[i])
            i=i+1

        print(card1)
        print(card2)

        ch=input("find same symbol: ")
        if (ch==card1[pos1]):
            print("Congrats.. u won")
        else:
            print("oops.. try again")
            
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
        if (score==34 or score==25 or score==47 or score==87 or score==99 or 
    score == 65 or score==91):
            print ('Oops..Snanke bit you!!')
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
        if (score==3 or score==6 or score==20 or score==36 or score==68 or 
    score == 63):
            print ('Yay..You got up by the ladder!!')
        return switcher.get(score, score)

    #shows score of both players
    def show_score(self, p1name, p2name, p1score, p2score):
        print('Score of ', p1name, ' is ', p1score)
        print('Score of ', p2name, ' is ', p2score)
        
    #function to play snakes and ladders game
    def play_snakes_n_ladders(self):
        p1name = input('Player 1, please enter your name:')
        p2name = 'Computer'
        p1score = 0
        p2score = 0
        score = p1score
        turn  = 0
        while 1:
            if turn == 1:
                score = p2score
                print (p2name, 'It\'s your turn')
            else:
                score = p1score                
                print (p1name, 'It\'s your turn')
            if turn == 0:
                cont = int(input('Press 1 if you want to continue, else press 0: '))
                if cont == 0:
                    break
            dice = random.randint(1,6)
            print('Dice rolls to ', dice)
            score = score + dice
            if score >= 100:
                score = 100
            if turn == 0:
                p1score = score
            else:
                p2score = score
            if (dice == 6):
                print('Yayyy..Dice rolled to 6.. You get another chance!!')
                continue
            score = self.check_snake(score)
            score = self.check_ladder(score)
            if turn == 0:
                p1score = score
            else:
                p2score = score
            
            if p1score == 100:
                self.show_score(p1name, p2name, p1score, p2score)
                print ('Congrats', p1name, 'You won!!')
                break
            if p2score == 100:
                self.show_score(p1name, p2name, p1score, p2score)
                print ('Congrats', p2name, 'You won!!')
                break
            self.show_score(p1name, p2name, p1score, p2score)
            turn = ( turn + 1 ) % 2
        

print('Kudo: Hi.. I am Kudo.. What do you want to do?')
while (1):
    instruction = hear_me()
    instr_sentence = instruction.hear_me()
        
    if instr_sentence.find("how are you")!=-1 or instr_sentence.find("How are you")!=-1:
        print("Kudo: I am fine.. How are you?")
    elif instr_sentence.find("weather") != -1:
        open_app = browser_app()
        open_app.weather_forecast()
    elif instr_sentence.find("game") != -1:
        print('Kudo: I have following games..Which game would you like to play?')
        print('Kudo: 1. Dobble Game')
        print('Kudo: 2. Guess the movie')
        print('Kudo: 3. Snakes & Ladders')
        game = hear_me()
        game_sentence = game.hear_me()
        if game_sentence.find("dobble") != -1 or game_sentence.find("Dobble") != -1:
            playgame = dobble_game()
            playgame.play_game()
        elif game_sentence.find("movie") != -1 or game_sentence.find("Movie") != -1:
            playgame = movie_game()
            playgame.play_guess_the_movie()
        elif game_sentence.find("Snakes") != -1 or game_sentence.find("snakes") != -1:
            playgame = snakes_n_ladders()
            playgame.play_snakes_n_ladders()
        else :
            print("Try Again..")
    elif instr_sentence.find("music") != -1 or instr_sentence.find("song") != -1:
        print("Kudo: Which song do you want me to play?")
        song = hear_me()
        song_name = song.hear_me()
        open_app = browser_app()
        open_app.play_song(song_name)
    elif instr_sentence.find("movie") != -1 or instr_sentence.find("Movie") != -1:
        print("Kudo: Which movie you want to watch?")
        movie = hear_me()
        movie_name = movie.hear_me()
        open_app = browser_app()
        open_app.play_movie(movie_name)
    elif instr_sentence.find("goodbye") != -1:
        break
    else:
        print('Kudo: Here are all the things you can do:')
        print('Kudo: 1. Check current weather conditions')
        print('Kudo: 2. Play Games')
        print('Kudo: 3. Listen to songs')
        print('Kudo: 4. Watch movies')
        print('Kudo: If you want to exit, say GoodBye')