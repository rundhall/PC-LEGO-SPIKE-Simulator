'''start_tank_at_power(left_power, right_power)
Starts moving the Driving Base using differential (tank) steering without speed control.
The motors can also be driven without speed control. This is useful when using your own control algorithm (e.g., a proportional line-follower).
If the left_power or right_power is outside of the allowed range, the value will be rounded to "-100" or "100" depending on whether the value is positive or negative.
If the power is a negative value, the corresponding motor will move backward instead of forward.
The program flow is not interrupted. This can most likely be interrupted by sensor input and a condition.
Parameters
left_power
The power of the left motor.
Type:Integer
Values:-100 to 100
Default:no default value
right_power
The power of the right motor.
Type:Integer
Values:-100 to 100
Default:no default value
Errors
TypeError
left_power or right_power is not an integer.
RuntimeError
One or both of the Ports do not have a motor connected or the motors could not be paired.
Example
'''
from spike import MotorPair
import time
motor_pair = MotorPair('B', 'A')

# Rotate the Driving Base in place to the right
motor_pair.start_tank_at_power(100, 100)

# wait for something
time.sleep_ms(1000)
motor_pair.stop()