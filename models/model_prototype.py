from .regression import logistic_regression

class model_prototype:
	def __init__(self):
		self.models = [logistic_regression()]
	
	def recognize(self, tag):
		for md in self.models:
			if md.recognize(tag):
				return md.clone()
		return None
	
	def list(self):
		return [md.name for md in self.models]