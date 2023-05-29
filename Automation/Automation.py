# Importing Required Modules:
import pyautogui
import os
import time
import pyttsx3
import wikipedia
import webbrowser
import random
import tkinter
from PIL import Image, ImageTk
from datetime import datetime

# An AI Image Window Using Tkinter
Image_Window = tkinter.Tk()
Image_Window.geometry("735x415")
Image_Window.resizable(0,0)
Image_Window.title("Artificial Intelligence And Desktop Assistant By Shylesh (JARVIS AI)")
Image_Window.iconbitmap("Assets/Jarvis_Logo.ico")
# Original Image
Image1 = tkinter.PhotoImage("Assests/Jarvis.png")
# Edited Image
Image2 = Image.open("Assets/Jarvis.png")
resized_image = Image2.resize((735,415), Image.LANCZOS)
converted_image = ImageTk.PhotoImage(resized_image)

# Funtion To Display The Image In Iage_Window
label = tkinter.Label(Image_Window, image=converted_image, width=735, height=415)
label.pack()
# Displaying The Image and Image_Window
print("Close The Image Window To Start")
Image_Window.mainloop()

# Speaking Functions
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Functions:

# Speaking Function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Wishing Function
def wishMe():
    hour = int(datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning Boss!")
        speak("Good Morning Boss!")
    elif hour>=12 and hour<15:
        print("Good Afternoon Boss!")
        speak("Good Afternoon Boss!")
    elif hour>=15 and hour<20:
        print("Good Evening Boss!")
        speak("Good Evening Boss!")
    else:
        print("Good Night Boss!")
        speak("Good Night Boss!")
    print("I Am Dusty")
    speak("I Am Dusty")

if __name__ == "__main__":
    wishMe()
    while True:
        print("Please Tell Me How Can I Help You")
        speak("Please Tell Me How Can I Help You")
        while True:
            command = input("Type What You Want To Do Here: ")
            # Searching Command In Wikipedia
            if "wikipedia" in command:
                print("Searching In Wikipedia")
                speak("Searching In Wikipedia")
                command=command.replace("wikipedia","")
                results=wikipedia.summary(command,sentences=5)
                print("According To Wikipedia: ")
                speak("According To Wikipedia: ")
                print(results)
                speak(results)
                break
            # Searching Command In Microsoft Edge
            if "search" in command:
                command=command.replace("search ","")
                print("Opening Microsoft Edge Sir")
                speak("Opening Microsoft Edge Sir")
                os.startfile("msedge.exe")
                time.sleep(10)
                pyautogui.hotkey('ctrl','l')
                pyautogui.write(command)
                pyautogui.press('enter')
                break
            # Opening Apps
            if "edge" in command:
                print("Opening Microsoft Edge Sir...")
                speak("Opening Microsoft Edge Sir...")
                os.startfile("msedge.exe")
                time.sleep(5)
            elif "calculator" in command:
                print("Opening Calculator Sir...")
                speak("Opening Calculator Sir...")
                os.startfile("calc.exe")
                time.sleep(5)
            elif "control" in command:
                print("Opening Control Panel Sir...")
                speak("Opening Control Panel Sir...")
                os.startfile("control.exe")
                time.sleep(5)
            elif "cmd" in command:
                print("Opening Command Prommt Sir...")
                speak("Opening Command Prommt Sir...")
                os.startfile("cmd.exe")
                time.sleep(5)
            elif "explorer" in command:
                print("Opening File Explorer Sir...")
                speak("Opening File Explorer Sir...")
                os.startfile("explorer.exe")
                time.sleep(5)
            elif "code" in command:
                print("Opening Visual Studio Code Sir...")
                speak("Opening Visual Studio Code Sir...")
                os.startfile("Code.exe")
                time.sleep(5)
            elif "powertoys" in command:
                print("Opening Micosoft PowerToys Sir...")
                speak("Opening Micosoft PowerToys Sir...")
                os.startfile("PowerToys.exe")
                time.sleep(5)
            elif "youtube" in command:
                print("Opening Youtube.com Sir...")
                speak("Opening Youtube.com Sir...")
                webbrowser.open("youtube.com")
                quit()
            # Some Fun Activities
            elif "joke" in command:
                while True:
                    while True:
                        all_jokes = [
                                "What did one snowman say to the other?, Do you smell carrots?",
                                "What Do Robots Eat For Snakes?, Computer Chips"
                            ]
                        joke = random.choice(all_jokes)
                        print("This Might Make You Laugh")
                        speak("This Might Make You Laugh")
                        print(joke)
                        speak(joke)
                        print("Ha Ha!")
                        speak("Ha Ha!")
                        speak("Do You Want Another Joke Sir?")
                        another_joke = input("Do You Want Another Joke Sir?: ")
                        if "yes" in another_joke:
                            break
                        else:
                            quit()
            elif "toss" in command:
                while True:
                    while True:
                        head_or_tail=["Heads","Tails"]
                        result=random.choice(head_or_tail)
                        print("Tossing A Coin Sir")
                        speak("Tossing A Coin Sir")
                        print("The Result Is "+result)
                        speak("The Result Is "+result)
                        speak("Do You Want To Toss Again Sir?")
                        toss_again = input("Do You Want To Toss Again Sir?: ")
                        if "yes" in toss_again:
                            break
                        else:
                            quit()
            # Some Talking Command For Time Pass
            elif "hello" in command:
                print("Hello Sir.")
                speak("Hello Sir.")
            elif "how are you" in command:
                how_are_you = ["I Am Doing Well Sir.","I Am Fine Sir."]
                how_are_you = random.choice(how_are_you)
                print(how_are_you)
                speak(how_are_you)
            elif "who created you" in command:
                print("I Have Been Created By Shylesh Shankar")
                speak("I Have Been Created By Shylesh Shankar")
            elif "who made you" in command:
                print("I Have Been Created By Shylesh Shankar")
                speak("I Have Been Created By Shylesh Shankar")
            elif "what are you doing" in command:
                print("I Am Learning About Humans And World")
                speak("I Am Learning About Humans And World")
            elif "sing a song" in command:
                print("I Don't Know To Sing Any Song Sorry Sir")
                speak("I Don't Know To Sing Any Song Sorry Sir")

            # Closing Command
            elif "shutdown" in command:
                confirm_shutdown = input("Are You Sure To ShutDown Your PC Sir?: ")
                if "yes" in confirm_shutdown:
                    speak("I Am Going To ShutDown Your PC Sir, Bye Sir, Have A Nice Day")
                    os.system('shutdown /s /t 06')
                else:
                    quit()
            elif "restart" in command:
                confirm_restart = input("Are You Sure To Restart Your PC Sir?: ")
                if "yes" in confirm_restart:
                    speak("I Am Going To Restart Your PC Sir, See You Again Sir")
                    os.system('shutdown /r /t 06')
                else:
                    quit()
            elif "quit" in command:
                print("I Am Quitting Sir, Bye Sir")
                speak("I Am Quitting Sir, Bye Sir")
                quit()
            else:
                print("Sorry Sir, I Can't Understand")
                speak("Sorry Sir, I Can't Understand")
                print("Please Tell Again")
                speak("Please Tell Again")