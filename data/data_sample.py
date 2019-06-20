# Sample data based on chosen preset
from linear_preset import linear_preset
from circle_preset import circle_preset
from cross_reset import cross_preset

class data_sample:
	
	def __init__(self):
		self.current = None
		self.preset_list = [linear_preset(), cross_preset(), circle_preset()]

	def recognize(self, tag)
		for preset in preset_list:
			if (preset.recognize(tag))
				self.current = preset
				self.resample()
				return True
		return False

	def resample(self)
		self.current.resample()

	def get_data(self)
		return self.current.get_data()
