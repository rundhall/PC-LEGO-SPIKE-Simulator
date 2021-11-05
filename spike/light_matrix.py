class Light_matrix:
	#If ISDEBUG is true. then all modules send debug information through console
	ISDEBUG = True

	HEART = "09090:99999:99999:09990:00900"
	HEART_SMALL =  "00000:09090:09990:00900:00000"
	HAPPY =  "00000:09090:00000:90009:09990"
	ASLEEP =  "00000:99099:00000:09990:00000"
	SMILE =  "00000:00000:00000:90009:09990"
	SAD =  "00000:09090:00000:09990:90009"
	CONFUSED =  "00000:09090:00000:09090:90909"
	ANGRY =  "90009:09090:00000:99999:90909"
	SURPRISED =  "09090:00000:00900:09090:00900"
	SILLY =  "90009:00000:99999:00909:00999"
	FABULOUS =  "99999:99099:00000:09090:09990"
	MEH =  "09090:00000:00090:00900:09000"
	YES =  "00000:00009:00090:90900:09000"
	NO =  "90009:09090:00900:09090:90009"
	CLOCK12 =  "00900:00900:00900:00000:00000"
	CLOCK1 =  "00090:00090:00900:00000:00000"
	CLOCK2 =  "00000:00099:00900:00000:00000"
	CLOCK3 =  "00000:00000:00999:00000:00000"
	CLOCK4 =  "00000:00000:00900:00099:00000"
	CLOCK5 =  "00000:00000:00900:00090:00090"
	CLOCK6 =  "00000:00000:00900:00900:00900"
	CLOCK7 =  "00000:00000:00900:09000:09000"
	CLOCK8 =  "00000:00000:00900:99000:00000"
	CLOCK9 = "00000:00000:99900:00000:00000"
	CLOCK10 = "00000:99000:00900:00000:00000"
	CLOCK11 = "09000:09000:00900:00000:00000"
	ARROW_N = "00900:09990:90909:00900:00900"
	ARROW_NE = "00999:00099:00909:09000:90000"
	ARROW_E = "00900:00090:99999:00090:00900"
	ARROW_SE = "90000:09000:00909:00099:00999"
	ARROW_S = "00900:00900:90909:09990:00900"
	ARROW_SW = "00009:00090:90900:99000:99900"
	ARROW_W = "00900:09000:99999:09000:00900"
	ARROW_NW = "99900:99000:90900:00090:00009"
	GO_RIGHT = "09000:09900:09990:09900:09000"
	GO_LEFT = "00090:00990:09990:00990:00090"
	GO_UP = "00000:00900:09990:99999:00000"
	GO_DOWN = "00000:99999:09990:00900:00000"
	TRIANGLE = "00000:00900:09090:99999:00000"
	TRIANGLE_LEFT = "90000:99000:90900:90090:99999"
	CHESSBOARD =  "09090:90909:09090:90909:09090"
	DIAMOND =  "00900:09090:90009:09090:00900"
	DIAMOND_SMALL =  "00000:00900:09090:00900:00000"
	SQUARE =  "99999:90009:90009:90009:99999"
	SQUARE_SMALL =  "00000:09990:09090:09990:00000"
	RABBIT =  "90900:90900:99990:99090:99990"
	COW =  "90009:90009:99999:09990:00900"
	MUSIC_CROTCHET =  "00900:00900:00900:99900:99900"
	MUSIC_QUAVER =  "00900:00990:00909:99900:99900"
	MUSIC_QUAVERS =  "09999:09009:09009:99099:99099"
	PITCHFORK =  "90909:90909:99999:00900:00900"
	XMAS =  "00900:09990:00900:09990:99999"
	PACMAN =  "09999:99090:99900:99990:09999"
	TARGET =  "00900:09990:99099:09990:00900"
	TSHIRT =  "99099:99999:09990:09990:09990"
	ROLLERSKATE =  "00099:00099:99999:99999:09090"
	DUCK =  "09900:99900:09999:09990:00000"
	HOUSE =  "00900:09990:99999:09990:09090"
	TORTOISE =  "00000:09990:99999:09090:00000"
	BUTTERFLY =  "99099:99999:00900:99999:99099"
	STICKFIGURE =  "00900:99999:00900:09090:90009"
	GHOST =  "99999:90909:99999:99999:90909"
	SWORD =  "00900:00900:00900:09990:00900"
	GIRAFFE =  "99000:09000:09000:09990:09090"
	SKULL =  "09990:90909:99999:09990:09990"
	UMBRELLA =  "09990:99999:00900:90900:09900"
	SNAKE =  "99000:99099:09090:09990:00000"
	ALL_CLOCKS =  "00900:00900:00900:00000:00000"
	ALL_ARROWS =  "00900:09990:90909:00900:00900"
	
	def __init__(self, ) :
		if(self.ISDEBUG):print("Light Matrix is initialised in debug mode. Simulation change at spike.light_matrix.py ")

	def show_image(self,image, brightness=100):
		#w, h = 5, 5
		#imagematrixRAM = [[0 for x in range(w)] for y in range(h)]
		if(self.ISDEBUG):print("Shows an image on the Light Matrix.")
		imagematrix = "default"
		print("display cleard")

		
		if image == "HEART": imagematrix = self.HEART
		if image == "HEART_SMALL": imagematrix = self.HEART_SMALL
		if image == "HAPPY": imagematrix = self.HAPPY
		if image == "SMILE": imagematrix = self.SMILE
		if image == "SAD": imagematrix = self.SAD
		if image == "CONFUSED": imagematrix = self.CONFUSED
		if image == "ANGRY": imagematrix = self.ANGRY
		if image == "ASLEEP": imagematrix = self.ASLEEP
		if image == "SURPRISED": imagematrix = self.SURPRISED
		if image == "SILLY": imagematrix = self.SILLY
		if image == "FABULOUS": imagematrix = self.FABULOUS
		if image == "MEH": imagematrix = self.MEH
		if image == "YES": imagematrix = self.YES
		if image == "NO": imagematrix = self.NO
		if image == "CLOCK12": imagematrix = self.CLOCK12
		if image == "CLOCK1": imagematrix = self.CLOCK1
		if image == "CLOCK2": imagematrix = self.CLOCK2
		if image == "CLOCK3": imagematrix = self.CLOCK3
		if image == "CLOCK4": imagematrix = self.CLOCK4
		if image == "CLOCK5": imagematrix = self.CLOCK5
		if image == "CLOCK6": imagematrix = self.CLOCK6
		if image == "CLOCK7": imagematrix = self.CLOCK7
		if image == "CLOCK8": imagematrix = self.CLOCK8
		if image == "CLOCK9": imagematrix = self.CLOCK9
		if image == "CLOCK10": imagematrix = self.CLOCK10 
		if image == "CLOCK11": imagematrix = self.CLOCK11
		if image == "ARROW_N": imagematrix = self.ARROW_N
		if image == "ARROW_NE": imagematrix = self.ARROW_NE
		if image == "ARROW_E": imagematrix = self.ARROW_E
		if image == "ARROW_SE": imagematrix = self.ARROW_SE
		if image == "ARROW_S": imagematrix = self.ARROW_S
		if image == "ARROW_SW": imagematrix = self.ARROW_SW
		if image == "ARROW_W": imagematrix = self.ARROW_W
		if image == "ARROW_NW": imagematrix = self.ARROW_NW
		if image == "GO_RIGHT": imagematrix = self.GO_RIGHT
		if image == "GO_LEFT": imagematrix = self.GO_LEFT
		if image == "GO_UP": imagematrix = self.GO_UP
		if image == "GO_DOWN": imagematrix = self.GO_DOWN
		if image == "TRIANGLE": imagematrix = self.TRIANGLE
		if image == "TRIANGLE_LEFT": imagematrix = self.TRIANGLE_LEFT
		if image == "CHESSBOARD": imagematrix = self.CHESSBOARD
		if image == "DIAMOND": imagematrix = self.DIAMOND
		if image == "DIAMOND_SMALL": imagematrix = self.DIAMOND_SMALL
		if image == "SQUARE": imagematrix = self.SQUARE
		if image == "SQUARE_SMALL": imagematrix = self.SQUARE_SMALL
		if image == "RABBIT": imagematrix = self.RABBIT
		if image == "COW": imagematrix = self.COW
		if image == "MUSIC_CROTCHET": imagematrix = self.MUSIC_CROTCHET
		if image == "MUSIC_QUAVER": imagematrix = self.MUSIC_QUAVER
		if image == "MUSIC_QUAVERS": imagematrix = self.MUSIC_QUAVERS
		if image == "PITCHFORK": imagematrix = self.PITCHFORK
		if image == "XMAS": imagematrix = self.XMAS
		if image == "PACMAN": imagematrix = self.PACMAN
		if image == "TARGET": imagematrix = self.TARGET
		if image == "TSHIRT": imagematrix = self.TSHIRT
		if image == "ROLLERSKATE": imagematrix = self.ROLLERSKATE
		if image == "DUCK": imagematrix = self.DUCK
		if image == "HOUSE": imagematrix = self.HOUSE
		if image == "TORTOISE": imagematrix = self.TORTOISE
		if image == "BUTTERFLY": imagematrix = self.BUTTERFLY
		if image == "STICKFIGURE": imagematrix = self.STICKFIGURE
		if image == "GHOST": imagematrix = self.GHOST
		if image == "SWORD": imagematrix = self.SWORD
		if image == "GIRAFFE": imagematrix = self.GIRAFFE
		if image == "SKULL": imagematrix = self.SKULL
		if image == "UMBRELLA": imagematrix = self.UMBRELLA
		if image == "SNAKE": imagematrix = self.SNAKE
		if image == "ALL_CLOCKS": imagematrix = self.ALL_CLOCKS
		if image == "ALL_ARROWS": imagematrix = self.ALL_ARROWS
		#if image == "HAPPY": imagematrix = settings.FORCESENSORTYPE
		splitimagematrix = imagematrix.split(":")
		matrixrow = ""
		for y in range (5):
			for x in range (5):
				#if(self.ISDEBUG):print(splitimagematrix[y][x],"/",str(x),"/",str(y))
				if splitimagematrix[y][x]=="9":
					matrixrow = matrixrow +"X"
				else:
					matrixrow = matrixrow +"_"
			print (matrixrow)
			matrixrow = ""
					
		print("Simulated Image showed name: ", image," image matrix:",imagematrix)
		if(self.ISDEBUG):print("Image name: ", image," image matrix:",imagematrix)
	
	def off(self):
		if(self.ISDEBUG):print("Light Matrix turned off")
		print("Simulated display turned off")
	
	def set_pixel(self,x, y, brightness=100):
		if(self.ISDEBUG):print("Sets the brightness of one pixel (one of the 25 LEDs) on the Light Matrix. x:",str(x)," y:",str(y))
		print("Sets the brightness of one Simulated pixel (one of the 25 LEDs) on the Light Matrix.")
	   


