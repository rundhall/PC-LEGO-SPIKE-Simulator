'''get_yaw_angle()
Retrieves the Hub’s yaw angle.
Yaw is the rotation around the front-back (vertical) axis. Pitch the is rotation around the left-right (transverse) axis. Roll the is rotation around the front-back (longitudinal) axis.
Returns
The yaw angle, specified in degrees.
Type:Integer (a positive or negative whole number, including 0)
Values:-180 to 180
Example
'''
from spike import PrimeHub

hub = PrimeHub()

while True:
    if hub.motion_sensor.get_yaw_angle() > 90:
        break