# A common preset
# Other particular presets will inheritaged from this class

class root_preset:
	
	def __init__(self):
		self.name = 'Root Preset'

	def recognize(self, tag):
		pass

	def resample(self):
		pass

	def get_data(self):
		pass
