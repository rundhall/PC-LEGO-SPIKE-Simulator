'''
get_reflected_light()
Retrieves the intensity of the reflected light.
Returns
The reflected light intensity.
Type:integer (a positive or negative whole number, including 0)
Values:0 to 100 %
Errors
RuntimeError
The sensor has been disconnected from the Port.
'''
from spike import ColorSensor


# Initialize the Color Sensor

paper_scanner = ColorSensor('E')


# Measure the color reflected_light

reflected_light = paper_scanner.get_reflected_light()


# Print the color reflected_light to the console

print('Measurgb_intensity reflected_light:', reflected_light)