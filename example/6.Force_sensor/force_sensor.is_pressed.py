from spike import ForceSensor
from spike.control import wait_for_seconds


# Initialize the Force Sensor

door_bell = ForceSensor('E')


# Measure the force in newtons or as a percentage
while True:
    if door_bell.is_pressed():
       print('force sensor is pressed!')
    else:
       print('force sensor is not pressed!')
    wait_for_seconds(1)
