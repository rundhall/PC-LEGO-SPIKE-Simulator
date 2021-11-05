'''wait_for_new_color()
Waits until the Color Sensor detects a new color.
The first time this method is called, it immediately returns the detected color. After that, it waits until the Color Sensor detects a color that’s different from the color that was detected the last time this method was used.
Returns
The name of the new color
Type:String (text)
Values:'black','violet','blue','cyan','green','yellow','red','white',None
Errors
RuntimeError
The sensor has been disconnected from the Port.
Example
'''
from spike import ColorSensor, time
from spike.control import wait_for_seconds

# Initialize the Color Sensor

paper_scanner = ColorSensor('E')


# Change the light 
for x in range(100):
    new_color = paper_scanner.wait_for_new_color()
    print("new color:",new_color)
    wait_for_seconds(1)
    
