'''set_default_speed(default_speed)
Sets the default motor speed. This speed will be used when you omit the speed argument in one of the other methods, such as run_for_degrees.
Setting the default speed does not affect any motors that are currently running.
It will only have an effect when another motor method is called after this method.
If the value of default_speed is outside of the allowed range, the default speed will be set to "-100" or "100" depending on whether the value is negative or positive.
Parameters
default_speed
The default speed value.
Type:integer (a positive or negative whole number, including 0)
Values:-100% to 100%.
Default:no default value
Errors
TypeError
default_speed is not an integer.
'''
from spike import Motor

motor = Motor('A')

motor.set_default_speed(11)
#motor.run_for_rotations(2)

# The program will never proceed to here if the motor is stalled