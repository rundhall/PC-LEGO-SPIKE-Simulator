wait_until(get_value_function, operator_function=<function equal_to>, target_value=True)
Waits until the condition is true before continuing with the program.
Parameters
get_value_function
Type
:
callable function
Values
:
A function that returns the current value to be compared to the target value.
Default
:
no default value
operator_function
Type
:
callable function
Values
:
A function that compares two arguments. The first argument will be the result of get_value_function(), and the second argument will be target_value. The function will compare both values and return the result.
Default
:
no default value
target_value
Type
:
any type
Values
:
Any object that can be compared by operator_function.
Default
:
no default value
Errors
TypeError
get_value_function or operator_function is not callable or operator_function does not compare two arguments.
Example
from spike import ColorSensor
from spike.control import wait_until
from spike.operator import equal_to

color_sensor = ColorSensor('A')


# Wait for the Color Sensor to detect "red"

wait_until(color_sensor.get_color, equal_to, 'red')
Example
from spike import ColorSensor, Motor
from spike.control import wait_until

color_sensor = ColorSensor('A')
motor = Motor('B')

def red_or_position():
    return color_sensor.get_color() == 'red' or motor.get_position() > 90

wait_until(red_or_position)
