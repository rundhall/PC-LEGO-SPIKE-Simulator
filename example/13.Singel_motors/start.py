'''start(speed=None)
Starts running the motor at a specified speed.
The motor will keep moving at this speed until you give it another motor command or when your program ends.
Parameters
speed
The motor’s speed.
Type:integer (a positive or negative whole number, including 0)
Values:-100% to 100%
Default:If no value is specified, it will use the default speed that’s been set by set_default_speed().
Errors
TypeError
speed is not an integer.
RuntimeError
The motor has been disconnected from the Port.
Example
'''
from spike import Motor
from spike.control import wait_for_seconds

motor = Motor('A')

motor.start()

# wait until something
wait_for_seconds(1)
motor.stop()