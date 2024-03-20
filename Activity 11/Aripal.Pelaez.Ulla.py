import speech_recognition as sr

# Initialize recognizer
r = sr.Recognizer()

# Function to listen and recognize speech from microphone
def listen():
    with sr.Microphone() as source:
        print("What's up! Say something!")
        
        # Listen for audio for a specific duration (5 seconds)
        audio = r.listen(source, timeout=10)
        try:
            # Recognize speech using Google Speech Recognition
            text = r.recognize_google(audio)
            print("You said: " + text)
        except sr.UnknownValueError:
            print("Sorry I don't Undertand You")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Call the listen function to start speech recognition
listen()
