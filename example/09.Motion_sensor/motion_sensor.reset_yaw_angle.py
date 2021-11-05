'''reset_yaw_angle()
Sets the yaw angle to "0."
'''

from spike import PrimeHub

hub = PrimeHub()

hub.motion_sensor.reset_yaw_angle()
angle = hub.motion_sensor.get_yaw_angle()
print('Angle:', angle)

# Angle is now 0
