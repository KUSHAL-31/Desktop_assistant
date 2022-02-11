import pyttsx3
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 175)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greet():
    hour = int(datetime.datetime.now().hour)
    min = int(datetime.datetime.now().minute)

    if hour >= 0 and hour < 12:
        speak("Good Morning sir,.......hope you have a fine day ahead")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir, i hope you are fine")
    else:
        speak("Good evening sir, i hope you are enjoying your day ")
    speak("My name is K31 assistant, how may i help you")


def command():
    print("Waiting for your response...")
    txt = input()
    return txt


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    greet()

    while True:
        query = command().lower()

        if 'my name' in query:
            speak("Yes sir, i obviously know your name, it is Mr.Kushal Soni")

        elif 'time' in query:
            hour = int(datetime.datetime.now().hour)
            min = int(datetime.datetime.now().minute)
            speak(f"The current time is {hour} hours and {min} minutes")

        elif 'k31' or 'k31':
            speak("I am doing great sir.....Online and ready for you")

        elif 'wikipedia' in query:
            try:
                speak("Searching on wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                speak(results)
            except Exception as e:
                speak(
                    "Sorry i am not able to find any information regarding it...please repeat it again")

        elif 'open google' in query:
            speak("opening google chrome browser...")
            webbrowser.open("www.google.com")

        elif 'open youtube' in query:
            speak("opening youtube...")
            webbrowser.open("www.youtube.com")

        elif 'rgit' in query:
            speak("Why do you want me to speak.....about a college which is already being abused daily by you sir........haa..haa..haa")
