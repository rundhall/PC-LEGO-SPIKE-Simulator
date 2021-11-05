start_at_power(power)
Starts rotating the motor at a specified power level.
The motor will keep moving at this power level until you give it another motor command or when your program ends.
Parameters
power
Power of the motor.
Type
:
integer (a positive or negative whole number, including 0)
Values
:
-100% to 100%
Default
:
no default value
Errors
TypeError
power is not an integer.
RuntimeError
The motor has been disconnected from the Port.
Measurements