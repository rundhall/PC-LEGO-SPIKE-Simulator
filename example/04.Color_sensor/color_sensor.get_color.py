'''get_color()
Retrieves the detected color of a surface.
Returns
Name of the color.
Type:String (text)
Values:'black','violet','blue','cyan','green','yellow','red','white',None
Errors
RuntimeError
The sensor has been disconnected from the Port.
Example
'''
from spike import ColorSensor
import time

# Initialize the Color Sensor

paper_scanner = ColorSensor('E')


# Measure the color
while True: 
    color = paper_scanner.get_color()
    # Print the color name to the console
    print('Detected:', color)
    time.sleep_ms(1000)
    # Check if it's a specific color
    if color == 'red':
        print('It is red!')
