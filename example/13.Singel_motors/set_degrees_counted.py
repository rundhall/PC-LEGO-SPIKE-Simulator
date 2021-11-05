'''set_degrees_counted(degrees_counted)
Sets the "number of degrees counted" to the desired value.
Parameters
degrees_counted
The value to which the number of degrees counted should be set.
Type:integer (a positive or negative whole number, including 0)
Values:any number
Default:no default value
Errors
TypeError
degrees_counted is not an integer.
RuntimeError
The motor has been disconnected from the Port
'''
from spike import Motor

motor = Motor('A')

motor.set_degrees_counted(10)
#motor.run_for_rotations(2)

# The program will never proceed to here if the motor is stalled