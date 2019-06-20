# Cross preset

from root_preset import root_preset

class cross_preset(root_preset):
	
	def __init__(self):
		root_preset.__init__()
		data = self.json_data()
		self.name = data['name']
	
	def json_data(self):
		dir = os.path.join(os.path.dirname(__file__), 'data_configs/cross.json')
		with open(dir) as f:
			return json.load(f)

	def classify(self, x1, x2):
		if x1 * x2 >= 0:
			return 1
		return 0
