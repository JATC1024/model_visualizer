# None preset

from data.root_preset import root_preset
import os, json

class none_preset(root_preset):
	
	def __init__(self):
		root_preset.__init__(self)
		data = self.json_data()
		self.name = data['name']

	def json_data(self):
		dir = os.path.join(os.path.dirname(__file__), 'data_configs/none.json')
		with open(dir) as f:
			return json.load(f)

	def resample(self):
		self.data = []
