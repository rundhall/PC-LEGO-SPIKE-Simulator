'''
Example program for checking ESP LEGO SPIKE simulator
Source: LEGO Education SPIKE 2.0.0 
Controlling the Light Matrix
Create your first program using Python.

Copy the code shown below by clicking or tapping the copy icon  in the box.
Paste the code to the Programming Canvas, where you’ll write your code.

The green lines are simply comments. They won’t influence your program's actions. The other lines are your program. Can you figure out what this first program will do?

Play the program.'''
# Import the PrimeHub class
from spike import PrimeHub
from spike.control import wait_for_seconds
# Initialize the Hub
your_hub = PrimeHub()
# Light up a smiley face


your_hub.light_matrix.show_image('HEART_SMALL')
wait_for_seconds(1)
your_hub.light_matrix.show_image('HAPPY')
wait_for_seconds(1)
your_hub.light_matrix.show_image('SMILE')
wait_for_seconds(1)
your_hub.light_matrix.show_image('SAD')
wait_for_seconds(1)
your_hub.light_matrix.show_image('CONFUSED')
wait_for_seconds(1)
your_hub.light_matrix.show_image('ANGRY')
wait_for_seconds(1)
your_hub.light_matrix.show_image('ASLEEP')
wait_for_seconds(1)
your_hub.light_matrix.show_image('SURPRISED')
wait_for_seconds(1)
your_hub.light_matrix.show_image('SILLY')
wait_for_seconds(1)
your_hub.light_matrix.show_image('FABULOUS')
wait_for_seconds(1)
your_hub.light_matrix.show_image('MEH')
wait_for_seconds(1)
your_hub.light_matrix.show_image('YES')
wait_for_seconds(1)
your_hub.light_matrix.show_image('NO')
wait_for_seconds(1)
your_hub.light_matrix.show_image('CLOCK12')
wait_for_seconds(1)
your_hub.light_matrix.show_image('CLOCK1')
wait_for_seconds(1)
your_hub.light_matrix.show_image('CLOCK2')
wait_for_seconds(1)
your_hub.light_matrix.show_image('CLOCK3')
wait_for_seconds(1)
your_hub.light_matrix.show_image('CLOCK4')
wait_for_seconds(1)
your_hub.light_matrix.show_image('CLOCK5')
wait_for_seconds(1)
your_hub.light_matrix.show_image('CLOCK6')
wait_for_seconds(1)
your_hub.light_matrix.show_image('CLOCK7')
wait_for_seconds(1)
your_hub.light_matrix.show_image('CLOCK8')
wait_for_seconds(1)
your_hub.light_matrix.show_image('CLOCK9')
wait_for_seconds(1)
your_hub.light_matrix.show_image('CLOCK10')
wait_for_seconds(1)
your_hub.light_matrix.show_image('CLOCK11')
wait_for_seconds(1)
your_hub.light_matrix.show_image('ARROW_N')
wait_for_seconds(1)
your_hub.light_matrix.show_image('ARROW_NE')
wait_for_seconds(1)
your_hub.light_matrix.show_image('ARROW_E')
wait_for_seconds(1)
your_hub.light_matrix.show_image('ARROW_SE')
wait_for_seconds(1)
your_hub.light_matrix.show_image('ARROW_S')
wait_for_seconds(1)
your_hub.light_matrix.show_image('ARROW_SW')
wait_for_seconds(1)
your_hub.light_matrix.show_image('ARROW_W')
wait_for_seconds(1)
your_hub.light_matrix.show_image('ARROW_NW')
wait_for_seconds(1)
your_hub.light_matrix.show_image('GO_RIGHT')
wait_for_seconds(1)
your_hub.light_matrix.show_image('GO_LEFT')
wait_for_seconds(1)
your_hub.light_matrix.show_image('GO_UP')
wait_for_seconds(1)
your_hub.light_matrix.show_image('GO_DOWN')
wait_for_seconds(1)
your_hub.light_matrix.show_image('TRIANGLE')
wait_for_seconds(1)
your_hub.light_matrix.show_image('TRIANGLE_LEFT')
wait_for_seconds(1)
your_hub.light_matrix.show_image('CHESSBOARD')
wait_for_seconds(1)
your_hub.light_matrix.show_image('DIAMOND')
wait_for_seconds(1)
your_hub.light_matrix.show_image('DIAMOND_SMALL')
wait_for_seconds(1)
your_hub.light_matrix.show_image('SQUARE')
wait_for_seconds(1)
your_hub.light_matrix.show_image('SQUARE_SMALL')
wait_for_seconds(1)
your_hub.light_matrix.show_image('RABBIT')
wait_for_seconds(1)
your_hub.light_matrix.show_image('COW')
wait_for_seconds(1)
your_hub.light_matrix.show_image('MUSIC_CROTCHET')
wait_for_seconds(1)
your_hub.light_matrix.show_image('MUSIC_QUAVER')
wait_for_seconds(1)
your_hub.light_matrix.show_image('MUSIC_QUAVERS')
wait_for_seconds(1)
your_hub.light_matrix.show_image('PITCHFORK')
wait_for_seconds(1)
your_hub.light_matrix.show_image('XMAS')
wait_for_seconds(1)
your_hub.light_matrix.show_image('PACMAN')
wait_for_seconds(1)
your_hub.light_matrix.show_image('TARGET')
wait_for_seconds(1)
your_hub.light_matrix.show_image('TSHIRT')
wait_for_seconds(1)
your_hub.light_matrix.show_image('ROLLERSKATE')
wait_for_seconds(1)
your_hub.light_matrix.show_image('DUCK')
wait_for_seconds(1)
your_hub.light_matrix.show_image('HOUSE')
wait_for_seconds(1)
your_hub.light_matrix.show_image('TORTOISE')
wait_for_seconds(1)
your_hub.light_matrix.show_image('BUTTERFLY')
wait_for_seconds(1)
your_hub.light_matrix.show_image('STICKFIGURE')
wait_for_seconds(1)
your_hub.light_matrix.show_image('GHOST')
wait_for_seconds(1)
your_hub.light_matrix.show_image('SWORD')
wait_for_seconds(1)
your_hub.light_matrix.show_image('GIRAFFE')
wait_for_seconds(1)
your_hub.light_matrix.show_image('SKULL')
wait_for_seconds(1)
your_hub.light_matrix.show_image('UMBRELLA')
wait_for_seconds(1)
your_hub.light_matrix.show_image('SNAKE')
wait_for_seconds(1)
your_hub.light_matrix.show_image('ALL_CLOCKS')
wait_for_seconds(1)
your_hub.light_matrix.show_image('ALL_ARROWS')
wait_for_seconds(1)
your_hub.light_matrix.off()


'''Change the image that’s displayed on the Light Matrix.
Change the parameter "HAPPY" to "HEART" in the code you already have. This will light up the heart instead of the happy face on the Hub.
Or, copy the code from the box below and paste it after the last line of your program. This will light up the happy face for 5 seconds and then light up a heart for 5 seconds.'''
'''
# Add another image
your_hub.light_matrix.show_image('HEART')
wait_for_seconds(5)
your_hub.light_matrix.off()
'''

'''
Playing Short Beeps and Time
Let’s make the Hub play some beeps.

If there's already a program on your Programming Canvas, it’s a good idea to delete it or start a new project before continuing.
Copy the code shown below to the Programming Canvas.
Make sure that you only have one line of code that starts with: from spike import.
Play the program!'''
''''# Import the PrimeHub class
from spike import PrimeHub
from spike.control import wait_for_seconds
# Initialize the Hub
hub = PrimeHub()
# beep beep beep!
hub.speaker.beep(60, 1)
'''
'''Change the beat and tone. This is one way of doing it.'''
'''# Here’s a new song
hub.speaker.beep(44, 0.5)
hub.speaker.beep(123, 1.0)
wait_for_seconds(0.5)
hub.speaker.beep(20, 0.5)
'''
'''Playing Sounds
You can also add sounds to be played from your device.

Copy the code shown below to the Programming Canvas. Play the program!'''
'''
# Import the PrimeHub class
from spike import App
# Initialize the app
app = App()
app.play_sound('Cat Meow 1')
'''
'''Pick another sound to play, or use this program.'''
'''app.play_sound('Triumph')
'''
