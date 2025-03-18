import speech_recognition as sr
from gtts import gTTS
import os

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    return recognizer.recognize_google(audio)

def text_to_speech(text):
    tts = gTTS(text)
    tts.save("output.mp3")
    os.system("mpg321 output.mp3")
