'''get_roll_angle()
Retrieves the Hub’s roll angle.
Roll is the rotation around the front-back (longitudinal) axis. Yaw is the rotation around the front-back (vertical) axis. Pitch is the rotation around the left-right (transverse) axis.
Returns
The roll angle, specified in degrees.
Type:Integer (a positive or negative whole number, including 0)
Values:-180 to 180
Example
'''
from spike import PrimeHub

hub = PrimeHub()

while True:
    if hub.motion_sensor.get_roll_angle() > 90:
        break

    # do something
