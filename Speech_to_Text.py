import speech_recognition as sr

# Create an object of recognizer
obj = sr.Recognizer()

with sr.Microphone() as sound:
  # Prompt user to start speaking 
  print("I am your script and listening you ... Please speak now...")
  
  # Listen to audio from microphone
  audio = obj.listen(sound)
  
  # Recognize speech using Google Web Speech API 
  query = obj.recognize_google(audio, language='en-IN')
  print("You said : ", query)