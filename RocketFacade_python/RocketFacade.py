import sys
import time
import errno
import logging

from Engine import Engine
from FuelTank import FuelTank
from InternalComputer import InternalComputer
from NoseCone import NoseCone


class RocketFacade:
	
	def __init__(self):
		self.engine = Engine()
		self.fueltank = FuelTank()
		self.computer = InternalComputer()
		self.nosecone = NoseCone()
		
	def test(self):
		successful = True
		self.computer.communicate("Aircraft testing has begun.")
		# Test Computer
		if not self.computer.monitorAstronautsVitals() and not self.computer.getAltitude() == 0 and not self.computer.getLaunchTimer() == 0.0:
			self.computer.communicate("An issue with the onboard computer was detected. Check the astronaut vitals.")
			successful = False
		else:
			self.computer.communicate("Computer Testing Passed")
			
		# Test FuelTank
		if not self.fueltank.getFuelLevel() == 0:
			self.computer.communicate("A malfunction on the fuel tank was detected.")
			successful = False
		else:
			self.computer.communicate("Fuel Tank Testing Passed")
			
		# Test Engine
		if not self.engine.getThrottle() == 0 and not self.engine.isActive():
			self.computer.communicate("A malfunction with the engine was detected. Check its status.")
			successful = False
		else:
			self.computer.communicate("Engine Testing Passed")
        
        # Test NoseCone
		if self.nosecone.isAntennaDeployed() or self.nosecone.isChuteDeployed():
			self.computer.communicate("Error with Nose Cone. Check if Antenna or Chute are deployed.")
			successful = False
		else:
			self.computer.communicate("Nose Cone Testing Passed")
        
		return successful
		
	def fuelUp(self):
		self.fueltank.setFuelLevel(100.0)
		
	def countdownStart(self):
		timeUntilLaunch = 10
		self.computer.communicate("Countdown sequence initiated")
		while (timeUntilLaunch > 0):
			time.sleep(1)
			
			self.computer.setLaunchTimer(timeUntilLaunch)
			if timeUntilLaunch >= 4:
				if timeUntilLaunch % 10 == 0:
					print "Launch in " + str(timeUntilLaunch) + "seconds..."
				else:
					timeUntilLaunch = timeUntilLaunch - 1
					timeUntilLaunch = timeUntilLaunch + 1
			else:
				print "Launch in " + str(timeUntilLaunch) + "seconds..."
			timeUntilLaunch = timeUntilLaunch - 1
		self.computer.communicate("Launch sequence initiated")
		self.launch()
	
	def launch(self):
		print "        |"
		print "       / \\" 
		print "      / _ \\"
		print "     |.o '.|"
		print "     |'._.'|"
		print "     |     |"
		print "   ,'|  |  |`."
		print "  /  |  |  |  \\"
		print "  |,-'--|--'-.|" 
		try:
			time.sleep(.5)
		except IOError, e:
			if e.errno != errno.EINTR:
				Logger.getLogger(RocketFacade)
				logging.critical
				raise
		print "      |   |      "
		try:
			time.sleep(.5)
		except IOError, e:
			if e.errno != errno.EINTR:
				Logger.getLogger(RocketFacade)
				logging.critical
				raise
		print "     /     \\      "
		try:
			time.sleep(.5)
		except IOError, e:
			if e.errno != errno.EINTR:
				Logger.getLogger(RocketFacade)
				logging.critical
				raise
		print "    / /   \\ \\      "
		try:
			time.sleep(.5)
		except IOError, e:
			if e.errno != errno.EINTR:
				Logger.getLogger(RocketFacade)
				logging.critical
				raise
		print "    | |   | |    "
		try:
			time.sleep(.5)
		except IOError, e:
			if e.errno != errno.EINTR:
				Logger.getLogger(RocketFacade)
				logging.critical
				raise
		print "     \\ \\ / /     "
		try:
			time.sleep(.5)
		except IOError, e:
			if e.errno != errno.EINTR:
				Logger.getLogger(RocketFacade)
				logging.critical
				raise
		print "       \\ /     "
		try:
			time.sleep(.5)
		except IOError, e:
			if e.errno != errno.EINTR:
				Logger.getLogger(RocketFacade)
				logging.critical
				raise
		print "                      "
		try:
			time.sleep(.5)
		except IOError, e:
			if e.errno != errno.EINTR:
				Logger.getLogger(RocketFacade)
				logging.critical
				raise
		print "                      "
		try:
			time.sleep(.5)
		except IOError, e:
			if e.errno != errno.EINTR:
				Logger.getLogger(RocketFacade)
				logging.critical
				raise
		print "                      "
		
		print "Aircraft Launch Successful"
	
	def abort(self):
		self.computer.communicate("An error has been detected and the abort sequence will initialize")
		self.computer.setLaunchTimer(0)
		self.engine.shutdown()
		alt1 = self.computer.getAltitude()
		try:
			time.sleep(1)
		except IOError, e:
			if e.errno != errno.EINTR:
				Logger.getLogger(RocketFacade)
				logging.critical
				raise
		alt2 = self.computer.getAltitude()
		if alt1-alt2 < 0:
			self.nosecone.deployParachute()
		self.computer.communicate("Aborting mission")
		self.nosenone.retractAntenna()
		
def main():
	rocket = RocketFacade()
	if rocket.test():
		rocket.countdownStart()
	else:
		rocket.abort()

main()
	
	
