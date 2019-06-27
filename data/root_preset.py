# A common preset
# Other particular presets will inheritaged from this class
import numpy, os, json

class root_preset:
	
	def __init__(self):
		data = root_preset.json_data(self)
		self.name = data['name']
		self.noise = data['noise']
		self.data = []
		self.size = data['size']
		self.rang = data['rang']
	
	def json_data(self):
		dir = os.path.join(os.path.dirname(__file__), 'data_configs/root.json')
		with open(dir) as f:
			return json.load(f)

	def be_noise(self):
		return numpy.random.uniform(0,1) <= self.noise

	def recognize(self, tag):
		data = self.json_data()
		return tag in data['tag']
	
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
