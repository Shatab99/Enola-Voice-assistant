from app import speak,takeCommand
import datetime
import wikipediaapi as wikipedia


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good morning sir")
    elif hour >= 12 and hour <= 18:
        speak("Good afternoon sir")
    else:
        speak("Good evening sir")

    speak(" I am enola. how can I help you !!!")


def name():
    speak("sorry sir!! I don't know your name. please tell me your name!!")
    name = takeCommand()
    speak('so your name is')
    speak(name)
    speak("that's a nice name !!")
    # speak("your name is Shahriar Shatab")


def askAbout():
    speak("I am fine sir . How about you ?")
    ask = takeCommand()
    if 'am' in ask:
        speak("that's great sir !!")
    elif 'not ' in ask:
        speak("ow I am really sorry for your condition !!")
    elif 'ill' in ask:
        speak("ow I am really sorry for your condition !!")

def wiki():
    speak("I can not tell about this . should I search it from wikipedia")
    wiki = takeCommand()
    if 'yes' in wiki:
        speak('searching wikipedia. please wait...')
        wiki = wiki.replace('wikipedia', "")
        result = wikipedia.summary(query, sentences=1) # type: ignore
        speak(result)
    elif 'No' in wiki:
        speak("Ok sir!!Your Wish!!") 

def knock():
    speak("who is there?")
    knock = takeCommand()
    if 'lover' in knock:
        speak("L M A O!!")
    else:
        speak("sorry!! I do not understand!")


def flirt():
    speak("Who told You that I am beautiful ??")  
    flirt =takeCommand()
    if 'crushed' in flirt:
        speak("Wow !! You are handsome too!!but I have some one!!")
      

def song():
    speak("ok")
    song = '''
                    My life is brilliant
                    My love is pure
                    I saw an angel
                    Of that I'm sure
                    She smiled at me on the subway
                    She was with another man
                    But I won't lose no sleep on that
                    'Cause I've got a plan
                    You're beautiful
                    You're beautiful
                    You're beautiful, it's true
                    I saw your face in a crowded place
                    And I don't know what to do
                    'Cause I'll never be with you'''
    speak(song) 


def sing():
    speak("Yeah!! Of course!! Should I sing??")
    sing = takeCommand()
    if 'ok' in sing:
        sng = ''' My life is brilliant
                    My love is pure
                    I saw an angel
                    Of that I'm sure
                    She smiled at me on the subway
                    She was with another man
                    But I won't lose no sleep on that
                    'Cause I've got a plan
                    You're beautiful
                    You're beautiful
                    You're beautiful, it's true
                    I saw your face in a crowded place
                    And I don't know what to do
                    'Cause I'll never be with you'''
        speak(sng)
    if 'yes' in sing:
        sng = ''' My life is brilliant,
                    My love is pure,
                    I saw an angel,
                    Of that I'm sure,
                    She smiled at me on the subway...
                    She was with another man..
                    But I won't lose no sleep on that,
                    'Cause I've got a plan..
                    You're beautiful,
                    You're beautiful,
                    You're beautiful, it's true...
                    I saw your face in a crowded place,
                    And I don't know what to do..
                    'Cause I'll never, be with you'''
        speak(sng)    
    else:
        speak("ok")