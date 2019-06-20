# Store a list of model
# Have method:
#	- Select model
#	- Control selected model

from .models.regression import logicstic_regression
from .models.svm import support_vector_machine

class model_store:

	def __init__(self):
		self.current = None
		self.data = []
		lr = logicstic_regression()
		svm = support_vector_machine()
		self.model_list = [lr, svm]

	def reset(self):
		self.current.reset()
		self.data = []

	def recognize(tag):
		for model in self.model_list:
			if model.recognize(tag):
				self.current = model
				self.reset()
				return True
		return False

	def add_one_data(self, element):
		self.data.append(element)

	def feed_data(self):
		self.current.feed_data(data)

	def get_argument(self):
		return self.current.get_argument()

	def set_argument(self, array):
		self.current.set_argument(array)


