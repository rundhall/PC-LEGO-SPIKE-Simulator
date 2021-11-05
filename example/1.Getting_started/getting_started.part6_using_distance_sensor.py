from spike import DistanceSensor, Motor
# Initialize the Distance Sensor and motor
distance_sensor = DistanceSensor('D')
motor = Motor('C')
# Move your hand slowly toward and then away from the Distance Sensor
while True:
	distance_sensor.wait_for_distance_farther_than(20, 'cm')
	motor.start()
	distance_sensor.wait_for_distance_closer_than(20, 'cm')
	motor.stop()

# Move your hand slowly toward and then away from the Distance Sensor, the motor speed will change based on the detected distance 
while True:
	percentage = distance_sensor.get_distance_percentage()
	if percentage is not None:
		motor.start(100 - percentage)
