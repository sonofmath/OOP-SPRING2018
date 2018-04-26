class FuelTank:
	def __init__(self):
		self.fuelLevel = 0
		self.fuelType = "none"
		
	def getFuelLevel(self):
		return self.fuelLevel
		
	def setFuelLevel(self, newFuelLevel):
		if newFuelLevel >= 100.0:
			self.fuelLevel = 100.0
		else:
			self.fuelLevel = newFuelLevel
