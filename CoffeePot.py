class CoffeePot:
	MODE_OFF = 0
	MODE_ON =1
	MODE_BREW = 2
	
	def reset(self):
		self_mode = CoffeePot.MODE_BREW
		self._brewStates = [ False for i in range(self._brew)]
	
	def __init__(self, brew):
		self.brewOk(brew)
		self._brew = brew
		self.reset()
			
	def getBrew(self):
		return self._brew
		
	def brewOk(self, brew):
		if not isinstance(brew, int):
			raise ValueError("brew must be an integer")
		if not brew == 2:
			raise ValueError("brew must be value 2 to brew")
			
	def brewingOk(self, brew):
		if not isinstance(brew, int):
			raise ValueError("brew must be an integer")
		if brew < 0 or self._brew <= brew:
			raise ValueError("brew (" + str(brew) + ") must be between 0 and " + str(self._brew-1) + ".")
			
	def brewStateOk(self, state):
		if not isinstance(state, bool):
			raise ValueError("brew and steam state must be an integer")
	
	def modeOk(self, mode):
		if not isinstance(mode, int):
			raise ValueError("mode must be an integer")
		if mode != CoffeePot.MODE_OFF and mode != CoffeePot.MODE_ON and mode != CoffeePot.MODE_BREW:
			raise ValueError("mode must be MODE_OFF, MODE_ON, or MODE_BREW")
			
	def setMode(self, mode):
		self.modeOk(mode)
		self._mode = mode
		
	def getMode(self):
		return self._mode

	def setBrewState(self, brew, state):
		self.brewingOk(brew)
		self.brewStateOk(state)
		self._brewStates[brew] = state
		
	def getBrewState(self, brew):
		self.brewingOk(brew)
		if self._mode == CoffeePot.MODE_OFF: return False
		if self._mode == CoffeePot.MODE_BREW: return True
		return self._brewStates[brew]
		
	def getbrewStates(self):
		return [ self.getBrewState(brew) for brew in range(self._brew)]
