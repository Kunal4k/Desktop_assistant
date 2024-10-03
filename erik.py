import datetime
import os
import webbrowser
import speech_recognition as sr
import pyttsx3
import wikipedia
import smtplib
# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am E.R.I.K Sir. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    # Correct usage of Microphone as context manager
    with sr.Microphone() as source:  # Fixed this line
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please.....")
        return "None"
    return query
def sendEmail(to,content):
     server=smtplib.SMTP('smtp.gmail.com',587)
     server.ehlo()
     server.starttls()
     server.login('youremail@gmail.com', 'your-password-here')
     server.sendmail('youremail@gmail.com', to, content)
     server.close()
if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:
      query=takeCommand().lower()
      if 'wikipedia' in query:
          speak('Searching Wikipedia.....')
          query=query.replace("wikipedia","")
          results=wikipedia.summary(query,sentences=2)
          speak("According to Wikipedia")
          print(results)
          speak(results)
      elif 'open youtube' in query:
          webbrowser.open("youtube.com")
      elif 'open google' in query:
          webbrowser.open("google.com")
      elif 'open stackoverflow' in query:
          webbrowser.open("stackoverflow.com")
      elif 'play music' in query:
          music_dir="F:\Songs"
          songs=os.listdir(music_dir)
          print(songs)
          os.startfile(os.path.join(music_dir,songs[0]))
      elif 'the time' in query:
          strTime=datetime.datetime.now().strftime("%H:%M:%S")
          speak(f"Sir, The time is {strTime}")
      elif 'open code' in query:
          codePath="C:\\Users\\Kajol\\AppData\\Local\\Programs\\Microsoft VS Code"
          os.startfile(codePath)
      elif 'email to kunal' in query:
        try:
            speak("What should I say")
            content=takeCommand()
            to="lloyd7th011gmail.com"
            sendEmail(to,content)
            speak("Email has been sent!")
        except Exception as e:
            print(e)
            speak("Sorry my friend Kunal . I am not able to send this email")
      elif 'quit' in query or 'exit' in query or 'stop' in query:
            speak("Goodbye Sir! Have a nice day!")
        