import time,random

class Left_button:
	ISDEBUG = True
	#Define the type of the Button simulator. Values:
	#Circulartime: it changes the value every second * BUTTONPRESSTIME 
	#Random: it returns pressed with a probability stated in BUTTON PROBABILITY value
	#Consol: it asks for a value from the console.
	#BUTTONTYPE = "Circulartime"
	BUTTONTYPE = "Random"
	#BUTTONTYPE = "Consol"
	BUTTONPRESSTIME = 3
	BUTTONPROBABILITY = 80

	def __init__(self):
		self.buttonlast = 0
		if(self.ISDEBUG):print("Left button is initialised in debug mode. Simulation Button type:",self.BUTTONTYPE ," change at spike.left_button.py ")
		self.time = time.time()

	def remap(self,x, in_min, in_max, out_min, out_max):
		return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

	def wait_until_pressed(self):
		if(self.ISDEBUG):
			print("wait_until_pressed: Waits until the left button is pressed.")
		if(self.BUTTONTYPE == "Random"):
			randnum =0
			while randnum < self.BUTTONPROBABILITY:
				randnum = self.remap(random.getrandbits(8), 0, 255, 0, 100)
				if(self.ISDEBUG):print("press left button simulated random number:", str(randnum), " probability:", self.BUTTONPROBABILITY)
				time.sleep(1)
		elif(self.BUTTONTYPE == "Circulartime"):
			self.time = time.time()
			while time.time() - self.time < self.BUTTONPRESSTIME:
				if(self.ISDEBUG): print("Time remaining until simulated left button press :", str(1000 * self.BUTTONPRESSTIME - (time.time() - self.time)))
		elif(self.BUTTONTYPE == "Consol"):
			while input("press 'p' to simulate a left button press :") != "p":
				pass
				if(self.ISDEBUG):print("push the left button")
		if(self.ISDEBUG):print("left button is pressed")

	def wait_until_released(self):
		if(self.ISDEBUG):print("wait_until_released: Waits until the left button is released.")
		if(self.BUTTONTYPE == "Random"):
			randnum =0
			while randnum < self.BUTTONPROBABILITY:
				randnum = self.remap(random.getrandbits(8), 0, 255, 0, 100)
				if(self.ISDEBUG):print("releas left button simulated random number:", str(randnum), " probability:", self.BUTTONPROBABILITY)
				time.sleep(1)
		elif(self.BUTTONTYPE == "Circulartime"):
			self.time = time.time()
			while time.time() - self.time <  self.BUTTONPRESSTIME:
				if(self.ISDEBUG):print("Time remaining until simulated left button released :", str(1000 * self.BUTTONPRESSTIME - (time.time() - self.time)))
		elif(self.BUTTONTYPE == "Consol"):
			while input("press 'r' to simulate a left button release: ") != "r":
				pass
		if(self.ISDEBUG):print("left button is released")

	def was_pressed(self):
		if(self.ISDEBUG):print("Tests to see whether the left button has been pressed since the last time this method called.")
		if(self.BUTTONTYPE == "Random"):
			randnum = self.remap(random.getrandbits(8), 0, 255, 0, 100)
			if(self.ISDEBUG):print("Simulated left button was pressed if random number:", str(randnum), " is higher then probability:", self.BUTTONPROBABILITY)
			if randnum < self.BUTTONPROBABILITY:
				if(self.ISDEBUG):print("Simulated left button was not pressed")
				return False
			else:
				if(self.ISDEBUG):print("Simulated left button was pressed")
				return True
		elif(self.BUTTONTYPE == "Circulartime"):
			if time.time() - self.time >  self.BUTTONPRESSTIME:
				if(self.ISDEBUG):print("Time is up and the simulated left button is pressed time ago:", str((time.time() - self.time)-1000 * self.BUTTONPRESSTIME))
				self.time = time.time()
				return True
			else:
				if(self.ISDEBUG):print("Simulated left button press will come in :", str(1000 * self.BUTTONPRESSTIME- (time.time() - self.time)), " sec")
				return False
				
		elif(self.BUTTONTYPE == "Consol"):
			readcharacter = input("press 'y' to simulate that the left button was pressed 'n' if it was not (y/n): ")
			if(readcharacter =="y"):
				return True
			if(readcharacter =="n"):
				return False


	def is_pressed(self):
		if(self.ISDEBUG):print("Tests whether the left button is pressed.")
		if(self.BUTTONTYPE == "Random"):
			randnum = self.remap(random.getrandbits(8), 0, 255, 0, 100)
			if(self.ISDEBUG):print("Simulated left button is pressed if random number:", str(randnum), " higher then probability:", self.BUTTONPROBABILITY)
			if randnum < self.BUTTONPROBABILITY:
				if(self.ISDEBUG):print("Simulated left button is not pressed")
				return False
			else:
				if(self.ISDEBUG):print("Simulated left button is pressed")
				return True
		elif(self.BUTTONTYPE == "Circulartime"):
			if time.time() - self.time >  self.BUTTONPRESSTIME:
				if(self.ISDEBUG):print("Time is up and the simulated left button is pressed time ago:", str((time.time() - self.time)-1000 * self.BUTTONPRESSTIME))
				self.time = time.time()
				return True
			else:
				if(self.ISDEBUG):print("Simulated left button press will come in :", str(1000 * self.BUTTONPRESSTIME- (time.time() - self.time)), " sec")
				return False
				
		elif(self.BUTTONTYPE == "Consol"):
			readcharacter = input("press 'y' to simulate that the left button is pressed 'n' if it is not (y/n): ")
			if(readcharacter =="y"):
				return True
			if(readcharacter =="n"):
				return False
