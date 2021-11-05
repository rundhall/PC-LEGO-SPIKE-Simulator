wait_for_seconds(seconds)
Waits for a specified number of seconds before continuing the program.
Parameters
seconds
The time to wait, specified in seconds.
Type
:
float (decimal value)
Values
:
any value
Default
:
no default value
Errors
TypeError
seconds is not a number.
ValueError
seconds is not at least 0.
Example
from spike.control import wait_for_seconds


# wait for 3 seconds (pause the program flow)

wait_for_seconds(3)
