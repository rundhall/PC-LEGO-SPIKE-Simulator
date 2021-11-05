'''get_volume()
Retrieves the value of the speaker volume.
This only retrieves the volume of the Hub, not the programming app.
Returns
The current volume.
Type:integer (a positive or negative whole number, including 0)
Values:0 to 100%
'''

from spike import PrimeHub

hub = PrimeHub()


# Increase the volume of the Hub speaker by 10%

hub.speaker.set_volume(hub.speaker.get_volume() + 10)
