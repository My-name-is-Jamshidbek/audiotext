import speech_recognition as sr

# Create a Recognizer object
r = sr.Recognizer()

# Start listening to the microphone
with sr.Microphone() as source:
    print("Speak now:")
    audio = r.listen(source)

# Transcribe the audio
text = r.recognize_google(audio)
print(text)
