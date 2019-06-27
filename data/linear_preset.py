# Linear preset

from data.root_preset import root_preset
import os, json

class linear_preset(root_preset):
	
	def __init__(self):
		root_preset.__init__(self)
		data = self.json_data()
		self.name = data['name']
		self.angle = data['angle']

	def json_data(self):
		dir = os.path.join(os.path.dirname(__file__), 'data_configs/linear.json')
		with open(dir) as f:
			return json.load(f)

	def classify(self, x1, x2):
		if x1 * self.angle + x2 >= 0:
			return 1
		return 0
