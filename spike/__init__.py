import time,spike.light_matrix,random,spike.status_light,spike.left_button,spike.right_button,spike.force_sensor,spike.distance_sensor,spike.app,spike.speaker,spike.color_sensor,spike.motion_sensor,spike.motor,spike.motor_pair

class PrimeHub:
	PORT_A = "A"
	PORT_B = "B"
	PORT_C = "C"
	PORT_D = "D"
	PORT_E = "E"
	PORT_F = "F"

	
	def __init__(self):
		self.left_button = left_button.Left_button()
		self.right_button = right_button.Right_button()
		self.speaker = speaker.Speaker()
		self.light_matrix = light_matrix.Light_matrix()
		self.motion_sensor = motion_sensor.Motion_sensor() 
		self.status_light = status_light.Status_light() 
	
class ForceSensor:
	def __init__(self,port):
		self.force_sensor = force_sensor.ForceSensor(port)
		
	def get_force_newton(self):
		return self.force_sensor.get_force_newton()
	
	def get_force_percentage(self):
		return self.force_sensor.get_force_percentage()
	
	def is_pressed(self):
		return self.force_sensor.is_pressed()
	
	def wait_until_pressed(self):
		return self.force_sensor.wait_until_pressed()
	
	def wait_until_released(self):
		return self.force_sensor.wait_until_released()
   
#MotorPair was removed because of a memory issue. ESP 32 WROOM not enough memory use WROVER with PSRAM	 
class MotorPair:
	def __init__(self,port1,port2):
		self.motor_pair = motor_pair.MotorPair(port1,port2)
	
	def set_default_speed(self,default_speed):
		return self.motor_pair.set_default_speed(default_speed)
		
	def set_stop_action(self,action):
		return self.motor_pair.set_stop_action(action)
	
	def set_motor_rotation(self,amount, unit='cm'):
		return self.motor_pair.set_motor_rotation(amount, unit)

	def get_default_speed(self):
		return self.motor_pair.get_default_speed()
	
	def start(self,speed=None):
		return self.motor_pair.start(speed)
	
	def start_tank_at_power(self,left_power, right_power):
		return self.motor_pair.start_tank_at_power(left_power, right_power)
	
	def start_tank(self,left_speed, right_speed):
		return self.motor_pair.start_tank(left_speed, right_speed)

	def stop(self):
		return self.motor_pair.stop()

	def move(self, amount, unit='cm', steering=0, speed=None):
		return self.motor_pair.move(amount, unit, steering, speed)
	
	def move_tank(self,amount, unit='cm', left_speed=None, right_speed=None):
		return self.motor_pair.move_tank(amount, unit, left_speed, right_speed)


class Motor:
	def __init__(self,port):
		self.motor = motor.Motor(port)
	
	def set_degrees_counted(self,degrees_counted):
		return self.motor.set_degrees_counted(degrees_counted)
		
	def set_default_speed(self,default_speed):
		return self.motor.set_default_speed(default_speed)
		
	def set_stop_action(self,action):
		return self.motor.set_stop_action(action)
		
	def set_stall_detection(self,stop_when_stalled):
		return self.motor.set_stall_detection(stop_when_stalled)
	
	def run_to_position(self,degrees, direction='shortest path', speed=None):
		return self.motor.run_to_position(degrees, direction, speed)
	
	def run_to_degrees_counted(self,degrees, speed=None):
		return self.motor.run_to_degrees_counted(degrees, speed)
	
	def run_for_degrees(self,degrees, speed=None):
		return self.motor.run_for_degrees(degrees, speed) 
	
	def run_for_rotations(self,rotations, speed=None):
		return self.motor.run_for_rotations(rotations, speed)
	
	def run_for_seconds(self,seconds, speed=None):
		return self.motor.run_for_seconds(seconds, speed)
	
	def get_speed(self):
		return self.motor.get_speed()
	
	def get_position(self):
		return self.motor.get_position()
	
	def get_degrees_counted(self):
		return self.motor.get_degrees_counted()
	
	def get_default_speed(self):
		return self.motor.get_default_speed()
	
	def start(self,speed=None):
		return self.motor.start(speed)

	def stop(self):
		return self.motor.stop()

	def was_interrupted(self):
		return self.motor.was_interrupted()
	
	def was_stalled(self):
		return self.motor.was_stalled()
	

class DistanceSensor:
	def __init__(self,port):
		self.distance_sensor = distance_sensor.DistanceSensor(port)
	
	def get_distance_cm(self,short_range=False):
		return self.distance_sensor.get_distance_cm(short_range)
	
	def get_distance_inches(self,short_range=False):
		return self.distance_sensor.get_distance_inches(short_range)
	
	def get_distance_percentage(self,short_range=False):
		return self.distance_sensor.get_distance_percentage(short_range)

	
	def light_up(self,right_top, left_top, right_bottom, left_bottom):
		return self.distance_sensor.light_up(right_top, left_top, right_bottom, left_bottom)
	
	def light_up_all(self,brightness=100):
		return self.distance_sensor.light_up_all(brightness)
	
	def wait_for_distance_farther_than(self,distance=100, unit='cm', short_range=False):
		return self.distance_sensor.wait_for_distance_farther_than(distance, unit, short_range)
	
	def wait_for_distance_closer_than(self,distance=100, unit='cm', short_range=False):
		return self.distance_sensor.wait_for_distance_closer_than(distance, unit, short_range)
	
class App:
	def __init__(self):
		self.app = app.App()
	
	def play_sound(self,musicname):
		return self.app.play_sound(musicname)
		
	def start_sound(self,musicname):
		return self.app.start_sound(musicname)

class ColorSensor:
	def __init__(self,port):
		self.color_sensor = color_sensor.ColorSensor(port)
	
	def get_ambient_light(self):
		return self.color_sensor.get_ambient_light()
	
	def get_blue(self):
		return self.color_sensor.get_blue()
	
	def get_color(self):
		return self.color_sensor.get_color()
	
	def get_green(self):
		return self.color_sensor.get_green()
	
	def get_red(self):
		return self.color_sensor.get_red()
	
	def get_reflected_light(self):
		return self.color_sensor.get_reflected_light()
	
	def get_rgb_intensity(self):
		return self.color_sensor.get_rgb_intensity()
	
	def light_up(self,light_1, light_2, light_3):
		return self.color_sensor.light_up(light_1, light_2, light_3)
	
	def light_up_all(self,brightness=100):
		return self.color_sensor.light_up_all(brightness)
	
	def wait_for_new_color(self):
		return self.color_sensor.wait_for_new_color()
	
	def wait_until_color(self,color):
		return self.color_sensor.wait_until_color(color)
