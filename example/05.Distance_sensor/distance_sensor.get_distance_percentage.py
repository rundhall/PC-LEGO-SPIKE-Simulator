'''get_distance_percentage(short_range=False)
Retrieves the measured distance as a percentage.
Parameters
short_range
Whether or not to use short range mode. Short range mode increases accuracy, but it can only detect nearby objects.
Type:boolean
Values:True or False
Default:False
Returns
The measured distance or "none" if the distance can't be measured.
Type:integer (a positive or negative whole number, including 0)
Values:any value between 0 and 100
Errors
TypeError
short_range is not a boolean.
RuntimeError
The sensor has been disconnected from the Port.
Events'''
from spike import DistanceSensor
import time

# Initialize the Distance Sensor

wall_detector = DistanceSensor('E')


# Measure the distances between the Distance Sensor and object in centimeters or inches
while True:
    dist_distance = wall_detector.get_distance_percentage()
    # Print both results to the console
    print('distance in percentage:', dist_distance)
    time.sleep_ms(500)
