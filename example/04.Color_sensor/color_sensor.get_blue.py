'''get_blue()
Retrieves the color intensity of blue.
Returns
Type:integer (a positive or negative whole number, including 0)
Values:0 to 1024
Errors
RuntimeError
The sensor has been disconnected from the Port.
'''
from spike import ColorSensor
import time

# Initialize the Color Sensor

paper_scanner = ColorSensor('E')


# Measure the color blue
while True: 
    blue = paper_scanner.get_blue()
    # Print the color name to the console
    print('Measured blue:', blue)
    time.sleep_ms(1000)