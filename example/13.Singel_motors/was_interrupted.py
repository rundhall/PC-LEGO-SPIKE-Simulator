'''was_interrupted()
Tests whether the motor was interrupted.
Returns
True if the motor was interrupted since the last time was_interrupted() was called, otherwise false.
Type:Boolean
Values:True or False
Errors
RuntimeError
The motor has been disconnected from the Port.
Example
'''
from spike import Motor

motor = Motor('A')

motor.run_for_rotations(2)
if not motor.was_interrupted():
    # the motor did not complete two rotations
    print("no interrupted")

