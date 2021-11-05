'''get_green()
Retrieves the color intensity of green.
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
    # Measure the color green
    green = paper_scanner.get_green()
    # Print the color green to the console
    print('Measured green:', green)
