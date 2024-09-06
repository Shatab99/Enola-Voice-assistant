from functions import song
from functions import sing,song,speak,wishMe,takeCommand,askAbout,wiki,knock,flirt

# if 'from wikipedia' in query:
#             speak('searching wikipedia. please wait...')
#             query = query.replace('wikipedia', "")
#             result = wikipedia.summary(query, sentences=1)
#             speak(result)

#         elif 'open youtube' in query:
#             webbrowser.get(
#                 "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open('youtube.com')

#         elif 'play music' in query:
#             music_dir = 'D:\\music\\audio'
#             songs = os.listdir(music_dir)
#             print("Playiing sir")
#             os.startfile(os.path.join(music_dir, songs[0]))
#         elif 'open music' in query:
#             music_dir = 'D:\\music\\audio'
#             songs = os.listdir(music_dir)
#             print("Playing Sir!!")
#             os.startfile(os.path.join(music_dir, songs[0]))
#         elif 'the time' in query:
#             strtime = datetime.datetime.now().strftime("%I:%M %p")
#             speak(f"Sir, the time is {strtime}")
#         elif 'open google' in query:
#             webbrowser.get(
#                 "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("google.com")
#         elif 'open browser' in query:
#             webbrowser.get(
#                 "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("google.com")
#         elif 'hello' in query:
#             speak('i had already introduced myself')
#         # elif 'my name' in query:
#         #     name()

#         elif 'your name' in query:
#             speak("Enola. sir!!")
#             speak("what's your name?sir! ")
#             usnm = takeCommand()
#             # speak(usnm)
#             speak("that's a nice name sir!!")
#         elif 'how are' in query:
#             askAbout()
#         elif 'about' in query:
#             wiki()   
#         elif 'knock' in query:
#             knock()
#         elif 'beautiful' in query:
#             flirt()   
#         elif 'song' in query:
#             song()
#         elif 'sing' in query:
#             sing()


data =[
    {"req": "hello", "res" : "hello , how are you ? "}
]