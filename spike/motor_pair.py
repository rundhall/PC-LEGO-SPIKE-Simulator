import random,time

class MotorPair:
	#If ISDEBUG is true. then all modules send debug information through console
	ISDEBUG = True
	
	def __init__(self,port1,port2):
		self.port1 = port1
		self.port2 = port2
		self.degrees_counted = 0
		self.default_speed = 100
		self.position = 0
		self.action="coast"
		self.stop_when_stallesyd=True
		self.degrees = 0
		self.direction = 'clockwise'
		self.speed = None
		self.servo1 = None
		self.servo2 = None
			
	def set_default_speed(self,default_speed):
		if(self.ISDEBUG):print("motor_pair set_default_speed(). Sets the default motor speed. New value default_speed:",str(default_speed))
		self.default_speed = default_speed
		
	def set_stop_action(self,action):
		if(self.ISDEBUG):print("motor_pair set_stop_action(). Sets the default behavior when a motor stops. New value action:",str(action))
		self.action = action
		
	def set_motor_rotation(self,amount, unit='cm'):
		if(self.ISDEBUG):print("motor_pair set_motor_rotation(). Sets the ratio of one motor rotation to the distance traveled. New value amount:",str(amount)," unit:",str(unit))
		self.amount = amount
		self.unit = unit

	def start_tank(self,left_speed, right_speed):
		if(self.ISDEBUG):print("motor_pair start_tank(). Starts moving the Driving Base using differential (tank) steering. New values left_speed:",str(left_speed)," right_speed:",str(right_speed))
	
	def start_tank_at_power(self,left_power, right_power):
		if(self.ISDEBUG):print("motor_pair start_tank_at_power(). Starts moving the Driving Base using differential (tank) steering without speed control. New values left_power:",str(left_power)," right_power:",str(right_power))

	def get_default_speed (self):
		if(self.ISDEBUG):print("motor_pair get_default_speed(). Retrieves the motor default_speed. Stored value:",str(self.default_speed))
		return self.default_speed
	
	def start(self,speed=None):
		if(self.ISDEBUG):print("motor_pair start(). Starts running the motor at a specified speed. New values speed:",str(speed))

	def stop(self):
		if(self.ISDEBUG):print("motor_pair stop(). Stops the motor.")

	def move(self, amount, unit='cm', steering=0, speed=None):
		if(self.ISDEBUG):print("motor_pair move(). Start both motors simultaneously to move a Driving Base. New values amount:",str(amount)," unit:",str(unit)," steering:",str(steering)," speed:",str(speed))

	def move_tank(self,amount, unit='cm', left_speed=None, right_speed=None):
		if(self.ISDEBUG):print("motor_pair move_tank(). Moves the Driving Base using differential (tank) steering. New values amount:",str(amount)," unit:",str(unit)," left_speed:",str(left_speed)," right_speed:",str(right_speed))

