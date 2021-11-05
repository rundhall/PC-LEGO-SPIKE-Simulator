import time

class App:
	#If ISDEBUG is true. then all modules send debug information through console
	ISDEBUG = True
	
	def __init__(self):
		if(self.ISDEBUG):print("App is initialised in debug mode. Simulation change at spike.app.py ")
		
	def play_sound(self,musicname):
		if(self.ISDEBUG):print("Plays a sound from the device (i.e., tablet or computer).")
		print (musicname + " starts playing this sound for 3 sec") 
		time.sleep(1)
		print (musicname + " is played and it is over") 
		if(self.ISDEBUG):print("The played sound is over")

	def start_sound(self,musicname):
		if(self.ISDEBUG):print("Starts playing a sound from your device. The program will not wait for the sound to finish playing before proceeding to the next command.")
		print (musicname + " starts playing and continue") 
		time.sleep(1)
		if(self.ISDEBUG):print("The played sound is started and finish time is unknowened")
	
