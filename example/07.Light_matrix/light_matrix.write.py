write(text)
Displays text on the Light Matrix, one letter at a time, scrolling from right to left.
Your program will not continue until all of the letters have been shown.
Parameters
text
Text to write.
Type
:
String (text)
Values
:
Any text
Default
:
no default value
Example
from spike import PrimeHub

hub = PrimeHub()

hub.light_matrix.write('Hello!')


# Show the number "1" on the Light Matrix

hub.light_matrix.write('1')
