# Sample data based on chosen preset

class data_sample:
	
	def __init__(self):
		self.current = None
		self.preset_list = []
		# TODO add preset list 

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
