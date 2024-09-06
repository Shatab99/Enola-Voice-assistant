import datetime
import wikipediaapi as wikipedia
import webbrowser
import os
from functions import speak,wishMe,takeCommand
from app import fetchCommand
from EnolnaData import data


def enolaTalk(command, response):
    if command in query :
        speak(response)

flag = False


if __name__ == "__main__":
    print("Enable Net connection for Better Experience!!!!")
    wishMe() 
    while True:
    # if 1:
        query = takeCommand().lower()
        for coms in data:
            if fetchCommand(coms['req'],coms['res'], query):
                flag = True
                break
    
        if not flag:
            speak("Sorry , I can not understand !")
        
