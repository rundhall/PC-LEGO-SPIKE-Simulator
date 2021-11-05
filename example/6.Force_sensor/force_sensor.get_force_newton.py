from spike import ForceSensor
from spike.control import wait_for_seconds


# Initialize the Force Sensor


door_bell = ForceSensor('E')


# Measure the force in newtons or as a percentage
while True:
    newtons = door_bell.get_force_newton()
    percentage = door_bell.get_force_percentage()
# Print both results

    print('N:', newtons, '=', percentage, '%')
    wait_for_seconds(1)

# Check whether the Force Sensor is pressed

#if door_bell.is_pressed():
 #   print('Hello!')
