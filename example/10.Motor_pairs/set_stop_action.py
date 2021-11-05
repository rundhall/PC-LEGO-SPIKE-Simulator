'''set_stop_action(action)
Sets the motor action that will be used when the Driving Base stops.
If the action is "brake," the motors will stop quickly and be allowed to turn freely.
If the action is "hold," the motors will actively hold their current position and cannot be turned manually.
If the action is set to "coast," the motors will stop slowly and can be turned freely.
Setting the "stop" action does not take immediate effect on the motors. The setting will be saved and used whenever stop() is called or when one of the move methods has completed without being interrupted.
Parameters
action
The desired action of the motors when the Driving Base stops.
Type:String (text)
Values:"brake","hold","coast"
Default:"coast"
Errors
TypeError
action is not a string.
ValueError
action is not one of the allowed values.
Example
'''
from spike import MotorPair

motor_pair = MotorPair('B', 'A')


# Allow the motors to turn freely after stopping
motor_pair.set_stop_action('coast')
