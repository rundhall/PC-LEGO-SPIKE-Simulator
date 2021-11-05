import time

class wait_for_seconds:
	
	def __init__(self,second):
		time.sleep(second)
	  
class Timer:
	
	def __init__(self):
		self.start = time.time()
	
	def now(self):
		dif = time.time()- self.start
		print("time.now", dif) 
		return dif
