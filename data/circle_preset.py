from root_preset import root_preset

class circle_preset(root_preset):

	def __init__(self):
		root_preset.__init__()
		self.name = 'Circle preset'
		self.radius = 0.5
	
	def recognize(self, tag):
		return (tag == 'Circle') or (tag == self.name)

	def classify(self, x1, x2):
		if x1**2 + x2**2 <= self.radius**2:
			return 1
		return 0
		
