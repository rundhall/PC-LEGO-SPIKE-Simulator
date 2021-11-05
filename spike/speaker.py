import time


class Speaker:
	#If ISDEBUG is true. then all modules send debug information through console
	ISDEBUG = True

	def __init__(self):
		if(self.ISDEBUG):print("Speaker is initialised in debug mode. in simulation mode change at spike.speaker.py ")
		self.volume = 0
   
	'''beep(note=60, seconds=0.2)
	Plays a beep on the Hub.
	Your program will not continue until seconds have passed.
	Parameters note The MIDI note number.
	Type : float (decimal number)
	Values : 44 to 123 ("60" is the middle C note)
	Default : 60 (middle C note) seconds
	The duration of the beep, specified in seconds.
	Type : float (decimal number)
	Values: any values
	Default: 0.2 seconds
	Errors
	TypeError
	note is not an integer or seconds is not a number.
	ValueError
	note is not within the allowed range of 44-123'''
	def beep(self,note = 60,seconds=0.2):
		if(self.ISDEBUG):print("start_beep: Start beep.")
		print (str(note) + " note starts beeping for "+str(seconds)+" sec") 
		time.sleep(seconds)
		print (str(note) + " note is finished") 
			
	def start_beep(self):
		if(self.ISDEBUG):print("start_beep: Start beep.")
		
	def stop(self):
		if(self.ISDEBUG):print("stop: stop beep.")
	
	def set_volume(self,volume=50):
		if(self.ISDEBUG):print("old volume: ",str(self.volume)," changed to new volume:", volume)
		self.volume = volume
	
	def get_volume(self):
		if(self.ISDEBUG):print("get stored volume:", self.volume)
		return self.volume