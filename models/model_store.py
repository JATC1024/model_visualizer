# Store a list of model
# Have method:
#	- Select model
#	- Control selected model

from .regression import logicstic_regression
from .svm import support_vector_machine

class model_store:
	current = None
	lr = logicstic_regression()
	svm = support_vector_machine()
	model_list = [lr, svm]

	def recognize(tag):
		for model in model_store.model_list:
			if model.recognize(tag):
				current = model
				return True
		return False



