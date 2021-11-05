'''
light_up(light_1, light_2, light_3)
Sets the brightness of the individual lights on the Color Sensor.
This causes the Color Sensor to change modes, which can affect your program in unexpected ways. For example, the Color Sensor can't read colors when it's in light up mode.
Parameters
light_1
The desired brightness of light 1.
Type:integer (a positive or negative whole number, including 0)
Values:0 to 100% ("0" is off, and "100" is full brightness.)
Default:100%
light_2
The desired brightness of light 2.
Type:integer (a positive or negative whole number, including 0)
Values:0 to 100% ("0" is off, and "100" is full brightness.)
Default:100%
light_3
The desired brightness of light 3.
Type:integer (a positive or negative whole number, including 0)
Values:0 to 100% ("0" is off, and "100" is full brightness.)
Default:100%
Errors
TypeError
light_1, light_2, or light_3 is not an integer.
RuntimeError
The sensor has been disconnected from the Port.
Example

light_up(light_1, light_2, light_3)
Sets the brightness of the individual lights on the Color Sensor.
This causes the Color Sensor to change modes, which can affect your program in unexpected ways. For example, the Color Sensor can't read colors when it's in light up mode.

'''
from spike import ColorSensor, time
from spike.control import wait_for_seconds

# Initialize the Color Sensor

paper_scanner = ColorSensor('E')


# Change the light 
for x in range(100):
    rgb_intensity = paper_scanner.light_up(x,x,x)
    wait_for_seconds(0.5)
    print("light_up:",str(x))

