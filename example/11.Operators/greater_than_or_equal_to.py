greater_than_or_equal_to(a, b)
Tests whether "a" is greater than or equal to "b."
This is the same as "a >= b."
Parameters
a
Any object that can be compared to "b."
Type
:
any type
Values
:
any value
Default
:
no default value
b
Any object that can be compared to "a."
Type
:
any type
Values
:
any value
Default
:
no default value
Returns
Type
:
Boolean
Values
:
True if a >= b, otherwise False.
Example
from spike import ColorSensor
from spike.control import wait_until
from spike.operator import greater_than_or_equal_to

color_sensor = ColorSensor('A')

wait_until(color_sensor.get_reflected_light, greater_than_or_equal_to, 50)
