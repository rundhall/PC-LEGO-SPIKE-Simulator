'''light_up(right_top, left_top, right_bottom, left_bottom)
Sets the brightness of the individual lights on the Distance Sensor.
Parameters
right_top
The brightness of the light that’s above the right part of the Distance Sensor.
Type:integer (a positive or negative whole number, including 0)
Values:0 to 100% ("0" is off, and "100" is full brightness.)
Default:100
left_top
The brightness of the light that’s above the left part of the Distance Sensor.
Type:integer (a positive or negative whole number, including 0)
Values:0 to 100% ("0" is off, and "100" is full brightness.)
Default:100
right_bottom
The brightness of the light that’s below the right part of the Distance Sensor.
Type:integer (a positive or negative whole number, including 0)
Values:0 to 100% ("0" is off, and "100" is full brightness.)
Default:100
left_bottom
The brightness of the light that’s below the left part of the Distance Sensor.
Type:integer (a positive or negative whole number, including 0)
Values:0 to 100% ("0" is off, and "100" is full brightness.)
Default:100
Errors
TypeError
right_top, left_top, right_bottom or left_bottom is not a number.
RuntimeError
The sensor has been disconnected from the Port.
Example'''
from spike import DistanceSensor

distance_sensor = DistanceSensor('A')

for x in range (0,100,5):
# Switch on the top lights of the Distance Sensor
    distance_sensor.light_up(x, x, int(100-x), int(100-x))

