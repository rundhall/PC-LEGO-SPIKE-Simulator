'''was_gesture(gesture)
Tests whether a gesture has occurred since the last time was_gesture() was used, or since the beginning of the program (for the first use).
Parameters
gesture
The name of the gesture.
Type:String (text)
Values:"shaken","tapped","double-tapped","falling","none"
Default:no default value
Errors
TypeError
gesture is not a string.
ValueError
gesture is not one of the allowed values.
Returns
True if the gesture has occurred since the last time was_gesture() was called, otherwise false.
Type:Boolean
Values:True or False
Example
'''
from spike import PrimeHub
from spike.control import wait_for_seconds

hub = PrimeHub()


while not hub.motion_sensor.was_gesture('shaken'):
    # the Hub was shaken some time within the last 5 seconds
    print("test")
print("shaken")
