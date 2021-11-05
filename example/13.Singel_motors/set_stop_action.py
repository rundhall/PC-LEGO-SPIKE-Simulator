'''set_stop_action(action)
Sets the default behavior when a motor stops.
Parameters
action
The desired motor behavior when the motor stops.
Type:String (text)
Values:"coast","brake","hold"
Default:coast
Errors
TypeError
action is not a string.
ValueError
action is not one of the allowed values.
RuntimeError
The motor has been disconnected from the Port.
'''
from spike import Motor

motor = Motor('A')

motor.set_stop_action("brake")
#motor.run_for_rotations(2)

# The program will never proceed to here if the motor is stalled
