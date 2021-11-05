from spike import ColorSensor, Motor
from spike.control import Timer
# Initialize the Colour Sensor, 2 motors, and a Timer
color_sensor = ColorSensor('F')
motor_a = Motor('A')
motor_e = Motor('E')
timer = Timer()
# Present each colored brick to the Color Sensor and observe what happens; it will detect each color for 30 seconds
while timer.now() < 5:
	color = color_sensor.wait_for_new_color()
	if color == 'violet':
		motor_a.run_for_rotations(1)
	elif color == 'yellow':
		motor_e.run_for_rotations(1)

print("wait_for_new_color is over") 

timer = Timer()
# This will use the reflected value of the colors to set the motor speed (yellow is approximately 80% and violet 60%)
while timer.now() < 5:
	color = color_sensor.wait_for_new_color()
	percentage = color_sensor.get_reflected_light()
	if color == 'magenta':
		motor_a.run_for_rotations(1, percentage)
	elif color == 'yellow':
		motor_e.run_for_rotations(1, percentage)
print("get_reflected_light is over") 