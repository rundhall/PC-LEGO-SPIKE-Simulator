'''beep(note=60, seconds=0.2)
Plays a beep on the Hub.
Your program will not continue until seconds have passed.
Parameters
note
The MIDI note number.
Type:float (decimal number)
Values:44 to 123 ("60" is the middle C note)
Default:60 (middle C note)
seconds
The duration of the beep, specified in seconds.
Type:float (decimal number)
Values:any values
Default:0.2 seconds
Errors
TypeError
note is not an integer or seconds is not a number.
ValueError
note is not within the allowed range of 44-123.
Example
'''
from spike import PrimeHub

hub = PrimeHub()


# beep beep beep!

hub.speaker.beep(60, 0.5)
hub.speaker.beep(67, 0.5)
hub.speaker.beep(60, 0.5)
