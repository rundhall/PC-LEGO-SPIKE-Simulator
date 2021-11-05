'''get_default_speed()
Retrieves the default motor speed.
Returns
The default motor speed.
Type:integer (a positive or negative whole number, including 0)
Values:-100 to 100 %
Settings
'''
from spike import MotorPair

motor_pair = MotorPair('B', 'A')

print(str(motor_pair.get_default_speed()))