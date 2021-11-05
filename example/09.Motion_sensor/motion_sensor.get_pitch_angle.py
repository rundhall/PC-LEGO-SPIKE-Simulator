'''get_pitch_angle()
Retrieves the Hub’s pitch angle.
Pitch is the rotation around the left-right (transverse) axis. Roll is the rotation around the front-back (longitudinal) axis. Yaw is the rotation around the front-back (vertical) axis.
Returns
The pitch angle, specified in degrees.
Type:Integer (a positive or negative whole number, including 0)
Values:-180 to 180
Example
'''
from spike import PrimeHub

hub = PrimeHub()

while True:
    if hub.motion_sensor.get_pitch_angle() > 90:
        break
        # do something
