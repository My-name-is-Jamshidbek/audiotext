import speech_recognition as sr

# Create a Recognizer object
r = sr.Recognizer()

# Read the audio file
with sr.AudioFile('voice_message.wav') as source:
    audio = r.record(source)

# Transcribe the audio
text = r.recognize_google(audio)
print(text)
