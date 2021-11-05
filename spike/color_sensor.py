from spike import simulator
import time
# or from spike.tcs34725 import TCS34725



class ColorSensor:
	 #If ISDEBUG is true. then all modules send debug information through console
	ISDEBUG = True
	#Define the type of the color simulator. Values:
	#Circular: it increases the return value by SIMULATORCHANGE, after reaching maximum value decreases by SIMULATORCHANGE every time it is called in while function it changes the value every second * SIMULATORTIME
	#Random: it returns random Color value
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
		self.colors_array = [None,'black','violet','blue','cyan','green','yellow','red','white']
		self.color_index = 0
		
		self.ambient_light = 0 #0..100
		self.reflected_light = 0 #0..100
		self.rgb_intensity = 0 #0..1024
		self.red = 0 #0..1024
		self.green = 0 #0..1024
		self.blue = 0 #0..1024
		self.ambient_light_direction = True 
		self.reflected_light_direction = True 
		self.rgb_intensity_direction = True 
		self.red_direction = True 
		self.green_direction = True 
		self.blue_direction = True
		self.color_index_direction = True
		self.simulator = simulator.Simulator()
		if(self.ISDEBUG):print("Color sensor is initialised in debug mode. Simulation:True Color sensor simulator type:",self.SIMULATORTYPE ," change at spike.color_sensor.py ")
	   
	def get_ambient_light(self):
	   if(self.ISDEBUG):print("Color sensor get_ambient_light() Retrieves the intensity of the ambient light.")
	   self.ambient_light, self.ambient_light_direction = self.simulator.get_new_value(issimulation=True,
																			 simulationtype=self.SIMULATORTYPE,
																			 isdebug=self.ISDEBUG,
																			 actualvalue= self.ambient_light,
																			 newreading= None,
																			 minvalue= 0,
																			 maxvalue= 100,
																			 name= "color sensor ambient light",
																			 direction= self.ambient_light_direction,
																			 change= selfself.SIMULATORCHANGE,
																			 iswait= False,
																			 switch_min= self.SIMULATORSWITCHMIN,
																			 switch_max=self.SIMULATORSWITCHMAX,
																			 isextern= False,
																			 minreading=0,
																			 maxreading=100)
	   return self.ambient_light


		
	def get_blue(self):
		if(self.ISDEBUG):print("Color sensor get_blue() Retrieves the color intensity of blue.")
		self.blue, self.blue_direction = self.simulator.get_new_value( issimulation=True,
															 simulationtype=self.SIMULATORTYPE,
															 isdebug=self.ISDEBUG,
															 actualvalue= self.blue,
															 newreading= None,
															 minvalue= 0,
															 maxvalue= 1024,
															 name= "color sensor blue",
															 direction= self.blue_direction,
															 change= self.SIMULATORCHANGE,
															 iswait= False,
															 switch_min= self.SIMULATORSWITCHMIN,
															 switch_max=self.SIMULATORSWITCHMAX,
															 isextern= False,
															 minreading=0,
															 maxreading=50)
		return self.blue
	
	def get_green(self):
		if(self.ISDEBUG):print("Color sensor get_green() Retrieves the color intensity of green.")
		self.green, self.green_direction = self.simulator.get_new_value(   issimulation=True,
																 simulationtype=self.SIMULATORTYPE,
																 isdebug=self.ISDEBUG,
																 actualvalue= self.green,
																 newreading= None,
																 minvalue= 0,
																 maxvalue= 1024,
																 name= "color sensor green",
																 direction= self.green_direction,
																 change= self.SIMULATORCHANGE,
																 iswait= False,
																 switch_min= self.SIMULATORSWITCHMIN,
																 switch_max=self.SIMULATORSWITCHMAX,
																 isextern= False,
																 minreading=0,
																 maxreading=50)
		return self.green
	
	def get_red(self):
		if(self.ISDEBUG):print("Color sensor get_red() Retrieves the color intensity of red.")
		self.red, self.red_direction = self.simulator.get_new_value(   issimulation=True,
															 simulationtype=self.SIMULATORTYPE,
															 isdebug=self.ISDEBUG,
															 actualvalue= self.red,
															 newreading= None,
															 minvalue= 0,
															 maxvalue= 1024,
															 name= "color sensor red",
															 direction= self.red_direction,
															 change= self.SIMULATORCHANGE,
															 iswait= False,
															 switch_min= self.SIMULATORSWITCHMIN,
															 switch_max=self.SIMULATORSWITCHMAX,
															 isextern= False,
															 minreading=0,
															 maxreading=50)
		return self.red
	
	def get_color(self):
		if(self.ISDEBUG):print("Color sensor get_color() Retrieves the detected color of a surface.")
		self.color_index, self.color_index_direction = self.simulator.get_new_value(   issimulation=True,
																			 simulationtype=self.SIMULATORTYPE,
																			 isdebug=self.ISDEBUG,
																			 actualvalue= self.color_index,
																			 newreading= None,
																			 minvalue= 0,
																			 maxvalue= 8,
																			 name= "color",
																			 direction= self.color_index_direction,
																			 change= 1,
																			 iswait= False,
																			 switch_min= self.SIMULATORSWITCHMIN,
																			 switch_max=self.SIMULATORSWITCHMAX,
																			 isextern= False,
																			 minreading=0,
																			 maxreading=8)
		return self.colors_array[self.color_index]
		
	def get_reflected_light(self):
		if(self.ISDEBUG):print("Color sensor get_reflected_light() Retrieves the intensity of the reflected light.")
		#self.reflected_light = 0 #0..100
		self.reflected_light, self.reflected_light_direction = self.simulator.get_new_value(   issimulation=True,
																					 simulationtype=self.SIMULATORTYPE,
																					 isdebug=self.ISDEBUG,
																					 actualvalue= self.reflected_light,
																					 newreading= None,
																					 minvalue= 0,
																					 maxvalue= 100,
																					 name= "color sensor reflected_light",
																					 direction= self.reflected_light_direction,
																					 change= self.SIMULATORCHANGE,
																					 iswait= False,
																					 switch_min= self.SIMULATORSWITCHMIN,
																					 switch_max=self.SIMULATORSWITCHMAX,
																					 isextern= False)
		return self.reflected_light
	
	def get_rgb_intensity(self):
		#self.rgb_intensity = 0 #0..1024
		if(self.ISDEBUG):print("Color sensor get_rgb_intensity() Retrieves the overall color intensity, and intensity of rgb_intensity, green, and blue.")
		self.rgb_intensity, self.rgb_intensity_direction = self.simulator.get_new_value(   issimulation=True,
																				 simulationtype=self.SIMULATORTYPE,
																				 isdebug=self.ISDEBUG,
																				 actualvalue= self.rgb_intensity,
																				 newreading= None,
																				 minvalue= 0,
																				 maxvalue= 1024,
																				 name= "color sensor rgb_intensity",
																				 direction= self.rgb_intensity_direction,
																				 change= self.SIMULATORCHANGE,
																				 iswait= False,
																				 switch_min= self.SIMULATORSWITCHMIN,
																				 switch_max=self.SIMULATORSWITCHMAX,
																				 isextern= False)
		return self.rgb_intensity
	
	def light_up(self,light_1, light_2, light_3):
		if(self.ISDEBUG):print("Color sensor light_up() Sets the brightness of the individual lights on the Color Sensor. light_1:",str(light_1),", light_2:",str(light_2),", light_3:",str(light_3))
		print("Simulated color sensor light up by: light_1:",light_1," light_2:",light_2," light_3:",light_3)
				
	def light_up_all(self,brightness=100):
		if(self.ISDEBUG):print("Color sensor light_up_all() Lights up all of the lights on the Color Sensor at the specified brightness. brightness:",str(brightness))
		print("Simulated color sensor light up all by: brightness:",brightness)
		
			
	def wait_for_new_color(self):
		if(self.ISDEBUG):print("Color sensor wait_for_new_color() Waits until the Color Sensor detects a new color. Color at start:",self.colors_array[self.color_index])
		runwhile = True
		while runwhile:
			old_color_index = self.color_index
			self.color_index, self.color_index_direction = self.simulator.get_new_value(   issimulation=True,
																			 simulationtype=self.SIMULATORTYPE,
																			 isdebug=self.ISDEBUG,
																			 actualvalue= old_color_index,
																			 newreading= None,
																			 minvalue= 0,
																			 maxvalue= 8,
																			 name= "color",
																			 direction= self.color_index_direction,
																			 change= self.SIMULATORCHANGE,
																			 iswait= True,
																			 switch_min= self.color_index,
																			 switch_max=self.color_index,
																			 isextern= True,
																			 time_period= self.SIMULATORTIME,
																			 minreading=0,
																			 maxreading=8)
			if(self.ISDEBUG):print("Do changes at color sensor new reading:", str(self.color_index), " to exit it should be lower then:", self.color_index , " or it should be higher then:", self.color_index )
			if self.color_index > old_color_index or self.color_index < old_color_index:
				runwhile = False
			else:
				time.sleep(1)
			old_color_index = self.color_index
		return self.colors_array[self.color_index]
	
	def wait_until_color(self,color):
		if color == 'black':
			old_color_index = 0
		if color=='violet':
			old_color_index = 1
		if color == 'blue':
			old_color_index = 2
		if color=='violet':
			old_color_index = 3
		if color == 'cyan':
			old_color_index = 4
		if color=='green':
			old_color_index = 5
		if color == 'yellow':
			old_color_index = 6
		if color=='red':
			old_color_index = 7
		if color=='white':
			old_color_index = 8	
		if(self.ISDEBUG):print("Color sensor wait_until_color() Waits until the Color Sensor detects the specified color.")
		runwhile = True
		while runwhile:
			self.color_index, self.color_index_direction = self.simulator.get_new_value(   issimulation=True,
																			 simulationtype=self.SIMULATORTYPE,
																			 isdebug=self.ISDEBUG,
																			 actualvalue= old_color_index,
																			 newreading= None,
																			 minvalue= 0,
																			 maxvalue= 8,
																			 name= "color",
																			 direction= self.color_index_direction,
																			 change= self.SIMULATORCHANGE,
																			 iswait= True,
																			 switch_min= self.color_index,
																			 switch_max=self.color_index,
																			 isextern= True,
																			 time_period= self.SIMULATORTIME,
																			 minreading=0,
																			 maxreading=8)
			if(self.ISDEBUG):print("Do changes at color sensor new reading:", str(self.color_index), " to exit it should be higher or equal then:", old_color_index , " or it should be lower or equal then:", old_color_index )
			if self.color_index == old_color_index: 
				runwhile = False
			else:
				time.sleep(1)
		return 
		
