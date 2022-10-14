from email.mime import audio
from unittest import result
import pyttsx3
import speech_recognition as sr  #pip install speechRecognition
import datetime
import wikipedia
import webbrowser 
import os
import requests
from bs4 import BeautifulSoup
import cv2
from geopy import Nominatim

engine = pyttsx3.init('sapi5') #API to take voices 
voices = engine.getProperty('voices')
#print(voices[1].id) #it will show voices present in the system

engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")

    elif hour>=12 and hour<18:
        speak("Good afternoon!")

    else:
        speak("Good evening!")

    speak(" Hermione is here to help")

def location():
    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode("Gomti Nagar Lucknow")
    speak(getLoc.address)
 

    speak("Latitude = ", getLoc.latitude, "\n")
    speak("Longitude = ", getLoc.longitude)



def came():
    # define a video capture object
   vid = cv2.VideoCapture(0)

   while(True):
    ret, frame = vid.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    vid.release()
    cv2.destroyAllWindows()
    
		
    
	



def news():
    url = 'https://www.bbc.com/news'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find('body').find_all('h3')
    for x in headlines:
        speak(x.text.strip())
        #res = x.text.strip()
	   



def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower() # to match cases in query

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Scanning Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'what can you do for me' in query:
            speak(f"I can tell you weather")
            speak(f"I can play music")
            speak(f"I can tell you location")
            speak(f"I can tell you the news")
    



        elif 'how is the weather' in query:
            webbrowser.open("https://weather.com/en-IN/weather/today/l/26.85,80.95?par=google")

        elif 'play music' in query:
            fav_music = 'C:\\Users\\Yash Pratap Singh\\Desktop\\java(vs)\\JavaScript\\Spotify Clone\\songs'
            songs = os.listdir(fav_music)
            print(songs)
            os.startfile(os.path.join(fav_music, songs[2]))

        elif 'the time' in query:
            stTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {stTime}")


        elif 'what is my location' in query:
            location()


        elif 'how do i look' in query:
            speak(f"see for yourself")
            came()
        



        elif 'tell me the news' in query:
            news()
            

        elif 'open vs code' in query:
            codePath = "C:\\Users\\Yash Pratap Singh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'stop' in query:
            exit()


