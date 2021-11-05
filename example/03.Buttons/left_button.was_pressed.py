from spike import PrimeHub
from spike.control import wait_for_seconds

hub = PrimeHub()

while True:
    wait_for_seconds(3)
    if hub.left_button.was_pressed():
        print('button was pressed')
        # Do something