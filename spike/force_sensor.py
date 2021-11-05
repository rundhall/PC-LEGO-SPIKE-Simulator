from spike import simulator
import time

class ForceSensor:
	#If ISDEBUG is true. then all modules send debug information through console
	ISDEBUG = True
	#Define the type of the Force Sensor simulator. Values:
	#Circular: it increases the return value by SIMULATORCHANGE, after reaching maximum value decreases by SIMULATORCHANGE every time it is called in while function it changes the value every second * SIMULATORTIME
	#Random: it returns with a random number 
	#Consol: it asks for a value from the console.
	#SIMULATORTYPE = "Circular"
	SIMULATORTYPE = "Random"
	#SIMULATORTYPE = "Consol"
	#The return value of the Force Sensor will change by this number
	SIMULATORCHANGE = 10
	#In Circular mode in wait functions this is the time in seconds between changes
	SIMULATORTIME = 3
	#If the measured, simulated value is higher than SIMULATORSWITCHMAX value then the while cycle is over or a press event occurs. (Inverse setting is possible)
	SIMULATORSWITCHMAX=80
	#If the measured, simulated value is lower than SIMULATORSWITCHMAX value then the while cycle is over or a press event occurs. (Inverse setting is possible)
	SIMULATORSWITCHMIN=0
	
	def __init__(self,port):
		self.port = port
		self.newton = 0
		self.newton_direction = True
		self.percentage = 0
		self.percentage_direction = True
		self.simulator = simulator.Simulator()
		if(self.ISDEBUG):print("Force sensor is initialised in debug mode. Simulation sensor type:",self.SIMULATORTYPE ," change at spike.force_sensor.py ")

	def get_new_measured_value(self,multipier=1):
		return None
	
	def remap(self,x, in_min, in_max, out_min, out_max):
		return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
	
	def get_force_newton(self):
		if(self.ISDEBUG):print("Retrieves the measured force, in newtons.")
		self.newton, self.newton_direction = self.simulator.get_new_value(issimulation=True,
																	 simulationtype=self.SIMULATORTYPE,
																	 isdebug=self.ISDEBUG,
																	 actualvalue= self.newton,
																	 newreading= self.get_new_measured_value(),
																	 minvalue= 0,
																	 maxvalue= 10,
																	 name= "force sensor newton",
																	 direction= self.newton_direction,
																	 change= self.SIMULATORCHANGE,
																	 iswait= False,
																	 switch_min= self.SIMULATORSWITCHMIN,
																	 switch_max=self.SIMULATORSWITCHMAX,
																	 isextern= False,
																	 minreading=0,
																	 maxreading=4095)
		return self.newton
	
	def get_force_percentage(self):
		if(self.ISDEBUG):print("Retrieves the measured force, in percentages.")
		self.percentage, self.percentage_direction = self.simulator.get_new_value(issimulation=True,
																	 simulationtype=self.SIMULATORTYPE,
																	 isdebug=self.ISDEBUG,
																	 actualvalue= self.percentage,
																	 newreading= self.get_new_measured_value(),
																	 minvalue= 0,
																	 maxvalue= 100,
																	 name= "force sensor percentage",
																	 direction= self.percentage_direction,
																	 change= self.SIMULATORCHANGE,
																	 iswait= False,
																	 switch_min= self.SIMULATORSWITCHMIN,
																	 switch_max=self.SIMULATORSWITCHMAX,
																	 isextern= False,
																	 minreading=0,
																	 maxreading=4095)
		return self.percentage
		
	def is_pressed(self):
		if(self.ISDEBUG):print("Tests whether the button on the force sensor is pressed.")
		self.percentage, self.percentage_direction = self.simulator.get_new_value(issimulation=True,
																	 simulationtype=self.SIMULATORTYPE,
																	 isdebug=self.ISDEBUG,
																	 actualvalue= self.percentage,
																	 newreading= self.get_new_measured_value(),
																	 minvalue= 0,
																	 maxvalue= 100,
																	 name= "force sensor percentage",
																	 direction= self.percentage_direction,
																	 change= self.SIMULATORCHANGE,
																	 iswait= False,
																	 switch_min= self.SIMULATORSWITCHMIN,
																	 switch_max=self.SIMULATORSWITCHMAX,
																	 isextern= False,
																	 minreading=0,
																	 maxreading=4095)
		if self.percentage < self.SIMULATORSWITCHMAX :
			if(self.ISDEBUG):
				print("force sensor button is pressed")
				return True
			else:
				return False

	def wait_until_pressed(self):
		if(self.ISDEBUG):print("Waits until the Force Sensor is pressed.")
		runwhile = True
		while runwhile:
			if not True:
				newreading = self.adc.read()
			else:
				newreading = None
			self.percentage, self.percentage_direction = self.simulator.get_new_value(   issimulation=True,
																	 simulationtype=self.SIMULATORTYPE,
																	 isdebug=self.ISDEBUG,
																	 actualvalue= self.percentage,
																	 newreading= newreading,
																	 minvalue= 0,
																	 maxvalue= 100,
																	 name= "distance closer than",
																	 direction= self.percentage_direction,
																	 change= self.SIMULATORCHANGE,
																	 iswait= True,
																	 switch_min= self.SIMULATORSWITCHMIN,
																	 switch_max= self.SIMULATORSWITCHMAX,
																	 isextern= True,
																	 time_period= self.SIMULATORTIME,
																	 minreading=0,
																	 maxreading=4095)
			if(self.ISDEBUG):print("Do changes at force sensor new reading:", str(self.percentage), " to exit it should be lower then:", self.SIMULATORSWITCHMIN , " or it should be higher then:", self.SIMULATORSWITCHMAX )
			if self.percentage < self.SIMULATORSWITCHMIN or self.percentage > self.SIMULATORSWITCHMAX : 
				runwhile = False
			else:
				time.sleep(1)
	
	def wait_until_released(self):
		if(self.ISDEBUG):print("Waits until the Force Sensor is released.")
		runwhile = True
		while runwhile:
			if not True:
				newreading = self.adc.read()
			else:
				newreading = None
			self.percentage, self.percentage_direction = self.simulator.get_new_value(   issimulation=True,
																	 simulationtype=self.SIMULATORTYPE,
																	 isdebug=self.ISDEBUG,
																	 actualvalue= self.percentage,
																	 newreading= self.get_new_measured_value(),
																	 minvalue= 0,
																	 maxvalue= 100,
																	 name= "distance closer than",
																	 direction= self.percentage_direction,
																	 change= self.SIMULATORCHANGE,
																	 iswait= True,
																	 switch_min= self.SIMULATORSWITCHMIN,
																	 switch_max= self.SIMULATORSWITCHMAX,
																	 isextern= False,
																	 time_period= self.SIMULATORTIME,
																	 minreading=0,
																	 maxreading=4095)
			if(self.ISDEBUG):print("Do changes at force sensor new reading:", str(self.percentage), " to exit it should be higher or equal then:", self.SIMULATORSWITCHMIN , " or it should be lower or equal then:", self.SIMULATORSWITCHMAX )
			if self.percentage >= self.SIMULATORSWITCHMIN and self.percentage <= self.SIMULATORSWITCHMAX : 
				runwhile = False
			else:
				time.sleep(1)