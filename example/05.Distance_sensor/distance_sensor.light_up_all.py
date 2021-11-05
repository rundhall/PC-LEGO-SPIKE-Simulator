'''light_up_all(brightness=100)
Lights up all of the lights on the Distance Sensor at the specified brightness.
Parameters
brightness
The specified brightness of all of the lights.
Type:integer (a positive or negative whole number, including 0)
Values:0 to 100% ("0" is off, and "100" is full brightness.)
Default:100
Errors
TypeError
brightness is not a number.
RuntimeError
The sensor has been disconnected from the Port.
Example
'''
from machine import sleep
from spike import DistanceSensor
from spike import ColorSensor

distance_sensor = DistanceSensor('A')
color_sensor = ColorSensor('A')

# Turn on the lights

distance_sensor.light_up_all()


# Turn off the lights
for x in range (10):
    distance_sensor.light_up_all(x)
    sleep(100)
    # Turn off the lights
for x in range (10):
    color_sensor.light_up_all(x)
    sleep(100)
    
distance_sensor.light_up_all(100)
color_sensor.light_up_all(200)
