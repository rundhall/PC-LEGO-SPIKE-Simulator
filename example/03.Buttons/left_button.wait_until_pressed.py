from spike import PrimeHub

hub = PrimeHub()


# Beep every time the Left Button is pressed

while True:
    hub.left_button.wait_until_pressed()
    hub.speaker.start_beep()
    print('pressed')
    hub.left_button.wait_until_released()
    hub.speaker.stop()
    print('released')