# IMPORTING MODULES

# Inbuilt Modules:
import datetime # Module To Speak Things Related To Time

# Other Modules(You Have To Pip Install It)
import pyttsx3 # Module To Make Desktop Assistant(Dusky) To Speak
import speech_recognition # Module To Get Microphone Input From The User
import wikipedia # Module To Search Somethings In Wikipedia
import webbrowser # Module To Open Some Websites

# VARIABLES:

# Variables To Make Dusky Speak:
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# FUNCTIONS:

# Function To Make Dusky Speak:
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function To Wish The User:
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=3 and hour<12:
        speak("Good Morning Boss!")
    elif hour>=12 and hour<15:
        speak("Good Afternoon Boss!")   
    elif hour>=15 and hour<20:
        speak("Good Evening Boss!")  
    else:
        speak("")
    speak("Please Tell Me How Can I Help You")

# Function To Get Microphone Input From The User
def takecommand():
    r=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:   
        print("Wait For Few Moments")
        query=r.recognize_google(audio,language='en-in')
        print("User Said", query)
        
    except Exception as e:
        print(e)
        query="nothing"
    return query

# Function To Make Dusky Do Some Tasks:
def Tasks():
    query=takecommand().lower()
    if 'who is' in query:
        print('Searching in Wikipedia...')
        speak('Searching in Wikipedia...')
        query = query.replace("who is ", "")
        # If You Tell "Who Is Sharukh Khan", It Will Replace It To Just "Sharukh Khan"
        results = wikipedia.summary(query, sentences=2)
        print("According to Wikipedia")
        speak("According to Wikipedia")
        print(results)
        speak(results)

# Running The DeskTop Assistant(Dusky)
if __name__ == "__main__":
    wishMe()
    while True:
        query=takecommand().lower()
        Tasks()
