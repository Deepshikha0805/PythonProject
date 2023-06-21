import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices', voices[1].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#To convert voice into text
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=10)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

#to wish
def wish():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("Good morning Deepshikha")
    elif hour>12 and hour<17:
        speak("Good afternoon Deepshikha")
    else:
        speak("Good evening Deepshikha")
    speak("I am assistant Warner , please tell me how can i help you")


if __name__=="__main__":
    wish()
    #while True:
    if 1:

        query=takecommand().lower()

        #logic building for tasks

        if "warner open notepad"in query:
            npath="C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)

        elif "warner open command prompt" in query:
            os.system ("start cmd ")

        elif "warner open camera" in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "warner play music" in query:
            music_dir = "C:\\Users\\hp\\Music"
            songs=os.listdir(music_dir)
            #rd=random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))

        elif "ip address" in query:
            ip=get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)





    #takecommand()
    #speak("I am iron man's assistant jarvis")

