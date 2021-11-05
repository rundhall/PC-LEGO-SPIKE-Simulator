'''stop()
Stops both motors simultaneously, which will stop a Driving Base.
The motors will either actively hold their current position or coast freely depending on the option that’s been selected by set_stop_action().
Errors
RuntimeError
One or both of the motors has been disconnected or the motors could not be paired.
Example
'''
from spike import MotorPair
import time
motor_pair = MotorPair('B', 'A')

motor_pair.start()

# wait for something
time.sleep_ms(1000)
motor_pair.stop()