'''was_stalled()
Tests whether the motor was stalled.
Returns
True if the motor has stalled since the last time was_stalled() was called, otherwise false.
Type:Boolean
Values:True or False
Errors
RuntimeError
The motor has been disconnected from the Port.
Example
'''
from spike import Motor

motor = Motor('A')

motor.set_stall_detection(True)
motor.run_for_rotations(2)
if not motor.was_stalled():
    # the motor did not complete two rotations
    print("no stalled")
