# Sample data based on chosen preset
from data.linear_preset import linear_preset
from data.circle_preset import circle_preset
from data.cross_preset import cross_preset
from data.none_preset import none_preset

class data_sample:
	
	def __init__(self):
		self.current = None
		self.preset_list = [none_preset(), linear_preset(), cross_preset(), circle_preset()]

	def list(self):
		res = []
		for preset in self.preset_list:
			res.append(preset.name)
		return res

	def recognize(self, tag):
		for preset in preset_list:
			if (preset.recognize(tag)):
				self.current = preset
				self.resample()
				return True
		return False

	def resample(self):
		self.current.resample()

	def get_data(self):
		return self.current.get_data()
