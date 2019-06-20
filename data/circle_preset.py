from root_preset import root_preset

class circle_preset(root_preset):

	def __init__(self):
		root_preset.__init__()
		data = self.json_data()
		self.name = data['name']
		self.radius = data['radius']
	
	def json_data(self):
		dir = os.path.join(os.path.dirname(__file__), 'data_configs/circle.json')
		with open(dir) as f:
			return json.load(f)

	def classify(self, x1, x2):
		if x1**2 + x2**2 <= self.radius**2:
			return 1
		return 0
		
