'''Events
wait_for_distance_farther_than(distance, unit='cm', short_range=False)
Waits until the measured distance is greater than the specified distance.
Parameters
distance
The target distance to be detected from the sensor to an object.
Type:float (decimal number)
Values:any value
Default:no default value
unit
The unit in which the distance is measured.
Type:String (text)
Values:"cm","in","%"
Default:cm
short_range
Whether or not to use short range mode. Short range mode increases accuracy, but it can only detect nearby objects.
Type:boolean
Values:True or False
Default:False
Errors
TypeError
distance is not a number or unit is not a string or short_range is not a boolean.
ValueError
unit is not one of the allowed values.
RuntimeError
The sensor has been disconnected from the Port.
Example
'''
from spike import DistanceSensor
import time

distance_sensor = DistanceSensor('A')

while True:
    distance_sensor.wait_for_distance_farther_than(20, 'cm')
    print('It is closer')
    time.sleep_ms(500)
    
    # do something, for example, start a motor
    distance_sensor.wait_for_distance_closer_than(30, 'cm')
    print('It is farther')
    time.sleep_ms(500)
    # do something, for example, stop a motor
