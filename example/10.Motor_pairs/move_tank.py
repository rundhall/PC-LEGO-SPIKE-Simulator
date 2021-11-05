'''move_tank(amount, unit='cm', left_speed=None, right_speed=None)
Moves the Driving Base using differential (tank) steering.
The speed of each motor can be controlled independently for differential (tank) drive Driving Bases.
When the specified unit is "cm" or "in," the "amount" of the unit parameter is equal to the horizontal distance that the Driving Base will travel before stopping. The relationship between the motor rotations and distance traveled can be adjusted by calling set_motor_rotation().
When the "unit" is "rotations" or "degrees," the "amount" parameter value specifies how much the motor axle will turn before stopping.
When the "unit" is "seconds," the "amount" parameter value specifies the duration that the motors will run before stopping.
If left_speed or right_speed is outside of the allowed range, the value will be set to "-100" or "100" depending on whether the value is positive or negative.
If one of the speeds (i.e., left_speed or right_speed) is negative, the negative-speed motor will run backward instead of forward. If the "amount" parameter value is negative, both motors will rotate backward instead of forward. If both of the speed values (i.e., left_speed and right_speed) are negative and the "amount" parameter value is negative, both motors will rotate forward.
The program will not continue until the specified value is reached.
Parameters
amount
The quantity to move in relation to the specified unit of measurement.
Type:float (decimal number)
Values:any value
Default:no default value
unit
The unit of measurement specified for the "amount" parameter.
Type:String (text)
Values:"cm","in","rotations","degrees","seconds"
Default:cm
left_speed
The speed of the left motor.
Type:integer (a positive or negative whole number, including 0)
Values:-100 to 100
Default:the speed set by set_default_speed()
right_speed
The speed of the right motor.
Type:integer (a positive or negative whole number, including 0)
Values:-100 to 100
Default:the speed set by set_default_speed()
Errors
TypeError
amount, left_speed or right_speed is not a number or unit is not a string.
ValueError
unit is not one of the allowed values.
RuntimeError
One or both of the Ports do not have a motor connected or the motors could not be paired.
Example
'''
from spike import MotorPair

motor_pair = MotorPair('B', 'A')
motor_pair.move_tank(10, 'cm', left_speed=25, right_speed=75)