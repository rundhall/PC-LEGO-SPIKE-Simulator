'''set_pixel(x, y, brightness=100)
Sets the brightness of one pixel (one of the 25 LEDs) on the Light Matrix.
Parameters
x
Pixel position, counting from the left.
Type:integer (a positive or negative whole number, including 0)
Values:1 to 5
Default:no default value
y
Pixel position, counting from the top.
Type:integer (a positive or negative whole number, including 0)
Values: 1 to 5
Default:no default value
brightness
Brightness of the pixel
Type:integer (a positive or negative whole number, including 0)
Values:0 to 100%
Default:100
Errors
TypeError
x, y or brightness is not an integer.
ValueError
x, y is not within the allowed range of 0-4.
Example
'''
from spike import PrimeHub

hub = PrimeHub()

hub.light_matrix.set_pixel(1, 4)
