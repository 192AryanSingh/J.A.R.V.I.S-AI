import pyttsx3
import speech_recognition as sr
import datetime
import os
import wikipedia
from googlesearch import search
import webbrowser  # Import the webbrowser module

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        print("Wait for a few moments...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You just said: {query}\n")
    except Exception as e:
        print(e)
        speak("Please Tell me again")
        query = "none"
    return query

def wishings():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good Morning Sir")
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 17:
        print("Good Afternoon Sir")
        speak("Good Afternoon Sir")
    elif hour >= 17 and hour < 20:
        print("Good Evening Sir")
        speak("Good Evening Sir")
    else:
        print("Good Night Sir")
        speak("Good Night Sir")

if __name__ == "__main__":
    wishings()
    query = commands().lower()
    if 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(strTime)
        speak(f"Sir, the time is {strTime}")
    elif 'open google chrome' in query:
        speak("Opening Google Chrome Application sir....")
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(chrome_path)
    elif 'wikipedia' in query:
        speak("Searching in Wikipedia")
        try:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        except wikipedia.exceptions.DisambiguationError as e:
            speak("Multiple results found. Please specify your query.")
            print("Multiple results found. Please specify your query.")
        except wikipedia.exceptions.PageError as e:
            speak("No results found. Please try a different query.")
            print("No results found. Please try a different query.")
    elif 'search google' in query:
        query = query.replace("search google", "")
        speak(f"Searching Google for {query}")
        search_results = search(query, num_results=5)  # Limit to 5 results
        for i, result in enumerate(search_results):
            if i >= 5:  # Limit the number of results to 5
                break
            print(result)
    elif 'open search' in query:  # Open a Google search in the web browser
        webbrowser.open("https://www.google.com/")
