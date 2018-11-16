import speech_recognition as sr
AUDIO_FILE = ("gg.wav")
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
	audio = r.record(source)
try:
	print("The audio file contains: " + r.recognize_google(audio))
except sr.UnknownValueError:
	print("Google Speech Rcognition could not understand audio")
except sr.RequestError as e:
	print("could not request results from Google speech recognaition service; {0}".format(e))


  