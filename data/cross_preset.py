# Cross preset

from root_preset import root_preset

class cross_preset(root_preset):
	
	def __init__(self):
		root_preset.__init__()
		self.name = 'Cross preset'
	
	def recognize(self, tag):
		return (tag == 'Cross') or (tag == self.name)

	def classify(self, x1, x2):
		if x1 * x2 >= 0:
			return 1
		return 0
