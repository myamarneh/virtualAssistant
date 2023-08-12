import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys


def speak(text):
    engine.say(text)
    engine.runAndWait()

def receiveRequest():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Awaiting Request...")
        audio = r.listen(source)

    try:
        print ("Recognizing")
        request = r.recognize_google(audio, language = 'en')
        print(f"user said: {request}\n")
    
    except:
        print("Sorry I didn't get that, please repeat your phrase")
        speak("Sorry I didn't get that, please repeat your phrase")
        request = receiveRequest()
    if 'Joe stop' in request:
            if NAME != None:
                speak(f"Goodbye {NAME}")
                sys.exit()
            else:
                speak("Goodbye")
                sys.exit()
    return request

def voiceType():
    speak("Would you prefer a masculine or feminine voice?")
    voice = receiveRequest().lower()
    global V
    V = 0

    if 'masculine' in voice:
        V = 0
    elif 'feminine' in voice:
        V = 1
    else:
        voice = voiceType()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning" + NAME)
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon" + NAME)
    else:
        speak("Good Evening" + NAME)

def addMusic():
    speak("If you would like to access your music, say yes and enter the desired applications directory, if not say no music")
    musicReq = receiveRequest().lower()
    if 'yes' in musicReq:
        global songDir
        speak("Please enter your music directory")
        songDir = input("Enter Directory Here: ")
        speak("Directory Updated")
    elif 'no' in musicReq:
        speak("Understood")

def changeMusic():
    speak("Please enter your new music directory")
    global songDir
    songDir = input("Enter Directory Here: ")
    speak("Directory Updated")

def addCode():
    speak("If you would like to access your code, say yes and enter the desired applications directory, if not say no code")
    codeReq = receiveRequest().lower()
    if 'yes' in codeReq:
        global codeDir
        speak("Please enter your coding application directory")
        codeDir = input("Enter Directory Here: ")
        speak("Directory Updated")
    elif 'no' in codeReq:
        speak("Understood")

def changeCode():
    speak("Please enter your new code directory")
    global codeDir
    codeDir = input("Enter Directory Here: ")
    speak("Directory Updated")

def changeName():
    speak("What would you like to change your name to?")
    global NAME 
    NAME = receiveRequest()
    speak(f"Name Updated, hello {NAME}")

def main():
    speak("How can I help?")
    request = receiveRequest().lower()   
    if 'wikipedia' in request:
        try:
            speak("Searching Wikipedia...")
            request = request.replace("wikipedia", "")
            result = wikipedia.summary(request, sentences = 2)
            print(result)
            speak(result)
        except:
            speak("Please include a search term")
    elif 'open youtube' in request:
        webbrowser.open("youtube.com")
        speak("Youtube Opening")
    elif 'open google' in request:
        webbrowser.open("google.com")
        speak("Google Opening")
    elif 'play music' in request:
        if songDir != None:
            try:
                os.startfile(songDir)
                speak("Here is your music")
            except:
                speak("Music application not found would you like to change the directory?")
                print("Error: Music application not found would you like to change the directory?")
                mcd = receiveRequest().lower()
                if 'yes' in mcd:
                    changeMusic()
                if 'no' in mcd:
                    speak("Understood")
        else:
                if request != None:
                    addMusic()
    elif 'change music directory' in request:
        changeMusic()
    elif 'change code directory' in request:
        changeCode()          
    elif 'the time' in request:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"the time is {time}")
    elif 'today\'s date' in request:
        day = datetime.date.today()
        speak(f"today's date is {day}")
    elif 'open code' in request:
        if codeDir != None:
            try:
                os.startfile(codeDir)
                speak("Here is your code")
            except:
                speak("Coding application not found would you like to change the directory?")
                print("Error: Coding application not found would you like to change the directory?")
                ccd = receiveRequest().lower()
                if 'yes' in ccd:
                    changeCode()
                if 'no' in ccd:
                    speak("Understood")
        else:
                addCode()
    elif 'change voice' in request:
        voiceType()
        engine.setProperty('voice', voices[V].id)
    elif 'change name' in request:
        changeName()
    elif 'list requests' in request:
        speak("Here is a list of the available commands")
        print("To Search for a Term include 'wikipedia' in request\n"
            "To Open Youtube include 'open youtube' in request\n"
            "To Open Google include 'open google' in request\n"
            "To Play Music include 'play music' in request\n"
            "To Change Music Directory include 'change music directory' in request\n"
            "To Open Your Coding Application include 'open code' in request\n"
            "To Change Your Coding Application\'s Directory include 'change code directory' in request\n"
            "To Get the Time inlcude 'the time' in request\n"
            "To Get the Date include 'today\'s date' in request\n"
            "To See Assistant Usage include 'list requests' in request\n"
            "To Change Assistant Voice include 'change voice' in request\n"
            "To Change Name include 'change name' in request")
    else:
        speak("Command unavailable, for usage please say, list requests") 
    
def start():
    speak("Initializing Assistant...")
    greet()
    speak("For a list of commands, say list requests")
    speak("To stop say, joe stop")
    global songDir
    songDir = None
    global codeDir
    codeDir = None
    addMusic()
    addCode()
    main()

print("Initializing Assistant")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')   
speak("Hello my name is Joe, what is your name?")
NAME = None
NAME = receiveRequest()
voiceType()
engine.setProperty('voice', voices[V].id)

start()

while True:   
    main()
