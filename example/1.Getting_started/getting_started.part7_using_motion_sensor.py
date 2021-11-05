from spike import PrimeHub, App
# Initialize the Hub and app
hub = PrimeHub()
app = App()

while True:
	orientation = hub.motion_sensor.wait_for_new_orientation()
	if orientation == 'front':
		hub.light_matrix.show_image('ASLEEP')
		app.start_sound('Snoring')
	elif orientation == 'up':
		hub.light_matrix.show_image('HAPPY')
		app.start_sound('Triumph')


while True:
	angle = abs(hub.motion_sensor.get_pitch_angle()) * 2
	hub.light_matrix.show_image('HAPPY', angle)
