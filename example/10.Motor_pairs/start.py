'''start(steering=0, speed=None)
Start both motors simultaneously to move a Driving Base.
Steering = "0" makes the Driving Base go straight. Negative numbers make the Driving Base turn left. Positive numbers make the Driving Base turn right.
The program flow is not interrupted. This is most likely interrupted by sensor input and a condition.
If the value of steering is equal to "-100" or "100," the Driving Base will perform a rotation on itself (i.e., "tank move") at the default speed of each motor.
If the value of "steering" is outside of the allowed range, the value will be set to "-100" or "100," depending on whether the value is positive or negative.
If speed is outside of the allowed range, the value will be set to "-100" or "100," depending on whether the value is positive or negative.
If the speed is negative, the Driving Base will move backward instead of forward. Likewise, if the "amount" is negative, the Driving Base will move backward instead of forward. If both the speed and the "amount" are negative, the Driving Base will move forward.
Parameters
steering
The direction and quantity to steer the Driving Base.
Type:integer (a positive or negative whole number, including 0)
Values:-100 to 100
Default:0
speed
The speed at which the Driving Base will move while performing a curve.
Type:integer (a positive or negative whole number, including 0)
Values:-100 to 100%
Default:If no value is specified, it will use the default speed that’s been set by set_default_speed().
Errors
TypeError
steering or speed is not an integer.
RuntimeError
One or both of the motors has been disconnected or the motors could not be paired.
Example
''' 
from spike import MotorPair
import time
motor_pair = MotorPair('B', 'A')

motor_pair.start()

time.sleep_ms(2000) 
# wait for something

motor_pair.stop()
