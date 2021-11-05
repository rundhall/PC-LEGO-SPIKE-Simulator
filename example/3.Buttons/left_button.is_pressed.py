from spike import PrimeHub
from spike.control import wait_for_seconds

hub = PrimeHub()

for x in range(200):
    wait_for_seconds(1)
    if hub.left_button.is_pressed():
        print('button is pressed')