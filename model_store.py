# Store a list of model
# Have method:
#	- Select model
#	- Control selected model

from models import support_vector_machine, logistic_regression

class model_store:

	def __init__(self):
		self.current = None
		self.data = []
		lr = logistic_regression()
		svm = support_vector_machine()
		self.model_list = [lr, svm]

	def reset(self):
		self.current.reset()
		self.data = []

	def recognize(self, tag):
		for model in self.model_list:
			if model.recognize(tag):
				self.current = model
				self.reset()
				return True
		return False

	def add_one_data(self, element):
		self.data.append(element)

	def add_data(self, array)
		self.data = array

	def feed_data(self):
		self.current.feed_data(data)

	def get_argument(self):
		return self.current.get_argument()

	def set_argument(self, array):
		self.current.set_argument(array)


