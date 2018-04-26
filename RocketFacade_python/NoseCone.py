class NoseCone:
	def __init__(self):
		self.chuteDeployed = False
		self.antennaDeployed = False
		
	def deployParachute(self):
		self.chuteDeployed = True
		
	def retractParachute(self):
		self.chuteDeployed = False
		
	def deployAntenna(self):
		self.antennaDeployed = True
		
	def retractAntenna(self):
		self.antennaDeployed = False
		
	def isChuteDeployed(self):
		return self.chuteDeployed
		
	def isAntennaDeployed(self):
		return self.antennaDeployed
