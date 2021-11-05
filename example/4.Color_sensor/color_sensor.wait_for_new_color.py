wait_for_new_color()
Waits until the Color Sensor detects a new color.
The first time this method is called, it immediately returns the detected color. After that, it waits until the Color Sensor detects a color that’s different from the color that was detected the last time this method was used.
Returns
The name of the new color
Type
:
String (text)
Values
:
'black','violet','blue','cyan','green','yellow','red','white',None
Errors
RuntimeError
The sensor has been disconnected from the Port.
Example

wait_for_new_color()
Waits until the Color Sensor detects a new color.
The first time this method is called, it immediately returns the detected color. After that, it waits until the Color Sensor detects a color that’s different from the color that was detected the last time this method was used.
Returns
The name of the new color
Type
:
String (text)
Values
:
'black','violet','blue','cyan','green','yellow','red','white',None
Errors
RuntimeError
The sensor has been disconnected from the Port.
Example