import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import pyjokes

engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('7K955E-RYVVAG93W4')

voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[len(voices)-0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    print('Jarvis: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('Hello Sir, i am a jarvis')
speak('How may I help you?')

'''
def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query
'''
        
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

def jokes():
    my_joke = pyjokes.get_joke('en', category='neutral')
    print(my_joke)
    speak(my_joke)

if __name__ == '__main__':

    while True:
    
        query = takeCommand()
        query = query.lower()
        
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')
            
        elif 'website' in query: # website
            speak('what should i search sir')
            scarch = takeCommand()
            chromepath = 'C://Program Files (x86)//Google//Chrome//Application//chrome.exe %s'
            webbrowser.get(chromepath).open_new_tab(scarch+'.com')

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = takeCommand()

            if 'arzoo' in recipient or 'arju' or 'arjoo' or 'arjun' in recipient:
                try:
                    speak('What should I say? ')
                    content = takeCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("iaarzoo40@gmail.com", 'Aarzoorumi75')
                    server.sendmail('iaarzoo40@gmail.com', "iaarzoo40@gmail.com", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))
            
        elif 'i hate you' in query:
            speak('really')
            an = takeCommand()
            if 'yes' in an:
                speak('hate you')
            else:
                speak('ok')

        elif 'who is the best man in the world' in query:
            speak('according to Harts Top 10 ranking, the best man in the world is the Prophet of Islam Muhammad. a selection that generated some controversy.')
            
        elif 'hello' in query:
            speak('Hello Sir')

        elif 'who are you' in query or 'what is your name' in query:
            speak('i am jarvis. made by aarzoo islam')

        
        elif 'what is the time right now' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
                                    
        elif 'music' in query:
            music_folder = 'D:\\music\\'
        
            music = ['music1', 'music2', 'music3', 'music4', 'music5', 'Rauf_&_Faik_-_детство']
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)
                  
            speak('Okay, here is your music! Enjoy!')

        elif "funny" in query:
            jokes()

        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('according to me....')
                    speak(results)
        
            except:
                #webbrowser.open('www.google.com')
                speak('say again please. i dont understand.')
        
        speak('Next Command! Sir!')
        