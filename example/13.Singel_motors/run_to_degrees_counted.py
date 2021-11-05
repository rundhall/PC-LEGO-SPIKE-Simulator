'''run_to_degrees_counted(degrees, speed=None)
Runs the motor until the number of degrees counted is equal to the value that has been specified by the "degrees" parameter.
The sign of the speed will be ignored, and the motor will always travel in the direction required to reach the specified number of degrees. If the speed is greater than "100," it will be limited to "100."
Parameters
degrees
The target degrees counted.
Type:integer (a positive or negative whole number, including 0)
Values:any number
Default:no default value
speed
The desired speed.
Type:integer (a positive or negative whole number, including 0)
Values:0 to 100% (positive values only)
Default:no default value
Errors
TypeError
degrees or speed is not an integer.
RuntimeError
The motor has been disconnected from the Port.
Example
'''
from spike import Motor
from spike.control import wait_for_seconds

motor = Motor('A')

for deg in range(0, 721, 90):
    motor.run_to_degrees_counted(deg)
    wait_for_seconds(1)
