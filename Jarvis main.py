import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import pywhatkit as kit
from time import ctime
import time
import math
import random
import pygame
import random
import tkinter as tk
from tkinter import messagebox
import pyautogui  #mouse
from pynput.keyboard import Key, Controller
import random
from words import words
import string
from ctypes import windll



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning Sir!")
    elif hour>=12 and hour<4:
        speak("Good afternoon Sir!")
    else:
        speak("Good Evening Sir!")

    
def takeCommand():
    # takes my command from microphone and gives text
    r =sr.Recognizer()
    with sr.Microphone() as source:
       print("Listening...")
       r.energy_threshold = 4000
       r.pause_threshold =  1
       audio = r.listen(source)
                    
    try:
       print("Recognizing...")
       query = r.recognize_google(audio, language ='en-in')
       print("user said : ", query)
    except Exception as e:
       print(e)
       # print("Sorry Sir!, can you repeat that again?")
       # speak("Sorry Sir!, can you repeat that again?")
       return "None"

    return query



def TaskExecution():
    wishMe()
    while True:
        speak("How can i help you?")
        query = takeCommand().lower()
    
        # Logic for executing tasks as per the query    
        if 'search' in query.lower() and 'on wikipedia' in query.lower():
            query = query.replace("search", "").replace("on wikipedia", "")
            results = wikipedia.summary(query, sentences =3)
            print(results)
            speak(results)
        
        elif 'your name' in query.lower():
            speak("i am jarvis sir!")
        
        elif 'your gender' in query.lower():
            speak('i am male sir!')
        elif 'your age' in query.lower():
            speak('i am imortal sir! my age is 3 months')


        # Open url in a new window of the default browser
        elif 'open youtube' in query.lower():
            speak("opening youtube!")
            url = 'youtube.com'
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)
            

        elif 'open google' in query.lower():
            speak("opening google!")
            url = 'google.com'
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)
        

        elif 'close chrome' in query.lower() or 'close google chrome' in query.lower():
            speak("closing google chrome")
            os.system('taskkill /f /im chrome.exe')


        #say time
        elif 'time' in query.lower():
           print(ctime())
           speak(ctime())
        

        #searching on google
        elif 'search' in query.lower() and 'on google' in query.lower():
            google = query.replace("search", "").replace("on google", "")
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open('https://www.google.com/search?q=' + google)
            


        elif 'search' in query.lower() and 'on youtube' in query.lower():
            query = query.replace("search", "").replace("on youtube", "")
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open('https://www.youtube.com/results?search_query=' + query)



        #play and control videos on youtube

        elif 'play' in query.lower() and 'on youtube' in query.lower():
            speak("what should i play?")
            play = takeCommand()
            query = play
            kit.playonyt(query)




        elif 'full screen' in query.lower():
            keyboard = Controller()
            keyboard.press('f')




        elif 'normal screen' in query.lower():
            keyboard = Controller()
            keyboard.press('f')




        elif 'play the video' in query.lower():
            keyboard = Controller()
            keyboard.press('k')




        elif 'pause the video' in query.lower():
            keyboard = Controller()
            keyboard.press('k')




        elif 'mute the video' in query.lower():
            keyboard = Controller()
            keyboard.press('m')




        elif 'unmute the video' in query.lower():
            keyboard = Controller()
            keyboard.press('m')




        elif 'forward' in query.lower():
            pyautogui.press('right')




        elif 'rewind' in query.lower():
            pyautogui.press('left')




        elif 'volume up' in query.lower():
            pyautogui.press('up')




        elif 'volume down' in query.lower():
            pyautogui.press('down')



        
        elif 'restart the video' in query.lower():
            pyautogui.press('0')



        #some commands for timepass
        elif 'hello jarvis' in query.lower():
            print("Hello Sir!")
            speak("Hello Sir!")
            
        elif 'thank you jarvis' in query.lower():
            print("Welcome Sir!")
            speak("Welcome Sir!")
            break

        elif 'how are you jarvis' in query.lower():
            print("I am Good Sir!")
            speak("I am Good Sir!")


        elif 'apologize to me' in query.lower():
            print("I am Sorry Sir!")
            speak("I am Sorry Sir!")
           

        elif 'nikal' in query.lower():
            print("I am Sorry Sir!")
            speak("I am Sorry Sir!")
            exit()


        elif 'bye jarvis' in query:
            print("see you soon Sir!")
            speak("see you soon Sir!")
            exit()
        
        
        elif 'stop jarvis' in query:
            print("see you soon Sir!")
            speak("see you soon Sir!")
            exit()


        #opening apps
        elif 'open spotify' in query.lower():
            print("opening spotify")
            speak("opening spotify")
            os.startfile('C:/Users/admin/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Spotify')
        

        elif 'close spotify' in query.lower():
            speak("closing spotify")
            os.system('taskkill /f /im Spotify.exe')


        #play music
        elif 'play music' in query.lower():
            print("opening spotify")
            speak("opening spotify")
            os.startfile('C:/Users/admin/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Spotify')


        #open apps
        elif 'open discord' in query.lower():
            print("opening discord")
            speak("opening discord")
            os.startfile('C:/Users/admin/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Discord Inc/Discord')
        

        elif 'close discord' in query.lower():
            speak("closing discord")
            os.system('taskkill /f /im Discord.exe')
            

        elif 'open whatsapp' in query.lower():
            print("opening whatsapp")
            speak("opening whatsapp")
            os.startfile('C:/Users/admin/Desktop/Desktop Shit/WhatsApp')
            

        elif 'close whatsapp' in query.lower():
            speak("closing whatsapp")
            os.system('taskkill /f /im WhatsApp.exe')
        

        elif 'open instagram' in query.lower():
            print("opening instagram")
            speak("opening instagram")
            os.startfile('C:/Users/admin/Desktop/Desktop Shit/Instagram')
        

        elif 'switch the window' in query.lower():
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")


        #snake game
        elif 'snake game' in query.lower():
            width = 500
            height = 500

            cols = 25
            rows = 20


            class cube():
                rows = 20
                w = 500
                def __init__(self, start, dirnx=1, dirny=0, color=(255,0,0)):
                    self.pos = start
                    self.dirnx = dirnx
                    self.dirny = dirny # "L", "R", "U", "D"
                    self.color = color

                def move(self, dirnx, dirny):
                    self.dirnx = dirnx
                    self.dirny = dirny
                    self.pos  = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)
            

                def draw(self, surface, eyes=False):
                    dis = self.w // self.rows
                    i = self.pos[0]
                    j = self.pos[1]
        
                    pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1,dis-2,dis-2))
                    if eyes:
                        centre = dis//2
                        radius = 3
                        circleMiddle = (i*dis+centre-radius,j*dis+8)
                        circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)
                        pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
                        pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)
        


            class snake():
                body = []
                turns = {}
    
                def __init__(self, color, pos):
                    #pos is given as coordinates on the grid ex (1,5)
                    self.color = color
                    self.head = cube(pos)
                    self.body.append(self.head)
                    self.dirnx = 0
                    self.dirny = 1
    
                def move(self):
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        keys = pygame.key.get_pressed()

                        for key in keys:
                            if keys[pygame.K_LEFT]:
                                self.dirnx = -1
                                self.dirny = 0
                                self.turns[self.head.pos[:]] = [self.dirnx,self.dirny]
                            elif keys[pygame.K_RIGHT]:
                                self.dirnx = 1
                                self.dirny = 0
                                self.turns[self.head.pos[:]] = [self.dirnx,self.dirny]
                            elif keys[pygame.K_UP]:
                                self.dirny = -1
                                self.dirnx = 0
                                self.turns[self.head.pos[:]] = [self.dirnx,self.dirny]
                            elif keys[pygame.K_DOWN]:
                                self.dirny = 1
                                self.dirnx = 0
                                self.turns[self.head.pos[:]] = [self.dirnx,self.dirny]
                            elif keys[pygame.K_SPACE]:
                                exit()
        
                    for i, c in enumerate(self.body):
                        p = c.pos[:]
                        if p in self.turns:
                            turn = self.turns[p]
                            c.move(turn[0], turn[1])
                            if i == len(self.body)-1:
                                self.turns.pop(p)
                        else:
                            c.move(c.dirnx,c.dirny)
        
        
                def reset(self,pos):
                    self.head = cube(pos)
                    self.body = []
                    self.body.append(self.head)
                    self.turns = {}
                    self.dirnx = 0
                    self.dirny = 1

                def addCube(self):
                    tail = self.body[-1]
                    dx, dy = tail.dirnx, tail.dirny

                    if dx == 1 and dy == 0:
                        self.body.append(cube((tail.pos[0]-1,tail.pos[1])))
                    elif dx == -1 and dy == 0:
                        self.body.append(cube((tail.pos[0]+1,tail.pos[1])))
                    elif dx == 0 and dy == 1:
                        self.body.append(cube((tail.pos[0],tail.pos[1]-1)))
                    elif dx == 0 and dy == -1:
                        self.body.append(cube((tail.pos[0],tail.pos[1]+1)))

                    self.body[-1].dirnx = dx
                    self.body[-1].dirny = dy
    
                def draw(self, surface):
                    for i,c in enumerate(self.body):
                        if i == 0:
                            c.draw(surface, True)
                        else:
                            c.draw(surface)
            


            def redrawWindow():
                global win
                win.fill((0,0,0))
                drawGrid(width, rows, win)
                s.draw(win)
                snack.draw(win)
                pygame.display.update()
                pass
                



            def drawGrid(w, rows, surface):
                sizeBtwn = w // rows

                x = 0
                y = 0
                for l in range(rows):
                    x = x + sizeBtwn
                    y = y +sizeBtwn

                    pygame.draw.line(surface, (255,255,255), (x, 0),(x,w))
                    pygame.draw.line(surface, (255,255,255), (0, y),(w,y))
    


            def randomSnack(rows, item):
                positions = item.body

                while True:
                    x = random.randrange(1,rows-1)
                    y = random.randrange(1,rows-1)
                    if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
                        continue
                    else:
                        break

                return (x,y)


            def main():
                global s, snack, win
                win = pygame.display.set_mode((width,height))
                s = snake((255,0,0), (10,10))
                s.addCube()
                snack = cube(randomSnack(rows,s), color=(0,255,0))
                flag = True
                clock = pygame.time.Clock()
    
                while flag:
                    pygame.time.delay(50)
                    clock.tick(10)
                    s.move()
                    headPos = s.head.pos
                    if headPos[0] >= 20 or headPos[0] < 0 or headPos[1] >= 20 or headPos[1] < 0:
                        print("Score:", len(s.body))
                        s.reset((10, 10))
                        time.sleep(1)

                    if s.body[0].pos == snack.pos:
                        s.addCube()
                        snack = cube(randomSnack(rows,s), color=(0,255,0))
            
                    for x in range(len(s.body)):
                        if s.body[x].pos in list(map(lambda z:z.pos,s.body[x+1:])):
                            print("Score:", len(s.body))
                            s.reset((10,10))
                            break
                    

                    redrawWindow()

            main()



        #send messages
        elif 'send a message' in query.lower():
            speak("what is the message?")
            message = takeCommand()
            query = message
            string_in_string = '{}\n'.format(query)
            pyautogui.typewrite(string_in_string)
            speak("message sent!")

        


        #hangman game

        elif 'hangman' in query.lower():


            def get_valid_word(words):
                word = random.choice(words)  # randomly chooses something from the list
                while '-' in word or ' ' in word:
                    word = random.choice(words)
                return word.upper()


            def hangman():
                word = get_valid_word(words)
                word_letters = set(word)  # letters in the word
                alphabet = set(string.ascii_uppercase)
                used_letters = set()  # what the user has guessed

                lives = 7

                # getting user input
                while len(word_letters) > 0 and lives > 0:
                    # letters used
                    # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
                    print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

                    # what current word is (ie W - R D)
                    word_list = [letter if letter in used_letters else '-' for letter in word]
                    print('Current word: ', ' '.join(word_list))

                    user_letter = input('Guess a letter: ').upper()
                    if user_letter in alphabet - used_letters:
                        used_letters.add(user_letter)
                    if user_letter in word_letters:
                        word_letters.remove(user_letter)
                        print('')

                    else:
                        lives = lives - 1  # takes away a life if wrong
                        print('\nYour letter,', user_letter, 'is not in the word.')

                    if user_letter in used_letters:
                        print('\nYou have already used that letter. Guess another letter.')

                    else:
                        print('\nThat is not a valid letter.')

                # gets here when len(word_letters) == 0 OR when lives == 0
                if lives == 0:
                    print('You died, sorry. The word was', word)
                else:
                    print('YAY! You guessed the word', word, '!!')


            if __name__ == '__main__':
                hangman()




        #TicTacToe game

        elif 'tic tac toe' in query.lower():
            print("Playing Tic Tac Toe!")
            speak("Playing Tic Tac Toe!")
            os.startfile('E:/jarvis/main.py')
            exit()
            



        #Amazon Searching

        elif 'search' in query.lower() and 'on amazon' in query.lower():
            speak("what should i search?")
            search = takeCommand()
            query = search
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open('https://www.amazon.in/s?k=' + query)




        #Flipkart Searching

        elif 'search' in query.lower() and 'on flipkart' in query.lower():
            speak("what should i search?")
            search = takeCommand()
            query = search
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open('https://www.flipkart.com/search?q=' + query)




        #Download Games

        if 'search' in query.lower() and 'on ocean of games' in query.lower():
            query = query.replace("search", "").replace("on ocean of games", "")
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open('http://oceanofgames.com/?s=' + query) 


        
        if 'search' in query.lower() and 'on allgamesforyou' in query.lower():
            query = query.replace("search", "").replace("on allgamesforyou", "")
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open('https://agfy.co/?s=' + query)
        


        if 'allgamesforyou game list' in query.lower():
            speak("opening")
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open('https://agfy.co/games-list/')



        if 'allgamesforyou software list' in query.lower():
            speak("opening")
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open('https://agfy.co/software-list/')
        




        #spam

        if 'spam' in query.lower():
            speak("what should i spam?")
            spam = takeCommand()
            query = spam

            condition = 100

            while condition > 0:
                condition = condition-1

                if condition == 2:
                    break 

                string_in_string = '{}\n'.format(query)
                pyautogui.typewrite(string_in_string)


        #human benchmark

        if 'human benchmark' in query.lower():
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open('https://humanbenchmark.com/tests/reactiontime')
              
            sniper_number = 0.01       # Tweak this according to your PC speed
            trigger_color = 7002955

            if __name__ == "__main__":
                gdi = windll.LoadLibrary("c:\\Windows\\system32\\gdi32.dll")

                while 1:
                    begin = time.time()
                    time.sleep(0.01)
                    width, height = pyautogui.position()
                    pixel = int(gdi.GetPixel(windll.user32.GetDC(0), width, height))
                    # uncomment if need to change color:
                    #print(pixel)
                    if pixel == trigger_color:
                        while time.time() - begin < sniper_number:
                            pass
                        pyautogui.click()


        #discord

        if 'message' in query.lower() and 'on discord' in query.lower():
            speak("to whom should i message?")
            person = takeCommand()
            query = person
            os.startfile('C:/Users/admin/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Discord Inc/Discord')
            time.sleep(2)
            pyautogui.moveTo(35,45)
            time.sleep(0.5)
            pyautogui.leftClick(35,45)
            pyautogui.moveTo(160,45)
            time.sleep(0.5)
            pyautogui.leftClick(160,45)
            pyautogui.typewrite(person)
            pyautogui.press('enter')
            speak("what is the message?")
            send = takeCommand()
            msg = send
            pyautogui.typewrite(msg)
            pyautogui.press('enter')

            


        if 'call' in query.lower() and 'on discord' in query.lower():
            speak("to whom should i call?")
            message = takeCommand()
            query = message
            query = query.replace("  ", "")
            os.startfile('C:/Users/admin/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Discord Inc/Discord')
            time.sleep(2)
            pyautogui.moveTo(35,45)
            time.sleep(0.5)
            pyautogui.leftClick(35,45)
            pyautogui.moveTo(160,45)
            time.sleep(0.5)
            pyautogui.leftClick(160,45)
            pyautogui.typewrite(query)
            pyautogui.press('enter')
            time.sleep(0.5)
            pyautogui.moveTo(975,45)
            time.sleep(0.5)
            pyautogui.leftClick(975,45)






if __name__ == "__main__":
    while True:
        permission = takeCommand()
        if "Jarvis" in permission:
            TaskExecution()
        elif "stop" in permission:
            print("see you soon Sir!")
            speak("see you soon Sir!")
            exit()
        elif "goodbye" in permission:
            print("see you soon Sir!")
            speak("see you soon Sir!")
            exit()
        elif "bye" in permission:
            print("see you soon Sir!")
            speak("see you soon Sir!")
            exit()
        elif "nikal" in permission:
            print("see you soon Sir!")
            speak("see you soon Sir!")
            exit()