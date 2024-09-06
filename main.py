import wikipedia
from functions import speak,wishMe,takeCommand,wiki
from app import fetchCommand
from EnolnaData import data





if __name__ == "__main__":
    print("Enable Net connection for Better Experience!!!!")
    wishMe() 
    while True:
    # if 1:
        query = takeCommand().lower()
        
        if "from wikipedia" in query :
            speak('searching wikipedia. please wait...')
            query = query.replace('wikipedia', "")
            result = wikipedia.summary(query, sentences=1)
            speak(result) 
        
        for coms in data:
            fetchCommand(coms['req'],coms['res'], query)


        
