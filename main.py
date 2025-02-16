import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

#pip install pocketsphinx
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com/in/gokul-krishna-n-499b39256/")
    elif "open chatgpt" in c.lower():
        webbrowser.open("https://chatgpt.com/")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    else:
        # Let openAi handle the request
        #api_key = "   "
    

if __name__ == "__main__":
    speak("Initializing Jarvis...... ")
    while True:
        # listen for the wake word jarvis
        # obtain audio from the microphone
        r = sr.Recognizer()

        print("recognising....")
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            print(word)
            if(word.lower() == "jarvis"):
                speak("yeah")
                # Listen for the command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source,pharse_time_out=2)
                    command = r.recognize_google(audio)

                    processCommand("Hi")
        except Exception as e:
            print("Error; {0}".format(e))
