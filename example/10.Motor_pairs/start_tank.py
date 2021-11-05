'''start_tank(left_speed, right_speed)
Starts moving the Driving Base using differential (tank) steering.
The speed of each motor can be controlled independently for differential (tank) drive Driving Bases.
If left_speed or right_speed is outside of the allowed range, the value will be set to "-100" or "100" depending on whether the value is positive or negative.
If the speed is negative, the motors will move backward instead of forward.
The program flow is not interrupted. This is most likely interrupted by sensor input and a condition.
Parameters
left_speed
The speed of the left motor.
Type:integer (a positive or negative whole number, including 0)
Values:-100 to 100
Default:no default value
right_speed
The speed of the right motor.
Type:integer (a positive or negative whole number, including 0)
Values:-100 to 100
Default:no default value
Errors
TypeError
left_speed or right_speed is not an integer.
RuntimeError
One or both of the Ports do not have a motor connected or the motors could not be paired.
Example
'''
from spike import MotorPair
import time

motor_pair = MotorPair('B', 'A')

# Rotate the Driving Base in place to the right
motor_pair.start_tank(100, 100)

time.sleep_ms(2000) 
# wait for something

motor_pair.stop()