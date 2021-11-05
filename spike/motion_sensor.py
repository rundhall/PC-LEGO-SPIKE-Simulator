from spike import simulator
import time

class Motion_sensor:
	 #If ISDEBUG is true. then all modules send debug information through console
	ISDEBUG = True
	#Define the type of the motion simulator. Values:
	#Circular: it increases the return value by SIMULATORCHANGE, after reaching maximum value decreases by SIMULATORCHANGE every time it is called in while function it changes the value every second * SIMULATORTIME
	#Random: it returns random motion value
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
	
	def __init__(self):
		self.gesture_array = [None,'shaken','tapped','doubletapped','falling']
		self.gesture_index = 0
		self.gesture_index_direction = True
		
		self.orientation_array = [None,'front','back','up','down','leftside','rightside']
		self.orientation_index = 0
		self.orientation_index_direction = True
		
		self.pitch_angle = 0
		self.pitch_angle_direction = True
		
		self.roll_angle = 0
		self.roll_angle_direction = True
		
		self.yaw_angle = 0
		self.yaw_angle_direction = True
				
		self.simulator = simulator.Simulator()
			  
		if(self.ISDEBUG):print("motion sensor is initialised in debug mode. Simulation motion sensor simulator type:",self.SIMULATORTYPE ," change at spike.motion_sensor.py ")
	
	def get_new_measured_value(self):
		return None

	def get_yaw_angle(self):
	   if(self.ISDEBUG):print("motion_sensor get_yaw_angle() Retrieves the Hub’s yaw angle.")
	   self.yaw_angle, self.yaw_angle_direction = self.simulator.get_new_value(issimulation=True,
																			 simulationtype=self.SIMULATORTYPE,
																			 isdebug=self.ISDEBUG,
																			 actualvalue= self.yaw_angle,
																			 newreading= -1,
																			 minvalue= -180,
																			 maxvalue= 180,
																			 name= "motion sensor yaw_angle",
																			 direction= self.yaw_angle_direction,
																			 change= self.SIMULATORCHANGE,
																			 iswait= False,
																			 switch_min= self.SIMULATORSWITCHMIN,
																			 switch_max=self.SIMULATORSWITCHMAX,
																			 isextern= False)
	   return self.yaw_angle
	
	def get_roll_angle(self):
	   if(self.ISDEBUG):print("motion sensor get_roll_angle() Retrieves the Hub’s roll angle.")
	   self.roll_angle, self.roll_angle_direction = self.simulator.get_new_value(issimulation=True,
																			 simulationtype=self.SIMULATORTYPE,
																			 isdebug=self.ISDEBUG,
																			 actualvalue= self.roll_angle,
																			 newreading= -1,
																			 minvalue= -180,
																			 maxvalue= 180,
																			 name= "motion sensor roll_angle",
																			 direction= self.roll_angle_direction,
																			 change= self.SIMULATORCHANGE,
																			 iswait= False,
																			 switch_min= self.SIMULATORSWITCHMIN,
																			 switch_max=self.SIMULATORSWITCHMAX,
																			 isextern= False)
	   return self.roll_angle
	
	def get_pitch_angle(self):
	   if(self.ISDEBUG):print("motion sensor get_pitch_angle() Retrieves the Hub’s pitch angle.")
	   self.pitch_angle, self.pitch_angle_direction = self.simulator.get_new_value(issimulation=True,
																			 simulationtype=self.SIMULATORTYPE,
																			 isdebug=self.ISDEBUG,
																			 actualvalue= self.pitch_angle,
																			 newreading= -1,
																			 minvalue= -180,
																			 maxvalue= 180,
																			 name= "motion sensor pitch_angle",
																			 direction= self.pitch_angle_direction,
																			 change= self.SIMULATORCHANGE,
																			 iswait= False,
																			 switch_min= self.SIMULATORSWITCHMIN,
																			 switch_max=self.SIMULATORSWITCHMAX,
																			 isextern= False)
	   return self.pitch_angle
	
	def get_gesture(self):
		if(self.ISDEBUG):print("motion sensor get_gesture() Retrieves the most recently-detected gesture.")
		self.gesture_index, self.gesture_index_direction = self.simulator.get_new_value(   issimulation=True,
																			 simulationtype=self.SIMULATORTYPE,
																			 isdebug=self.ISDEBUG,
																			 actualvalue= self.gesture_index,
																			 newreading= self.get_new_measured_value(),
																			 minvalue= 0,
																			 maxvalue= 4,
																			 name= "motion",
																			 direction= self.gesture_index_direction,
																			 change= 1,
																			 iswait= False,
																			 switch_min= self.SIMULATORSWITCHMIN,
																			 switch_max=self.SIMULATORSWITCHMAX,
																			 isextern= False,
																			 minreading=0,
																			 maxreading=1024)
		return self.gesture_array[self.gesture_index]
		
	def get_orientation(self):
		if(self.ISDEBUG):print("motion sensor get_orientation() Retrieves the Hub's current orientation.")
		self.orientation_index, self.orientation_index_direction = self.simulator.get_new_value(   issimulation=True,
																			 simulationtype=self.SIMULATORTYPE,
																			 isdebug=self.ISDEBUG,
																			 actualvalue= self.orientation_index,
																			 newreading= self.get_new_measured_value(),
																			 minvalue= 0,
																			 maxvalue= 6,
																			 name= "motion",
																			 direction= self.orientation_index_direction,
																			 change= 1,
																			 iswait= False,
																			 switch_min= self.SIMULATORSWITCHMIN,
																			 switch_max=self.SIMULATORSWITCHMAX,
																			 isextern= False,
																			 minreading=0,
																			 maxreading=1024)
		return self.orientation_array[self.orientation_index]
	
   
	
	def reset_yaw_angle(self):
		if(self.ISDEBUG):print("motion sensor reset_yaw_angle() Sets the yaw angle to 0.")
		self.yaw_angle = 0
		
	def light_up_all(self,brightness=100):
		if(self.ISDEBUG):print("motion sensor light_up_all() Lights up all of the lights on the motion Sensor at the specified brightness. brightness:",str(brightness))
	
	def wait_for_new_orientation(self):
		#next line is not correct implementation it should be changed later
		if not True: self.orientation_index = int(self.remap(self.sensor.get_values()['AcX'], 0, 1024, 0, 6))
		if(self.ISDEBUG):print("motion sensor wait_for_new_orientation() Waits until the Hub’s orientation changes. Orientation at start:",self.orientation_array[self.orientation_index])
		runwhile = True
		while runwhile:
			old_orientation_index = self.orientation_index
			if not True:
				#next line is not correct implementation it should be changed later
				newreading = self.sensor.get_values()['AcX']
			else:
				newreading = None
			self.orientation_index, self.orientation_index_direction = self.simulator.get_new_value(   issimulation=True,
																			 simulationtype=self.SIMULATORTYPE,
																			 isdebug=self.ISDEBUG,
																			 actualvalue= self.orientation_index,
																			 newreading= newreading,
																			 minvalue= 0,
																			 maxvalue= 6,
																			 name= "motion",
																			 direction= self.orientation_index_direction,
																			 change= self.SIMULATORCHANGE,
																			 iswait= True,
																			 switch_min= self.orientation_index,
																			 switch_max=self.orientation_index,
																			 isextern= True,
																			 time_period= self.SIMULATORTIME,
																			 minreading=0,
																			 maxreading=1024)
			if(self.ISDEBUG):print("Do changes at color sensor new reading:", str(self.orientation_index), " to exit it should be lower then:", self.orientation_index , " or it should be higher then:", self.orientation_index )
			if self.orientation_index > old_orientation_index or self.orientation_index < old_orientation_index:
				runwhile = False
			else:
				time.sleep(1)
			old_orientation_index = self.orientation_index
		return self.orientation_array[self.orientation_index]
	
	def wait_for_new_gesture(self):
		#next line is not correct implementation it should be changed later
		if not True: self.gesture_index = int(self.remap(self.sensor.get_values()['AcY'], 0, 1024, 0, 4))
		if(self.ISDEBUG):print("motion sensor wait_for_new_gesture() Waits until the Hub’s gesture changes. Gesture at start:",self.gesture_array[self.gesture_index])
		runwhile = True
		
		while runwhile:
			old_gesture_index = self.gesture_index
			if not True:
				#next line is not correct implementation it should be changed later
				newreading = self.sensor.get_values()['AcY']
			else:
				newreading = None
			self.gesture_index, self.gesture_index_direction = self.simulator.get_new_value(   issimulation=True,
																			 simulationtype=self.SIMULATORTYPE,
																			 isdebug=self.ISDEBUG,
																			 actualvalue= self.gesture_index,
																			 newreading= newreading,
																			 minvalue= 0,
																			 maxvalue= 4,
																			 name= "motion",
																			 direction= self.gesture_index_direction,
																			 change= self.SIMULATORCHANGE,
																			 iswait= True,
																			 switch_min= self.gesture_index,
																			 switch_max=self.gesture_index,
																			 isextern= True,
																			 time_period= self.SIMULATORTIME,
																			 minreading=0,
																			 maxreading=1024)
			if self.gesture_index > old_gesture_index or self.gesture_index < old_gesture_index:
				runwhile = False
			else:
				time.sleep(1)
			old_gesture_index = self.gesture_index
		return self.gesture_array[self.gesture_index]
	
	def remap(self,x, in_min, in_max, out_min, out_max):
		return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
	
	def was_gesture(self,gesture):
		if(self.ISDEBUG):print("motion sensor was_gesture(gesture) Tests whether a gesture has occurred since the last time was_gesture() was used, or since the beginning of the program (for the first use).")
		self.gesture_index, self.gesture_index_direction = self.simulator.get_new_value(   issimulation=True,
																			 simulationtype=self.SIMULATORTYPE,
																			 isdebug=self.ISDEBUG,
																			 actualvalue= self.gesture_index,
																			 newreading= self.get_new_measured_value(),
																			 minvalue= 0,
																			 maxvalue= 4,
																			 name= "motion",
																			 direction= self.gesture_index_direction,
																			 change= 1,
																			 iswait= False,
																			 switch_min= self.SIMULATORSWITCHMIN,
																			 switch_max=self.SIMULATORSWITCHMAX,
																			 isextern= False,
																			 minreading=0,
																			 maxreading=1024)
		if gesture == self.gesture_array[self.gesture_index]: 
			return True
		else:
			return False

