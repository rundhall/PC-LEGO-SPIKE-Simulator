'''start_at_power(power, steering=0)
Starts moving the Driving Base without speed control.
The motors can also be driven without speed control. This is useful when using your own control algorithm (e.g., a proportional line-follower).
If the steering is outside of the allowed range, the value will be set to "-100" or "100" depending on whether the value is positive or negative.
If the power is outside of the allowed range, the value will be set to "-100" or "100" depending on whether the value is positive or negative.
If the power is negative, the Driving Base will move backward instead of forward.
The program flow is not interrupted. This can most likely be interrupted by sensor input and a condition.
Parameters
power
The amount of power to send to the motors.
Type:integer (a positive or negative whole number, including 0)
Values:-100 to 100%
Default:100
steering
The steering direction (-100 to 100). "0" makes the Driving Base move straight. Negative numbers make the Driving Base turn left. Positive numbers make the Driving Base turn right.
Type:Integer
Values:-100 to 100
Default:0
Errors
TypeError 
steering or power is not an integer.
RuntimeError
One or both of the Ports do not have a motor connected or the motors could not be paired.
Example
'''
from spike import MotorPair, ColorSensor

motor_pair = MotorPair('B', 'A')

while True:
    motor_pair.start_at_power(50, 0)