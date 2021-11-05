'''run_for_rotations(rotations, speed=None)
Runs the motor for a specified number of rotations.
Parameters
rotations
The number of rotations that the motor should run.
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
rotations is not a number or speed is not an integer.
RuntimeError
The motor has been disconnected from the Port.
Example
'''
from spike import Motor

motor = Motor('A')


# Run the motor 90 degrees clockwise:

motor.run_for_rotations(0.25)


# Run the motor 90 degrees counterclockwise:

motor.run_for_rotations(-0.25)
