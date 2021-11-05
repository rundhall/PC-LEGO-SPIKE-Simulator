'''wait_for_new_orientation()
Waits until the Hub’s orientation changes.
The first time this method is called, it will immediately return the current value. After that, calling this method will block the program until the Hub’s orientation has changed since the previous time this method was called.
Returns
The Hub’s new orientation.
Type:String (text)
Values:'front', 'back', 'up', 'down', 'leftside', 'rightside'
Example
'''
from spike import PrimeHub

hub = PrimeHub()
orientation=" "
while orientation != "leftside":
    orientation = hub.motion_sensor.wait_for_new_orientation()
if orientation == 'leftside':
    print("leftside")
elif orientation == 'rightside':
    print("rightside")

