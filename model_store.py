# Store a list of model
# Have method:
#	- Select model
#	- Control selected model

from regression import logicstic_regression
from svm import support_vector_machine

class model_store:
	
	def __init__(self):
		self.current = None
		lr = logicstic_regression()
		svm = support_vector_machine()
		self.model_list = [lr, svm]

	def recognize(self, tag):
		for model in self.model_list:
			if model.recognize(tag):
				self.current = model
				return True
		return False
		


