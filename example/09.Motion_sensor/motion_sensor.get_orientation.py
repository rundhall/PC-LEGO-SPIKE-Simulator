'''get_orientation()
Retrieves the Hub's current orientation.
Returns
The Hub’s current orientation.
Type:String (text)
Values:'front','back','up','down','leftside','rightside'
Example
'''
from spike import PrimeHub

hub = PrimeHub()
while True:
    if hub.motion_sensor.get_orientation() == 'front':
        print ('front')
        break
    # do something
