from spike import MotorPair
# Initialize the motor pair
motor_pair = MotorPair('E', 'F')
# Initialize default speed
motor_pair.set_default_speed(50)
# Move in one direction for 2 seconds
motor_pair.move(2, 'seconds')

# Move in the other direction for 2 seconds
motor_pair.set_default_speed(-50)
motor_pair.move(2, 'seconds')

from spike import MotorPair
# Initialize the motor pair
motor_pair = MotorPair('E', 'F')
# Turn in one direction for 2 seconds
motor_pair.move_tank(10, 'cm', left_speed=25, right_speed=75)

# Move in the other direction for 2 seconds
motor_pair.move_tank(1, 'rotations', left_speed=-50, right_speed=50)
