import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
MASTER= "MIHIR"

print("Initialising Jarvis")

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# Speak func will pronounce the string which is passedto it 
def speak(text):
    engine.say(text)
    engine.runAndWait()

#this func will wish u according to time
def wishMe():
    hour= int(datetime.datetime.now().hour)
#    print(hour)
    if hour>=0 and hour<12:
        speak("Good Morning"+ MASTER)
    elif hour>=12 and hour<18:
        speak("Good Afternoon"+ MASTER)
    else:
        speak("Good Evening"+ MASTER)
    #speak("I am Jarvis. How may i help you ")

#this func will take input from microphone 
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTENing...")
        audio = r.listen(source)
    
    try:
        print("Recognizing")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said : {query}\n")

    except Exception as e:
        print("SAy that again please")
        query= None
    return query
    

#Main program starts here
speak("Initialising Jarvis...")
wishMe()
query = takeCommand()

#logic for executing basi tasks as per the query
if 'wikipedia' in query.lower():
    speak('Searching wikipedia...')
    query= query.replace("wikipedia","")
    results = wikipedia.summary(query, sentences = 2)
    print(results)
    speak(results)
elif 'open youtube' in query.lower():
   # webbrowser.open("youtube.com")
    
elif 'play music' in query.lower():
    songs = os.listdir()
    print(songs)



