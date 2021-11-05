'''set_stall_detection(stop_when_stalled)
Turns stall detection on or off.
Stall detection senses when a motor has been blocked and can’t move. If stall detection has been enabled and a motor is blocked, the motor will be powered off after two seconds and the current motor command will be interrupted. If stall detection has been disabled, the motor will keep trying to run and programs will "get stuck" until the motor is no longer blocked.
Stall detection is enabled by default.
Parameters
stop_when_stalled
Choose "true" to enable stall detection or "false" to disable it.
Type:boolean
Values:True or False
Default:True
Errors
TypeError
stop_when_stalled is not a boolean.
RuntimeError
The motor has been disconnected from the Port.
Example
'''
from spike import Motor

motor = Motor('A')

motor.set_stall_detection(False)
#motor.run_for_rotations(2)

# The program will never proceed to here if the motor is stalled