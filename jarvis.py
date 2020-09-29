'''

What can this A.I J.A.R.V.I.S do for you

It can send emails for you
It can play music for you
It can do wikipedia searches for you
It can do website searches for you
This can tell present time correctly
It is capable of opening websites like Google, Youtube, etc, in a web browser
It is capable of opening your code or IDE with a single voice command

'''

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import wolframalpha

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id) # voice[0].id = Male voice and voice[1].id = Female voice

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe(): # it will make our J.A.R.V.I.S wish the user according to the time of computer
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning !")

    elif hour>=12 and hour<18:
        speak("Good afternoon")

    else:
        speak("Good evening")

    speak("I am jarvis sir. please tell me how may i help you")

def takeCommand():
    #it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('iaarzoo40@gmail.com', 'Aarzoorumi75') # your email id , password
    server.sendmail('iaarzoo40@gmail.com', to,content)
    server.close()


if __name__ == "__main__":
    wishMe()
    #if 1: # akta task kore exit hoie jabe
    while True: # contine cholbe
        query = takeCommand().lower()
    
    #logic for executing tasks based on query
        if 'wikipedia' in query: # wikipedia
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) #sentences ta holo koto line porbe
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query: # Youtbue
            webbrowser.open("youtube.com")
        elif 'open google' in query: # Google
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query: # stackoverflow
            webbrowser.open("stackoverflow.com")
        elif 'website' in query: # website
            speak('what should i search sir')
            scarch = takeCommand()
            chromepath = 'C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s'
            webbrowser.get(chromepath).open_new_tab(scarch+'.com')
        
        elif 'play music' in query: # music
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query: # time
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query: # vs code
            codePath = "C:\\Users\\NFPC\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to arju' in query: # email
            try:
                speak("what should i say ?")
                content = takeCommand()
                to = "iaarzoo758607@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("Sorry sir. i am not able to send this email")

                    # exit this system
                    
        elif 'quit' in query:
           os._exit(0)

        elif 'bye' in query:
            speak('bye sir, have a good day.')
            os._exit(0)