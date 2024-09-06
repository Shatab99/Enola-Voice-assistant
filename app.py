import pyttsx3
import speech_recognition as sr


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty("rate")
engine.setProperty('voice', voices[1].id)
engine.setProperty("rate", 180)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def takeCommand():
    # It takes command from microphone and return strings
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.8
        r.energy_threshold = 800
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-bd')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        speak("Sorry!!! Please say that again....")
        print("Sorry!!! Please say that again....")
        return "None"
    return query


def fetchCommand(question, answer, query):
    if question in query :
        if callable(answer):
            answer()  # Call the function if it's callable
        else:
            speak(answer)
        return True
    return False