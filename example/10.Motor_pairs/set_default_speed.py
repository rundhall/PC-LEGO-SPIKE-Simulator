'''set_default_speed(speed)
Sets the default motor speed.
If speed is outside of the allowed range, the value will be set to "-100" or "100" depending on whether the value is positive or negative.
Setting the speed will not have any effect until one of the move or start methods is called, even if the Driving Base is already moving.
Parameters
speed
The default motor speed.
Type:integer (a positive or negative whole number, including 0)
Values:-100 to 100
Default:100
Errors
TypeError
speed is not a number.
'''
from spike import MotorPair

motor_pair = MotorPair('B', 'A')

motor_pair.set_default_speed(11)