import unittest
from CoffeePot import CoffeePot

class TestCoffeePot(unittest.TestCase):
	def _testInit(self, unit):
		self.assertEqual(unit.getMode(), CoffeePot.MODE_BREW)
		for brew in range(unit.getBrew()):
			self.assertEqual(unit.getBrewState(brew), False,
							"brew " + str(brew) + " should be off")
		
	def _testModes(self, unit):
		unit.setMode(CoffeePot.MODE_BREW)
		for brew in range(unit.getBrew()):
			unit.setBrewState(brew, False)
			self.assertEqual(unit.getBrewState(brew), True)
			unit.setBrewState(brew, True)
			self.assertEqual(unit.getBrewState(brew), True)
			
		unit.setMode(CoffeePot.MODE_OFF)
		for brew in range(unit.getBrew()):
			unit.setBrewState(brew, False)
			self.assertEqual(unit.getBrewState(brew), False)
			unit.setBrewState(brew, True)
			self.assertEqual(unit.getBrewState(brew), False)
		
	def _testModesInvalid(self, unit):
		for mode in ("brew", "off"):
			ok = False
			try:
				unit.setMode(mode)
			except ValueError:
				ok = True
			self.assertTrue(ok)
		
	def _testBrew(self, unit):
		for state in (False, True):
			unit.setBrewState(brew, state)
			unit.setMode(CoffeePot.MODE_OFF)
			self.assertEqual(unit.getBrewState(brew), False, 
							"brew " + str(brew) + "in off mode should be False.")
			unit.setMode(CoffeePot.MODE_BREW)
			self.assertEqual(unit.getBrewState(brew), True,
							"brew" + str(brew) + " in brew mode should be True.")
							
	def _testBrewInvalid(self, unit, brew):
		for state in (0.5, "off", "on"):
			ok = False
			try:
				unit.setBrewState(brew, state)
			except ValueError:
				ok = True
			self.assertTrue(ok, "brew" + str(brew) + " should fail to set value " + str(state))
			
	def _testBrewing(self, unit):
		for brew in range(unit.getBrew()):
			self._testBrew(unit, brew)
			self._testBrewInvalid(unit, brew)
		
	def testConstructCoffeePot(self):
		unit = CoffeePot(2)
		self._testInit(unit)
		
	def testConstructCoffeePotInvalid(self):
		ok = False
		try:
			unit = CoffeePot(-2)
		except ValueError:
			ok = True
		self.assertTrue(ok)
		
	def testModesCoffeePot(self):
		unit = CoffeePot(2)
		self._testModes(unit)
		
	def testModesInvalidCoffeePot(self):
		unit = CoffeePot(2)
		self._testModesInvalid(unit)
		
	def testBrewCoffeePot(self):
		unit = CoffeePot(2)
		self._testBrewing(unit)
		
if __name__ == '__main__':
	unittest.main()
		
