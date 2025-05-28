import speech_recognition as sr

# Initialize recognizer
r = sr.Recognizer()

# Load your WAV file
with sr.AudioFile("sample.wav") as source:
    audio = r.record(source)  # Read the entire audio file

# Recognize speech using Google Web Speech API
try:
    text = r.recognize_google(audio)
    print("Transcribed Text:")
    print(text)
except sr.UnknownValueError:
    print("Sorry, could not understand the audio.")
except sr.RequestError as e:
    print(f"Could not request results; {e}")
