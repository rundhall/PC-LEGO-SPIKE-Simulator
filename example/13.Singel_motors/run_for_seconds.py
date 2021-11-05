'''run_for_seconds(seconds, speed=None)
Runs the motor for a specified number of seconds.
Parameters
seconds
The number of seconds for which the motor should run.
Type:float (decimal number)
Values:any number
Default:no default value
speed
The motor’s speed.
Type:integer (a positive or negative whole number, including 0)
Values:-100% to 100%
Default:If no value is specified, it will use the default speed that’s been set by set_default_speed().
Errors
TypeError
seconds is not a number or speed is not an integer.
RuntimeError
The motor has been disconnected from the Port.
Example
'''
from spike import Motor
import time

motor = Motor('A')


# Run clockwise for half a second at 75% speed

motor.run_for_seconds(0.5, 100)
time.sleep_ms(3000)

# Run counterclockwise for 6 seconds at 30% speed

motor.run_for_seconds(3, 100)