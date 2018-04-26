class Engine:
	def __init__(self):
		self.throttlePercentage = 0
		self.active = False
		
	def getThrottle(self):
		return self.throttlePercentage
		
	def setThrottle(self, newThrottle):
		self.throttlePercentage = newThrottle
		
	def warmUp(self):
		self.active = True
	
	def shutdown(self):
		self.active = False
		
	def isActive(self):
		return self.active
	
		
