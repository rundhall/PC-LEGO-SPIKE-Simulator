from spike import ForceSensor, Motor
# Initialize the Force Sensor, a motor, and a variable
force_sensor = ForceSensor('B')
motor = Motor('C')
count = 0
# You can press the Force Sensor 5 times 
motor.set_default_speed(25)
while count < 5:
	force_sensor.wait_until_pressed()
	motor.start()
	force_sensor.wait_until_released()
	motor.stop()
	count = count + 1


# This condition will always be true, so it will loop forever
while True:
	# Measure the force in newtons or as a percentage
	percentage = force_sensor.get_force_percentage()
	# Use the measured force to start the motor
	motor.start(percentage)
