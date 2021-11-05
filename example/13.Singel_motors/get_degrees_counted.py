'''get_degrees_counted()
Retrieves the number of degrees that have been counted by the motor.
Returns
The number of degrees that’s been counted.
Type:integer (a positive or negative whole number, including 0)
Values:any number
Errors
RuntimeError
The motor has been disconnected from the Port.
'''
from spike import Motor

motor = Motor('A')


# Run the motor 90 degrees clockwise

print(str(motor.get_degrees_counted()))