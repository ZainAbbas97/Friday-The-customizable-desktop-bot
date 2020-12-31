#============================================================Friday=========================================================================







#============================================================Modules=======================================================================
import pyttsx3
from datetime import datetime
import pyaudio
import speech_recognition as sr
import webbrowser
import os
import pythoncom
import wikipedia
import subprocess
import time
#============================================================Voices====================================================================
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
#============================================================Speak function============================================================
#speak function....pronounce string passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()


#=============================================================speech to text===========================================================
r = sr.Recognizer()
mic = sr.Microphone(device_index=1) #my device index is 1, you have to put your device index
with mic as source:
    speak('Good day MASTER...How can i help you?')
    audio = r.listen(source) #take voice input from the microphone
print(r.recognize_google(audio)) #to print voice into text

now = datetime.now()
current_time = now.strftime("%A:%d:%B:%I:%M")


#=============================================================Query====================================================================
try:
    query = r.recognize_google(audio, language = 'en-in')
    print(f"user said: {query}\n")                
except Exception as e:
    speak('Im sorry can you repeat?')
    query = None
#============================================================Executing commands======================================================================
#============================================================Wikipedia=================================================================
if 'wikipedia' in query.lower():
        speak('Accessing wikipedia')
        query = query.replace('wikipedia', '')
        wik = wikipedia.summary(query, sentences =2)
        speak(wik)
    #==============================================================Youtube===============================================================
elif 'youtube' in query.lower():
    speak('Accessing Youtube')
    query = query.replace('search youtube for', '')
    url = 'https://www.youtube.com/results?search_query=' + query
    chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)
    #===============================================================Google=================================================================
elif 'google' in query.lower():
    speak('Accessing Google')
    query = query.replace('search google for', '')
    url = 'https://www.google.com/search?q=' + query
    chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)
    #===============================================================Discord====================================================================
elif 'discord' in query.lower():
    speak('Accessing discord')
    query = query.replace('discord', '')
    url = 'discord.com'
    chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)
    #================================================================Instagram==================================================================
elif 'intagram' in query.lower():
    speak('Accessing instagram')
    query = query.replace('instagram', '')
    url = 'instagram.com'
    chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)
    #==================================================================Facebook===================================================================
elif 'facebook' in query.lower():
    speak('Accessing facebook')
    query = query.replace('facebook', '')
    url = 'facebook.com'
    chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)
    #==================================================================Aliexpress===================================================================
elif 'aliexpress' in query.lower():
    speak('Accessing aliexpress')
    query = query.replace('search aliexpress for', '')
    url = 'https://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20191231091831&SearchText=' + query
    chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)
    #================================================================Spotify====================================================================
elif 'spotify' in query.lower():
    speak('Launching Spotify')
    song = os.startfile('C:\\Users\\Zayn\\AppData\\Roaming\\Spotify\\Spotify.exe')
    #==================================================================Rocket league=============================================================
elif 'rocket league' in query.lower():
    speak('Launching Rocket league')
    rl = subprocess.call('Z:\\SteamLibrary\\steamapps\\common\\rocketleague\\Binaries\\Win64\\RocketLeague.exe')
    #==================================================================Apex Legends=============================================================
elif 'apex legends' in query.lower():
    speak('Launching Apex')
    Ax = subprocess.call('Z:\\Origin stuff\\Apex\\r5apex.exe')
    #==================================================================Miinecraft========================================================
elif 'minecraft' in query.lower():
    speak('Launching Minecraft')
    mc = subprocess.call('C:\\Users\\Zayn\\AppData\\Roaming\\.minecraft\\TLauncher.exe')

    #==================================================================Intro=====================================================================
elif 'introduce' in query.lower():
    speak('I am Friday your personal Ai assistant .. I was developed by Master Zayn for the purpose of serving him as his own personal Alexa type bot in 2020 .. To wake me up just say my name Friday and i shall be ready to serve you .. To use me to open any website or app just say app or site name and i shall acess the desired website .. Im sorry for any inconvenience as im still in the developing stage .. Thats all .. Have fun!')

    #==================================================================DateTime=====================================================================
elif 'time' in query.lower():
    speak(current_time)
elif 'exit' in query:
    speak('Initiating exit sequence...!')
    SystemExit
else:
    speak('Sorry im not programmed to do more yet .. Sad .. i know..')


