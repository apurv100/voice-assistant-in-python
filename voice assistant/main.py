import pyttsx3 
# pyttsx3 is text to speech conversion library in python which can work offline.
# To install pyttsx3 -  pip install pyttsx3
import speech_recognition as sr
# To install SpeechRecognition library - pip install SpeechRecognition
import datetime
import os
import smtplib # Small Mail transfer protocols for sending mail
import webbrowser
import wikipedia

engine = pyttsx3.init('sapi5') # sapi 5 is an API developed by Microsoft to allow the use of Speech Recognition and Speech Synthesis within windows application
voices = engine.getProperty('voices') # Getting Details of current voice
#engine.setProperty('voice', voices[0].id)
# Changing index will change the voices, 0 for male(David), 1 for female(Zira), 2 or beyond for any other voices if available

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

def speak(audio):
    # This function will take a string as input and will spell that string.
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    # This function greet you according to the timing.
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good Morning Sir.')
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon Sir.')
    else:
        speak('Good Evening Sir.')
    speak("I am Jarvis. How can I assist you?")


## this function takes in the commands from user
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something")
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-us")
        print(f"User said: {query}\n")
    except Exception as e:
        speak("Say that again please")
        print("Say that again please")
        return "None"
    return query


def executeCommand(query):
    if 'wikipedia' in query:
        speak('Searching Wikipedia')
        query = query.replace("wikipedia", "")
        try:
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)
            return True
        except :
            speak("the search query doesn not exist")
            return True
    elif 'open youtube' in query:
        webbrowser.get(chrome_path).open("youtube.com")
        return True
        
    elif 'open google' in query:
        webbrowser.get(chrome_path).open("google.com")
        return True
    elif 'open stackoverflow' in query:
        webbrowser.get(chrome_path).open("stackoverflow.com")
        return True
    elif 'email' in query:
        try:
            speak("What should I say?")
            content = takeCommand()
            to = "apurva.somu@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent!")
            return True
        except Exception as e:
            speak("I am not able to send this email")
            return True
    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print("Sir, the time is {}".format(strTime))
        speak("Sir, the time is {}".format(strTime))
        return True
        
    elif 'bye' in query:
        speak("goodbye sir happy to help!")
        return False



def main():
    #wishMe()
    m=True
    c=0
    while c<=3:
        query = takeCommand().lower()
        m = executeCommand(query)
        if m==False:
            break
        c=c+1


main()