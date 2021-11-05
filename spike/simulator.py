import random,time,math

class Simulator:
	def remap(self,x, in_min, in_max, out_min, out_max):
		return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
	  
	def get_new_value(self,
					  issimulation=True,
					  simulationtype="Random",
					  isdebug=True, actualvalue=0,
					  newreading=-1,
					  minvalue = 0,
					  maxvalue = 100,
					  name ="color sensor ambient light",
					  direction = True,
					  change = 1,
					  iswait= False,
					  switch_min = 0,
					  switch_max=80,
					  isextern=False,
					  time_period= 1,
					  minreading=0,
					  maxreading=200):
		if(issimulation or newreading==-1):
			if(simulationtype == "Random"):
				actualvalue = int(self.remap(random.getrandbits(8), 0, 255, minvalue, maxvalue))
				if(isdebug):print(str(name)," simulated random number:", str(actualvalue) )
				if(iswait):
					runwhile = True
					while runwhile:
						if isextern:
							if actualvalue > switch_max or actualvalue < switch_min:
								runwhile = False
							else:
								actualvalue = int(self.remap(random.getrandbits(8), 0, 255, minvalue, maxvalue)) 
								if(isdebug):print(str(name)," simulated random number:", str(actualvalue), " to exit it should be lower then:", switch_min , " or it should be higher then:", switch_max )
						else:
							if actualvalue <= switch_max and actualvalue >= switch_min:
								runwhile = False
							else:
								actualvalue = int(self.remap(random.getrandbits(8), 0, 255, minvalue, maxvalue))
								if(isdebug):print(str(name)," simulated random number:", str(actualvalue), " to exit it should be higher or equal then:", switch_min , " or it should be lower or equal then:", switch_max )
						time.sleep(1)
			   
			elif(simulationtype == "Circular"):
				if(iswait):
					self.time = time.time()
					while time.time() - self.time < time_period:
						if(isdebug):print("Time remaining until simulated ",str(name)," event occurs in sec: ", str(int(math.ceil( time_period - (time.time() - self.time)))))
						time.sleep(1)
					actualvalue = switch_max +1 
				else:
					if(direction):
						actualvalue += change
						if(actualvalue >= maxvalue):
							direction = False
					else:
						actualvalue -= change
						if(actualvalue <= minvalue):
							direction = True
					if(isdebug):print("Simulated Circular ",str(name)," value:", actualvalue)
					time.sleep(1)
			elif(simulationtype == "Consol"):
				if(iswait):
					while input("press 'p' to simulate a "+ str(name)+" event :") != "p":
						pass
					actualvalue = switch_max +1 
				else:
					actualvalue = int(input("new reading in "+str(name)+" ("+str(minvalue)+"..."+str(maxvalue)+"): "))
					if actualvalue>=maxvalue :
						actualvalue = maxvalue
					if actualvalue<=minvalue :
						actualvalue = minvalue
					if(isdebug):print("Simulated ",str(name)," value from console:", actualvalue)
		else:
			actualvalue = newreading
			if(isdebug):print("actualvalue ",str(actualvalue)," minreading: "+str(minreading)," maxreading: "+str(maxreading)," minvalue: "+str(minvalue)," maxvalue: "+str(maxvalue))
			actualvalue = int(self.remap(actualvalue, minreading, maxreading, minvalue, maxvalue))

		return int(actualvalue), direction
