'''get_speed()
Retrieves the motor speed.
Returns
The motor’s current speed
Type:integer (a positive or negative whole number, including 0)
Values:-100% to 100%
Errors
RuntimeError
The motor has been disconnected from the Port
'''

from spike import Motor

motor = Motor('A')


# Run the motor 90 degrees clockwise

motor.run_for_degrees(90,44)
print(str(motor.get_speed()))