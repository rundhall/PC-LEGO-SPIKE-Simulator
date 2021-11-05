'''stop()
Stops any sound that is playing.
Example
'''
from spike import PrimeHub

hub = PrimeHub()

hub.speaker.start_beep()

# Do something

hub.speaker.stop()
