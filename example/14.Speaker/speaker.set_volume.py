'''set_volume(volume)
Sets the speaker volume.
If the assigned volume is out of range, the nearest volume (i.e., 0 or 100) will be used instead. This only sets the volume of the Hub, not the programming app.
Parameters
volume
The new volume percentage.
Type:integer (a positive or negative whole number, including 0)
Values:0 to 100%
Default:100%
Errors
TypeError
volume is not an integer.
Example
'''
from spike import PrimeHub

hub = PrimeHub()


# Set the Hub speaker volume to 50%

hub.speaker.set_volume(50)
