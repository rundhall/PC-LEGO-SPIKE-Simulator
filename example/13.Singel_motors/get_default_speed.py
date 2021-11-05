'''
get_default_speed()
Retrieves the current default motor speed.
Returns
The default motor’s speed.
Type:integer (a positive or negative whole number, including 0)
Values:(-100% to 100%).
'''
from spike import Motor

motor = Motor('A')

print(str(motor.get_default_speed()))