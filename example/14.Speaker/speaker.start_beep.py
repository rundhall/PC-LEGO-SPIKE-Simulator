'''start_beep(note=60)
Starts playing a beep.
The beep will play indefinitely until stop() or another beep method is called.
Parameters
note
The MIDI note number.
Type:float (decimal number)
Values:44 to 123 ("60" is the middle C note)
Default:60 (middle C note)
Errors
TypeError
note is not an integer.
ValueError
note is not within the allowed range of 44-123
Example
'''
from spike import PrimeHub

hub = PrimeHub()

hub.speaker.start_beep()

# Do something

hub.speaker.stop()
