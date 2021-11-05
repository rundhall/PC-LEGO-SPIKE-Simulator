'''get_red()
Retrieves the color intensity of red.
Returns
Type:integer (a positive or negative whole number, including 0)
Values:0 to 1024
Errors
RuntimeError
The sensor has been disconnected from the Port.
'''
from spike import ColorSensor


# Initialize the Color Sensor

paper_scanner = ColorSensor('E')

while True:
    # Measure the color red

    red = paper_scanner.get_red()


    # Print the color red to the console

    print('Measured red:', red)
