# Linear preset

from root_preset import root_preset

class linear_preset(root_preset):
	
	def __init__(self):
		root_preset.__init__()
		self.name = 'Linear preset'
		self.angle = 1
	
	def recognize(self, tag):
		return (tag == 'Linear') or (tag == self.name)

	def classify(self, x1, x2):
		if x1 * self.angle + x2 >= 0:
			return 1
		return 0
