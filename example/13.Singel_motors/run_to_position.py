'''run_to_position(degrees, direction='shortest path', speed=None)
Runs the motor to an absolute position.
The sign of the speed will be ignored (i.e., absolute value), and the motor will always travel in the direction that’s been specified by the "direction" parameter. If the speed is greater than "100," it will be limited to "100."
Parameters
degrees
The target position.
Type:integer (positive or negative whole number, including 0)
Values:0 to 359
Default:no default value
direction
The direction to use to reach the target position.
Type:String (text)
Values:"Shortest path" could run in either direction, depending on the shortest distance to the target.
"Clockwise" will make the motor run clockwise until it reaches the target position.
"Counterclockwise" will make the motor run counterclockwise until it reaches the target position.
Default:no default value
speed
The motor’s speed.
Type:integer (a positive or negative whole number, including 0)
Values:0 to 100%
Default:If no value is specified, it will use the default speed that’s been set by set_default_speed().
Errors
TypeError
degrees or speed is not an integer or direction is not a string.
ValueError
direction is not one of the allowed values or degrees is not within the range of 0-359 (both inclusive).
RuntimeError
The motor has been disconnected from the Port.
Example
'''
from spike import Motor
import time

motor = Motor('A')


# Set the motor to position "0," aligning the markers

motor.run_to_position(0)
time.sleep_ms(3000)
motor.run_to_position(150,'clockwise')
time.sleep_ms(3000)
motor.run_to_position(250,'clockwise')
time.sleep_ms(3000)
motor.run_to_position(350,'clockwise')
time.sleep_ms(3000)