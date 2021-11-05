'''get_gesture()
Retrieves the most recently-detected gesture.
Returns
The gesture.
Type:String (text)
Values:'shaken','tapped','doubletapped','falling'
Example
'''
from spike import PrimeHub

hub = PrimeHub()

while True:
	if hub.motion_sensor.get_gesture() == 'falling':
		print("Aaah!")
		break
	print(hub.motion_sensor.get_gesture())
