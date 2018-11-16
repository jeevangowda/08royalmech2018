import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source,duration=5)
	r.dynamic_energy_threshold = True
	print("say something!")
	audio = r.listen(source)
	try:
		print("You said: " + r.recognize_google(audio))
	except sr.UnknownvalueError:
		print("Google speech recognition could not understand audio")
	except sr.RequestError as e:
		print("could not request result from Google speech recognition service; {0}".format(e))