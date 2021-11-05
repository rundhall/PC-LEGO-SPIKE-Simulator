import random,time
from spike import simulator

class DistanceSensor:
	#If ISDEBUG is true. then all modules send debug information through console
	ISDEBUG = True
	#Define the type of the Distance simulator. Values:
	#Circular: it increases the return value by SIMULATORCHANGE, after reaching maximum value decreases by SIMULATORCHANGE every time it is called in while function it changes the value every second * SIMULATORTIME
	#Random: it returns random distance value
	#Consol: it asks for a value from the console.
	#SIMULATORTYPE = "Circular"
	SIMULATORTYPE = "Random"
	#SIMULATORTYPE = "Consol"
	
	#In Circular mode this is the time between changes
	SIMULATORTIME = 3
	#In Circular mode this the amount the distance value will change every period.
	SIMULATORCHANGE = 10
	#If the measured, simulated value is higher than SIMULATORSWITCHMAX value then the while cycle is over or a press event occurs. (Inverse setting is possible)
	SIMULATORSWITCHMAX=80
	#If the measured, simulated value is lower than SIMULATORSWITCHMAX value then the while cycle is over or a press event occurs. (Inverse setting is possible)
	SIMULATORSWITCHMIN=0
	
	def __init__(self,port):
		self.port = port
		self.distance_cm =0
		self.distance_inches =0
		self.distance_percentage =0
		self.distance_cm_direction = True
		self.distance_inches_direction = True
		self.distance_percentage_direction = True
		self.simulator = simulator.Simulator()
		if(self.ISDEBUG):print("Distance sensor is initialised in debug mode. Button type:",self.SIMULATORTYPE ," change at spike.distance_sensor.py ")
  
	def light_up_all(self,brightness=100):
		if(self.ISDEBUG):print("Lights up all of the lights on the Distance Sensor at the specified brightness.brightness:",str(brightness))
		print("Simulated distance sensor light up the sensor light with the brightness:",str(brightness))

	def light_up(self,right_top, left_top, right_bottom, left_bottom):
		if(self.ISDEBUG):print("Sets the brightness of the individual lights on the Distance Sensor. Light up by: right_top:",right_top," left_top:",left_top," right_bottom:",right_bottom," left_bottom:", left_bottom)
		print("Simulated distance sensor light up by: right_top:",right_top," left_top:",left_top," right_bottom:",right_bottom," left_bottom:", left_bottom)
		

	'''
	get_distance_cm: Retrieves the measured distance in centimeters.
	Parameters:	short_range
	Whether or not to use short range mode. Short range mode increases accuracy, but it can only detect nearby objects.
	Type	:	boolean
	Values	:	True or False
	Default	:	False
	Returns	The measured distance or "none" if the distance can't be measured.
	Type	:	float (decimal number)
	Values	:	0 to 200 cm'''
	
	def get_distance_cm(self,short_range=False):
		if(self.ISDEBUG):print("Retrieves the measured distance in centimeters.")
		self.distance_cm, self.distance_cm_direction = self.simulator.get_new_value(issimulation=True,
																			 simulationtype=self.SIMULATORTYPE,
																			 isdebug=self.ISDEBUG,
																			 actualvalue= self.distance_cm,
																			 newreading= None,
																			 minvalue= 0,
																			 maxvalue= 200,
																			 name= "distance sensor distance_cm",
																			 direction= self.distance_cm_direction,
																			 change= self.SIMULATORCHANGE,
																			 iswait= False,
																			 switch_min= self.SIMULATORSWITCHMIN,
																			 switch_max=self.SIMULATORSWITCHMAX,
																			 isextern= False,
																			 minreading=0,
																			 maxreading=200)
		return self.distance_cm
		
	def get_distance_inches(self,short_range=False):
		if(self.ISDEBUG):print("Retrieves the measured distance in inches.")
		self.distance_inches, self.distance_inches_direction = self.simulator.get_new_value(issimulation=True,
																	 simulationtype=self.SIMULATORTYPE,
																	 isdebug=self.ISDEBUG,
																	 actualvalue= self.distance_inches,
																	 newreading= None,
																	 minvalue= 0,
																	 maxvalue= 79,
																	 name= "distance sensor distance_inches",
																	 direction= self.distance_inches_direction,
																	 change= self.SIMULATORCHANGE,
																	 iswait= False,
																	 switch_min= self.SIMULATORSWITCHMIN,
																	 switch_max=self.SIMULATORSWITCHMAX,
																	 isextern= False,
																	 minreading=0,
																	 maxreading=200)
		return self.distance_inches
		
	def get_distance_percentage(self,short_range=False):
		if(self.ISDEBUG):print("Retrieves the measured distance as a percentage.")
		self.distance_percentage, self.distance_percentage_direction = self.simulator.get_new_value(issimulation=True,
																	 simulationtype=self.SIMULATORTYPE,
																	 isdebug=self.ISDEBUG,
																	 actualvalue= self.distance_percentage,
																	 newreading= None,
																	 minvalue= 0,
																	 maxvalue= 100,
																	 name= "distance sensor distance_percentage",
																	 direction= self.distance_percentage_direction,
																	 change= self.SIMULATORCHANGE,
																	 iswait= False,
																	 switch_min= self.SIMULATORSWITCHMIN,
																	 switch_max=self.SIMULATORSWITCHMAX,
																	 isextern= False,
																	 minreading=0,
																	 maxreading=200)
		return self.distance_percentage
   
   
   
	def wait_for_distance_farther_than(self,distance=100, unit='cm', short_range=False):
		if(self.ISDEBUG):print("distance_sensor wait_for_distance_farther_than() Waits until the measured distance is farther than the specified distance.")
		maxvalue_unit = 100
		if unit == "cm":
			maxvalue_unit = 200
		if unit == "in":
			maxvalue_unit = 78
		if unit == "%":
			maxvalue_unit = 100
		runwhile = True
		self.distance_cm, self.distance_cm_direction = self.simulator.get_new_value(   issimulation=True,
																	 simulationtype=self.SIMULATORTYPE,
																	 isdebug=self.ISDEBUG,
																	 actualvalue= self.distance_cm,
																	 newreading= None,
																	 minvalue= 0,
																	 maxvalue= maxvalue_unit,
																	 name= "distance farther than",
																	 direction= self.distance_cm_direction,
																	 change= self.SIMULATORCHANGE,
																	 iswait= True,
																	 switch_min= 0,
																	 switch_max=distance,
																	 isextern= False,
																	 time_period= self.SIMULATORTIME,
																	 minreading=0,
																	 maxreading=200)
		return self.distance_cm
	
	def wait_for_distance_closer_than(self,distance=100, unit='cm', short_range=False):
		maxvalue_unit = 100
		if unit == "cm":
			maxvalue_unit = 200
		if unit == "in":
			maxvalue_unit = 78
		if unit == "%":
			maxvalue_unit = 100
		runwhile = True
		self.distance_cm, self.distance_cm_direction = self.simulator.get_new_value(   issimulation=True,
																	 simulationtype=self.SIMULATORTYPE,
																	 isdebug=self.ISDEBUG,
																	 actualvalue= self.distance_cm,
																	 newreading= None,
																	 minvalue= 0,
																	 maxvalue= maxvalue_unit,
																	 name= "distance closer than",
																	 direction= self.distance_cm_direction,
																	 change= self.SIMULATORCHANGE,
																	 iswait= True,
																	 switch_min= 0,
																	 switch_max=distance,
																	 isextern= True,
																	 time_period= self.SIMULATORTIME,
																	 minreading=0,
																	 maxreading=200)
		return self.distance_cm
