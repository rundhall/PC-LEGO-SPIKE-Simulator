import random,time

class Motor:
	#If ISDEBUG is true. then all modules send debug information through console
	ISDEBUG = True
	
	def __init__(self,port):
		self.port = port
		self.degrees_counted = 0
		self.default_speed = 100
		self.position = 0
		self.action="coast"
		self.stop_when_stallesyd=True
		self.degrees = 0
		self.direction = 'clockwise'
		self.speed = None
		self.servo = None

	def set_degrees_counted(self,degrees_counted):
		if(self.ISDEBUG):print("motor set_degrees_counted(). Sets the number of degrees counted to the desired value. New value degrees_counted:",str(degrees_counted))
		self.degrees_counted = degrees_counted
		
	def set_default_speed(self,default_speed):
		if(self.ISDEBUG):print("motor set_default_speed(). Sets the default motor speed. New value default_speed:",str(default_speed))
		self.default_speed = default_speed
		
	def set_stop_action(self,action):
		if(self.ISDEBUG):print("motor set_stop_action(). Sets the default behavior when a motor stops. New value action:",str(action))
		self.action = action
		
	def set_stall_detection(self,stop_when_stalled):
		if(self.ISDEBUG):print("motor set_stall_detection(). Turns stall detection on or off. New value stop_when_stalled:",str(stop_when_stalled))
		self.stop_when_stalled = stop_when_stalled
		
		#input the relatave turn the old absolute position and a speed
	def handel_servo(self,
					 issimulation=True,
					 isdebug=True,
					 relative_turn=0,
					 old_absolute_position=0,
					 run_time_period = 0,
					 speed=None,
					 default_speed=100,
					 servo=None):
		#servo clockwise speed min. 85  max 5 counterclockwise speed min. 95 max 180
		#calculation for clockwise timer=degree*(0.9*speed**2-170*speed+8600)/360 
		#Values:"shortest path" could run in either direction, depending on the shortest distance to the target.
		#"clockwise" will make the motor run clockwise until it reaches the target position.
		#"counterclockwise" will make the motor run counterclockwise until it reaches the target position.
		duty = 0
		if speed == None:
			speed = default_speed
		else:
			speed = speed
		if speed == 0:
			duty = 0
			
		if not run_time_period == 0:
			relative_turn = run_time_period*1000 / ((0.9*speed**2-170*speed+8600)/360) 
			if speed < 0:
				relative_turn = relative_turn * -1
		
		new_absolute_position = old_absolute_position + relative_turn % 360
		
		if relative_turn > 0:
			duty = 100 - int(speed)
			if duty < 2:
				duty = 2
			#different calculation for different direction
			timer=abs(relative_turn*(0.9*speed**2-170*speed+8600)/360)/1000 
		else:
			duty = 80 + speed
			timer=abs(relative_turn*(0.9*speed**2-170*speed+8600)/360)/1000 
			
		if new_absolute_position < 0:
			new_absolute_position = new_absolute_position + 360
		if(isdebug):print("relative turn:",str(relative_turn),
						  " old absolute position:",str(old_absolute_position),
						  " new absolute position:",str(new_absolute_position),
						  " speed:",str(speed),
						  " duty:",str(duty),
						  " timer:",str(timer))
		if run_time_period == 0:
			time.sleep(int(timer))
		else:
			time.sleep(int(run_time_period))
		return new_absolute_position
		
					 

	def run_to_position(self,degrees, direction='Shortest path', speed=None):
		if(self.ISDEBUG):print("motor run_to_position(). Runs the motor to an absolute position. New values degrees:",str(degrees)," direction:",str(direction)," speed:",str(speed))
		self.degrees = degrees
		self.direction = direction
		self.speed = speed
		if degrees > 359:
				degrees = 359
		if degrees < 0:
				degrees = 0
		relative_turn = 0
		direction = direction[:1].lower() + direction[1:]
		if direction=='shortest path':
			if degrees > self.position:
				if degrees - self.position > 180:
					relative_turn = -1*(360 - (degrees-self.position))
				else:
					relative_turn = degrees-self.position
			else:
				if degrees - self.position < -180:
					relative_turn = degrees-self.position
				else:
					relative_turn = -1*(360 - (degrees-self.position))
				   
		if degrees > self.position:
			if direction=='clockwise':
				relative_turn = degrees-self.position
			if direction=='counterclockwise':
				relative_turn = -1*(360 - (degrees-self.position))
		else:
			if direction=='clockwise':
				relative_turn = -1*(360 - (degrees-self.position)) 
			if direction=='counterclockwise':
				relative_turn = degrees-self.position
		if degrees == self.position:
			relative_turn = 0
		self.position = self.handel_servo(issimulation=True,
					 isdebug=self.ISDEBUG,
					 relative_turn = relative_turn,
					 old_absolute_position =self.position,
					 run_time_period = 0,
					 speed=self.speed,
					 default_speed=self.default_speed,
					 servo=self.servo)
		
	def run_to_degrees_counted(self,degrees, speed=None):
		if(self.ISDEBUG):print("motor run_to_degrees_counted(). Runs the motor until the number of degrees counted is equal to the value. New values degrees:",str(degrees)," speed:",str(speed))
		self.degrees = degrees
		self.speed = speed
		self.position = self.handel_servo(issimulation=True,
					 isdebug=self.ISDEBUG,
					 relative_turn = degrees,
					 old_absolute_position =self.position,
					 run_time_period = 0,
					 speed=self.speed,
					 default_speed=self.default_speed,
					 servo=self.servo)
	
	def run_for_degrees(self,degrees, speed=None):
		if(self.ISDEBUG):print("motor run_for_degrees(). Runs the motor for a specified number of degrees. New values degrees:",str(degrees)," speed:",str(speed))
		self.degrees = degrees
		self.speed = speed
		self.position = self.handel_servo(issimulation=True,
					 isdebug=self.ISDEBUG,
					 relative_turn = degrees,
					 old_absolute_position =self.position,
					 run_time_period = 0,
					 speed=self.speed,
					 default_speed=self.default_speed,
					 servo=self.servo)

	def run_for_rotations(self,rotations, speed=None):
		if(self.ISDEBUG):print("motor run_for_rotations(). Runs the motor for a specified number of rotations. New values rotations:",str(rotations)," speed:",str(speed))
		self.rotations = rotations
		self.speed = speed
		self.degrees = rotations*360
		self.position = self.handel_servo(issimulation=True,
					 isdebug=self.ISDEBUG,
					 relative_turn = self.degrees,
					 old_absolute_position =self.position,
					 run_time_period = 0,
					 speed=self.speed,
					 default_speed=self.default_speed,
					 servo=self.servo)
			   
	def run_for_seconds(self,seconds, speed=None):
		if(self.ISDEBUG):print("motor run_for_seconds(). Runs the motor for a specified number of seconds. New values seconds:",str(seconds)," speed:",str(speed))
		self.seconds = seconds
		self.speed = speed
		self.position = self.handel_servo(issimulation=True,
			 isdebug=self.ISDEBUG,
			 relative_turn = self.position,
			 old_absolute_position = self.position,
			 run_time_period = seconds,
			 speed=self.speed,
			 default_speed=self.default_speed,
			 servo=self.servo)
		
		
		
	def get_speed(self):
		if(self.ISDEBUG):print("motor get_speed(). Retrieves the motor speed. Stored value:",str(self.speed))
		return self.speed
	
	def get_position(self):
		if(self.ISDEBUG):print("motor get_position(). Retrieves the motor position. Stored value:",str(self.position))
		return self.position
	
	def get_degrees_counted(self):
		if(self.ISDEBUG):print("motor get_degrees_counted(). Retrieves the motor degrees_counted. Stored value:",str(self.degrees_counted))
		return self.degrees_counted	

	def get_default_speed (self):
		if(self.ISDEBUG):print("motor get_default_speed(). Retrieves the motor default_speed. Stored value:",str(self.default_speed))
		return self.default_speed
	
	def start(self,speed=None):
		if(self.ISDEBUG):print("motor start(). Starts running the motor at a specified speed. New values speed:",str(speed))
		
		if self.direction=='clockwise':
			isclockwise = True
		else:
			isclockwise = False
		duty = 0
		if speed == None:
			self.speed = self.default_speed
		else:
			self.speed = speed
		if isclockwise:
			duty = 100 - int(self.speed)
			if duty < 2:
				duty = 2
		else:
			duty = 80 + self.speed
		if self.speed == 0:
			duty = 0
		if(self.ISDEBUG):print("duty:",str(duty)," speed:",str(self.speed)," self.direction:",str(self.direction))
		

	def stop(self):
		if(self.ISDEBUG):print("motor stop(). Stops the motor.")
		
	def was_interrupted(self):
		if(self.ISDEBUG):print("motor was_interrupted(). Tests whether the motor was interrupted.")
		return False
	
	def was_stalled(self):
		if(self.ISDEBUG):print("motor was_stalled(). Tests whether the motor was stalled.")
		return False
