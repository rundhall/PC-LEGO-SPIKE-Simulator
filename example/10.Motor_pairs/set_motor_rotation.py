'''set_motor_rotation(amount, unit='cm')
Sets the ratio of one motor rotation to the distance traveled.
If there are no gears used between the motors and the wheels of the Driving Base, the "amount" is the circumference of one wheel.
Calling this method does not affect the Driving Base if it’s already running. It will only have an effect the next time one of the move or start methods is used.
Parameters
amount
The distance that the Driving Base moves when both motors move one rotation each.
Type:float (decimal number)
Values:any value
Default:17.6
unit
The unit of measurement specified for the "amount" parameter.
Type:String (text)
Values:"cm","in"
Default:cm
Errors
TypeError
amount is not a number or unit is not a string.
ValueError
unit is not one of the allowed values.
Example
'''
import math
from spike import MotorPair

motor_pair = MotorPair('B', 'A')

motor_pair.set_motor_rotation(17.6 * math.pi, 'cm')
