# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""




import win32com.client
speaker = win32com.client.Dispatch ( "SAPI.SpVoice" )
speaker.Speak ( "Welcome to world of Artificial Intelligence" )


import urllib.request
import urllib.parse
import re
import sys


import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import webbrowser



def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")

    os.system("mpg321 audio.mp3")
 
def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
 
    # Speech recognition using Google Speech Recognition

    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data
 
def jarvis(data):
    if "how are you" in data:
        speaker.Speak("i am fine Sir, thank you")
        os.system("say 'hello world'")
 
    if "what time is it" in data:
        speaker.Speak(ctime())
 
    if "hi Jarvis" in data:
        speaker.Speak("Yes Sir ! i am awake")
   # if "where is" in data:
    #    
      #  speak("Hold on Frank, I will show you where " + location + " is.")
       # os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
       


    if "can you play a song for me" in data:
        speaker.Speak("Ok Sir, Please tell the name of the song")
        
        
        data = recordAudio()
     #   location = data[2]
        query_string = urllib.parse.urlencode({"search_query" : data})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        webbrowser.get("C:/Users/Dell/AppData/Local/Google/Chrome/Application/chrome.exe %s").open("http://www.youtube.com/watch?v=" + search_results[0])
        return 
    
        
    
    if "close the song " or "stop the song"  in data:
        speaker.Speak("closing sir")
        os.system("taskkill /im chrome.exe /f")
        
    if "goodbye Jarvis" in data:
        speaker.Speak("good bye Saksham")
        sys.exit()
        
    if "shutdown Jarvis" in data: 
        import subprocess
        subprocess.call(["shutdown", "-f", "-s", "-t", "60"])
     
     
        
 
# initialization
time.sleep(2)
speak("Hello there, what can I do for you?")
speaker.Speak("Hello , what can I do for you?")
while 1:
    data = recordAudio()
    jarvis(data)