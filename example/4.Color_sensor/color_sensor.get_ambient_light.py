Retrieves the intensity of the ambient light.
This causes the Color Sensor to change modes, which can affect your program in unexpected ways. For example, the Color Sensor can't read colors when it's in ambient light mode.

Returns
The ambient light intensity.
Type
:
integer (a positive or negative whole number, including 0)
Values
:
0 to 100 %
Errors
RuntimeError
The sensor has been disconnected from the Port.