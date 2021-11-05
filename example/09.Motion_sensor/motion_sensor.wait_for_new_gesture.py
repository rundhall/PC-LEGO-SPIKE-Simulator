'''wait_for_new_gesture()
Waits until a new gesture happens.
Returns
The new gesture.
Type:String (text)
Values:'shaken','tapped','doubletapped','falling'
Example
'''
from spike import PrimeHub

hub = PrimeHub()

gesture=" "
while gesture != "shaken":
    gesture = hub.motion_sensor.wait_for_new_gesture()
if gesture == 'shaken':
    # do one thing
    print("shaken")
elif gesture == 'tapped':
    # do another thing
    print("tapped")

