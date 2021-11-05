now()
Retrieves the "right now" time of the Timer.
Returns
The current time, specified in seconds.
Type
:
Integer (a positive or negative whole number, including 0)
Values
:
A value greather than 0
Example
from spike.control import Timer

timer = Timer()

while True:
    # If it has been more than 5 seconds since the Timer started
    if timer.now() > 5:
        # then break out of the while loop
        break