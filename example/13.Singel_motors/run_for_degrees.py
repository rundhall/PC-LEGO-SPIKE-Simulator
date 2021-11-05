'''
run_for_degrees(degrees, speed=None)
Runs the motor for a specified number of degrees.
Parameters
degrees
The number of degrees that the motor should run.
Type:integer (a positive or negative whole number, including 0)
Values:any number
Default:no default value
speed
The motor’s speed.
Type:integer (a positive or negative whole number, including 0)
Values:-100 to 100%
Default:If no value is specified, it will use the default speed that’s been set by set_default_speed().
Errors
TypeError
degrees or speed is not an integer.
RuntimeError
The motor has been disconnected from the Port.
Example
'''
from spike import Motor
import time

motor = Motor('A')


# Run the motor 90 degrees clockwise

motor.run_for_degrees(90)
time.sleep_ms(3000)
print('90 run_for_degrees done')

# Run the motor 90 degrees counterclockwise

motor.run_for_degrees(-90)
time.sleep_ms(3000)
print('-90 run_for_degrees done')

# Run the motor 360 degrees clockwise at maximum (100%) speed

motor.run_for_degrees(360, 100)
time.sleep_ms(3000)
print('360 run_for_degrees done')
