'''get_position()
Retrieves the motor position. This is the clockwise angle between the moving marker and the zero-point marker on the motor.
Returns
The motor’s position.
Type:integer (a positive or negative whole number, including 0)
Values:0 to 359 degrees
Errors
RuntimeError
The motor has been disconnected from the Port.
'''
from spike import Motor

motor = Motor('A')


# Run the motor 90 degrees clockwise

print(str(motor.get_position()))