# Import necessary Libraries
import pyttsx3
import speech_recognition as sr
import winsound
import time

talk = pyttsx3.init()

#possible lists of possible words or sentences with different punctuation
hi_List = ['hi', 'Hi', 'Hello', 'hello', 'Hey', 'hey', 'yo', 'Yo,' 'salam', 'Salam', 'hi echo', 'Hi echo', 'echo', 'echo']
bye_List = ['Bye', 'bye', 'Goodbye', 'goodbye', 'Good bye' 'good bye', 'byebye', 'by by', 'By by', 'Tata', 'tata', 'So long', 'so long', 'okay bye', 'ok bye', 'Ok bye', 'Okay bye']
qst1_list = ["Who are you", 'who are you', 'what is your name', 'your name', 'Your name', 'What are you', 'what are you',]
question_list = ['what is the capital of india', "whats the capital of india"]
res_neg_list = ['bad robot', 'Bad robot','bad boy', "Bad boy", 'you are rude echo', 'You are rude echo', ' you are a bad robot', 'You are a bad robot']
slang_list = ['Bal', 'bal', 'Crap', 'crap', 'chutiya', 'Chutiya', 'chootia', 'Chootia']
Love_list = ['i love you', 'I love you', 'Love you', 'love you']
hate_list = ['i hate you', 'I hate you', 'Hate you', 'hate you']

def Listen():
    """
    Takes users voice as input and converts it to text.
    """
    speech = sr.Recognizer()
    #say beep before listening
    
    #take input from microphone
    with sr.Microphone() as source:
        winsound.Beep(frequency = 2500, duration = 100) #beep to inform that it's listening
        print("Say>>")
        voice = speech.listen(source) 
        text = speech.recognize_google(voice)
        print(text) #print what it heard just to debug

    return text  #return what was heard

    
def Decide(listen):
    """
    Takes decision based on what user says.
    """
    print(f" Command = {listen}.") #just to debug

    #see what user said is in which list or not
    if listen in hi_List:
        print("Resonse in Hi list")
        Respond("Hi there, Good to see you.")

    elif listen in bye_List:
        print("In bye list.")
        Respond("I liked talking with you, okay take care.")

    elif listen in Love_list:
        Respond("Yuk, I have a robot girl friend. No seat available")
    
    elif listen in hate_list:
        Respond("Hate you too.")
     
    elif listen in qst1_list:
        Respond("""I am Echo. The dumb talking robot written in python.
                    My creator Aarzoo islam is trying to make me smart""")
    
    elif listen in question_list:
        print("in qst_2 list.")
        Respond("The capital of india is delli")
    
    elif listen in res_neg_list:
        Respond("I am very sorry I was just joking.")

    elif listen in slang_list:
        Respond("You are a bad guy")

    else:
        Respond("Sorry I don't understand Please say again.")

def Respond(t):
    print(f"Talking the: {t}") #to debug and see if everythings going okay

    talk.say(t)
    talk.setProperty('rate', 90) #90 words per minute
    talk.runAndWait()

while True: #for ever loop 

    comm = Listen() #listen to what user says

    Decide(comm)  #take decision and respond

    time.sleep(1) #after that a delay of 1 second