'''wait_until_color(color)
Waits until the Color Sensor detects the specified color.
Parameters
color
The name of the color
Type:String (text)
Values:"black","violet","blue","cyan","green","yellow","red","white",None
Default:no default value
Errors
TypeError
color is not a string or None.
ValueError
color is not one of the allowed values.
RuntimeError
The sensor has been disconnected from the Port.
Example
'''
from spike import ColorSensor

color_sensor = ColorSensor('A')

color_sensor.wait_until_color('white')
print('white color is there')
# Add actions after this
