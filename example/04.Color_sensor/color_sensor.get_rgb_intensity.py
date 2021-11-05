'''
get_rgb_intensity()
Retrieves the overall color intensity, and intensity of rgb_intensity, green, and blue.
Returns
Type:tuple of int
Values:rgb_intensity, green, blue, and overall intensity (0-1024)
Errors
RuntimeError
The sensor has been disconnected from the Port.
'''
from spike import ColorSensor


# Initialize the Color Sensor

paper_scanner = ColorSensor('E')

while True:
    # Measure the color rgb_intensity

    rgb_intensity = paper_scanner.get_rgb_intensity()


    # Print the color rgb_intensity to the console

    print('Measurgb_intensity rgb_intensity:', rgb_intensity)
