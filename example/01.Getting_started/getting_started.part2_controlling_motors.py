from spike import Motor
from spike.control import wait_for_seconds
# Initialize the motor
motor = Motor('C')
# Rotate clockwise for 2 seconds at 75% speed
motor.run_for_seconds(2.0, 75)

# Rotate counterclockwise for 6.5 seconds at 30% speed
motor.run_for_seconds(6.5, -30)

from spike import Motor
# Initialize the motor
motor = Motor('C')
# Rotate the motor 360 degrees clockwise
motor.run_for_degrees(360)

# Run the motor 360 degrees clockwise, at 30% speed
motor.run_for_degrees(-360, 30)


from spike import Motor
# Initialize the motor
motor = Motor('C')
# Place the motor in position "0," aligning the markers
motor.run_to_position(0, 'shortest path', 75)


# Run the motor to different positions, at different speeds
wait_for_seconds(1)
motor.run_to_position(0, 'shortest path', 30)
wait_for_seconds(1)
motor.run_to_position(90, 'clockwise', 100)
