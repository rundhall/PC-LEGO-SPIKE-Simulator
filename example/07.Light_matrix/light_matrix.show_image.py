'''
Following are all of the functions that are linked to the Light Matrix.
Actions
show_image(image, brightness=100)
Shows an image on the Light Matrix.
Parameters
image
Name of the image.
Type:String (text)
Values:ANGRY, ARROW_E, ARROW_N, ARROW_NE, ARROW_NW, ARROW_S, ARROW_SE, ARROW_SW, ARROW_W, ASLEEP, BUTTERFLY, CHESSBOARD, CLOCK1, CLOCK10, CLOCK11, CLOCK12, CLOCK2, CLOCK3, CLOCK4, CLOCK5, CLOCK6, CLOCK7, CLOCK8, CLOCK9, CONFUSED, COW, DIAMOND, DIAMOND_SMALL, DUCK, FABULOUS, GHOST, GIRAFFE, GO_RIGHT, GO_LEFT, GO_UP, GO_DOWN, HAPPY, HEART, HEART_SMALL, HOUSE, MEH, MUSIC_CROTCHET, MUSIC_QUAVER, MUSIC_QUAVERS, NO, PACMAN, PITCHFORK, RABBIT, ROLLERSKATE, SAD, SILLY, SKULL, SMILE, SNAKE, SQUARE, SQUARE_SMALL, STICKFIGURE, SURPRISED, SWORD, TARGET, TORTOISE, TRIANGLE, TRIANGLE_LEFT, TSHIRT, UMBRELLA, XMAS, YES
Default:no default value
brightness
Brightness of the image
Type:integer (a positive or negative whole number, including 0)
Values:0 to 100%
Default:100
Errors
TypeError
image is not a string or brightness is not an integer.
ValueError
image is not one of the allowed values.
Example'''
from spike import PrimeHub
from spike.control import wait_for_seconds

hub = PrimeHub()
while True:
    hub.light_matrix.show_image('HAPPY')
    wait_for_seconds(1)
    hub.light_matrix.show_image('HEART_SMALL')
    wait_for_seconds(1)
