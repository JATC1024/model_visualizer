from .regression import logistic_regression

class model_prototype:
	_models = [logistic_regression()]

	@staticmethod
	def create_model(tag):
		for md in model_prototype._models:
			if md.recognize(tag):
				return md.clone()
		return None