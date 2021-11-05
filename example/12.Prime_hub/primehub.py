The Hub is divided into six components, each with a number of functions linked to it.
To use the Hub, you must first initialiZe it.
Example
Constants
PrimeHub.left_button
The Left Button on the Hub.
Example
from spike import PrimeHub

hub = PrimeHub()

hub.left_button.wait_until_pressed()
PrimeHub.right_button
The Right Button on the Hub.
Example
from spike import PrimeHub

hub = PrimeHub()

hub.right_button.wait_until_pressed()
PrimeHub.speaker
The speaker inside the Hub.
Example
from spike import PrimeHub

hub = PrimeHub()

hub.speaker.beep()
PrimeHub.light_matrix
The Light Matrix on the Hub.
Example
from spike import PrimeHub

hub = PrimeHub()

hub.light_matrix.off()
PrimeHub.status_light
The Brick Status Light on the Hub’s Center Button.
Example
from spike import PrimeHub

hub = PrimeHub()

hub.status_light.on('blue')
PrimeHub.motion_sensor
The Motion Sensor inside the Hub.
Example
from spike import PrimeHub

hub = PrimeHub()

yaw = hub.motion_sensor.get_yaw_angle()
PrimeHub.PORT_A
The Port that's labeled "A" on the Hub.
PrimeHub.PORT_B
The Port that's labeled "B" on the Hub.
PrimeHub.PORT_C
The Port that's labeled "C" on the Hub.
PrimeHub.PORT_D
The Port that's labeled "D" on the Hub.
PrimeHub.PORT_E
The Port that's labeled "E" on the Hub.
PrimeHub.PORT_F
The Port that's labeled "F" on the Hub.
