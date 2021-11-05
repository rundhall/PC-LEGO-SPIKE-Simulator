stop()
Stops the motor.
What the motor does after it stops depends on the action that’s been set in set_stop_action(). The default value of set_stop_action() is "coast."
Errors
RuntimeError
The motor has been disconnected from the Port.
Example
from spike import Motor

motor = Motor('A')

motor.start()

# wait until something

motor.stop()
Measurements