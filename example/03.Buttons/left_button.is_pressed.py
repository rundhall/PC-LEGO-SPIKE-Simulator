from spike import PrimeHub
from spike.control import wait_for_seconds

hub = PrimeHub()

for x in range(200):
    wait_for_seconds(0.5)
    if hub.left_button.is_pressed():
        print('left button is pressed')
    if hub.right_button.is_pressed():
        print('right button is pressed')