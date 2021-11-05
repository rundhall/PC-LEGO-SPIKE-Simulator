from spike import PrimeHub
from spike import ForceSensor
import time

hub = PrimeHub()

force_sensor = ForceSensor('A')

while True:
    force_sensor.wait_until_pressed()
    # do something, for example,
    hub.speaker.start_beep()
    print('pressed')
    time.sleep_ms(1000)
    force_sensor.wait_until_released()
    # do something, for example,
    hub.speaker.stop()
    print('released')
    time.sleep_ms(1000)
