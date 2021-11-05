'''
light_up_all(brightness=100)
Lights up all of the lights on the Color Sensor at the specified brightness.
This causes the Color Sensor to change modes, which can affect your program in unexpected ways. For example, the Color Sensor can't read colors when it's in light up mode.
Parameters
brightness
The desired brightness of the lights on the Color Sensor.
Type:integer (a positive or negative whole number, including 0)
Values:0 to 100% ("0" is off, and "100" is full brightness.)
Default:100%
Errors
TypeError
brightness is not an integer.
RuntimeError
The sensor has been disconnected from the Port.
Example
'''
from spike import ColorSensor
from machine import sleep

color_sensor = ColorSensor('A')


# Turns on the Color Sensor's lights

color_sensor.light_up_all()


# Turns off the Color Sensor's lights


# Turn off the lights
for x in range (250):
    color_sensor.light_up_all(x)
    sleep(60)
