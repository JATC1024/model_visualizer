# A common preset
# Other particular presets will inheritaged from this class
import numpy

class root_preset:
	
	def __init__(self):
		self.name = 'Root Preset'
		self.noise = 0.1
		self.data = []
		self.size = 100
		self.rang = (-1, 1)

	def be_noise(self)
		return numpy.random.uniform(0,1) <= self.noise

	def recognize(self, tag):
		pass
	
	def classify(self, x1, x2):
		pass

	def resample(self):
		for i in range(0, self.size):
			x1 = numpy.random.uniform(self.rang[0], self.rang[1])
			x2 = numpy.random.uniform(self.rang[0], self.rang[1])
			y = self.classify(x1, x2)
			if self.be_noise():
				y = 1 - y
			self.data.append((x1,x2,y))

	def get_data(self):
		return self.data
