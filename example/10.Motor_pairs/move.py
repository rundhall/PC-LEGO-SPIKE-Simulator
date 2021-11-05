'''move(amount, unit='cm', steering=0, speed=None)
Start both motors simultaneously to move a Driving Base.
Steering = "0" makes the Driving Base go straight. Negative numbers make the Driving Base turn left. Positive numbers make the Driving Base turn right.
The program will not continue until the specified value is reached.
If the value of steering is equal to "-100" or "100," the Driving Base will perform a rotation on itself (i.e., "tank move") at the default speed of each motor.
If the value of steering is outside of the allowed range, the value will be set to "-100" or "100," depending on whether the value is positive or negative.
If speed is outside of the allowed range, the value will be set to "-100" or "100," depending on whether the value is positive or negative.
If the speed is negative, the Driving Base will move backward instead of forward. Likewise, if the "amount" is negative, the Driving Base will move backward instead of forward. If both the speed and the "amount" are negative, the Driving Base will move forward.
When the specified unit is "cm" or "in," the "amount" of the unit parameter is equal to the horizontal distance that the Driving Base will travel before stopping. The relationship between the motor rotations and distance traveled can be adjusted by calling set_motor_rotation().
When the "unit" is "rotations" or "degrees," the "amount" parameter value specifies how much the motor axle will turn before stopping.
When the "unit" is "seconds," the "amount" parameter value specifies the duration that the motors will run before stopping.
Parameters
amount
The quantity to move in relation to the specified unit of measurement.
Type:float (decimal numbers)
Values:any value
Default:no default value
unit
The unit of measurement specified for the "amount" parameter.
Type:String (text)
Values:"cm","in","rotations","degrees","seconds"
Default:cm
steering
The direction and quantity to steer the Driving Base.
Type:integer (a positive or negative whole number, including 0)
Values:-100 to 100
Default:0
speed
The motor speed.
Type:integer (a positive or negative whole number, including 0)
Values:-100 to 100
Default:the speed set by set_default_speed()
Errors
TypeError
amount is not a number, or steering or speed is not an integer, or unit is not a string.
ValueError
unit is not one of the allowed values.
RuntimeError
One or both of the motors has been disconnected or the motors could not be paired.
Example
'''
import math
from spike import MotorPair

motor_pair = MotorPair('B', 'A')


# turn a Driving Base 180 degrees in place (if wheels are 8.1 cm apart)

motor_pair.move(8.1 * math.pi / 2, 'cm', steering=100)
