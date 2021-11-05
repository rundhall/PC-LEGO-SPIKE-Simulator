class Status_light:
	ISDEBUG = True
	#max LED number
	MAXLEDNUMBER = 8
	#actual LED ID
	LEDID = 0
	

	def __init__(self):
		if(self.ISDEBUG):print("Status light is initialised in debug mode. Simulation Maximum LED:",self.MAXLEDNUMBER ," change at spike.status_light.py ")
		print("Simulated status light ")

	def on(self,color='white'):
		if(self.ISDEBUG):print("Sets the color of the light to: ",color)
		print("Simulated status light is turned on with this color:",color)

	def off(self):
		if(self.ISDEBUG):print("Turns off the light.")
		print("Simulated status light is turned on with this color:",color)
		