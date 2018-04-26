import time

class InternalComputer:
	def __init__(self):
		self.launchTimer = 0
		self.altitude = 0;
		self.astronautsAlive = True
		
	def monitorAstronautsVitals(self):
		return self.astronautsAlive
		
	def communicate(self, message):
		localtime = time.asctime( time.localtime(time.time()) )
		print localtime, ": ", message
		
	def getAltitude(self):
		return self.altitude
		
	def setAltitude(self, newAltitude):
		self.altitude = newAltitude
		
	def getLaunchTimer(self):
		return self.launchTimer
		
	def setLaunchTimer(self, newTime):
		self.launchTimer = newTime
