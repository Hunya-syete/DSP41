import speech_recognition as sr
import pyaudio

r = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Say something!")
        
        audio = r.listen(source, timeout=5)
        try:
          
            text = r.recognize_google(audio)
            print("You said: " + text)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == "__main__":

    listen()
