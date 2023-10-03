import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Ma'am")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Ma'am")
    else:
        speak("Good Evening Ma'am") 
    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
    speak(f"The time is {strTime}")
if __name__ == "__main__":
    wishMe()