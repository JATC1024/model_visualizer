# A fake model_manager
# Used to test ui.py

class model_manager:
	def __init__(self):
		pass
	def list(self):
		return ['Linear Regression', 'Support Vector Machine']
	def recognize(self, tag):
		if (tag == 'Linear Regression'):
			self.current = tag
			return True
		elif tag == 'Support Vector Machine':
			self.current = tag
			return True
		return False
	def name(self):
		return self.current
	def get_arguments(self):
		return { "Learning rate": { "type": "float", "default" : 0.001 } , "Activation function" : { "type": "string", "option": ["Sigmoid", "Tanh"] , "default": "Sigmoid"} }
	def set_arguments(self, args):
		pass

	def feed_data(self, data):
		pass
	
	def reset(self):
		pass
