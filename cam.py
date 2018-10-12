import os
from time import sleep
def mymail():
	def takesnap():
		os.system("fswebcam -F 4 img/temp.jpg")
		return
		for i in range(10):
			takesnap()
			mymail()
			sleep(5)
