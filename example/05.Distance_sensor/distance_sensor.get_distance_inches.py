'''get_distance_inches(short_range=False)
Gets the measured distance in inches.
Parameters
short_range
Whether or not to use short range mode. Short range mode increases accuracy, but it can only detect nearby objects.
Type:boolean
Values:True or False
Default:False
Returns
The measured distance or "none" if the distance can't be measured.
Type:float (decimal number)
Values:any value between 0 and 79
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
    dist_cm = wall_detector.get_distance_cm()
    dist_inches = wall_detector.get_distance_inches()
    # Print both results to the console
    print('cm:', dist_cm, 'Inches:', dist_inches)
    time.sleep_ms(500)
