import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("Hi, what can I do for you?")
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice).lower()
            if 'alexa' in command:
                command = command.replace('alexa','')

    except:
        pass
    return command

def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play','')
        print('Now playing'+ song)
        talk('Playing'+ song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        time2 = datetime.datetime.now().strftime('%I%M %p')
        print(time)
        talk("The time is:"+ time2)
    elif 'tell me about' in command:
        finder = command.replace('tell me about','')
        info = wikipedia.summary(finder,1)
        print(info)
        talk(info)
    elif 'joke' in command:
        temp = pyjokes.get_joke()
        print(temp)
        talk(temp)
    elif 'hello' or 'hi' in command:
        print("Hi there!")
        talk("Hi there!")
    else:
        print("Sorry, I didn't quite catch that!")
        talk("Sorry, I didn't quite catch that!")

while True:
    run_alexa()


