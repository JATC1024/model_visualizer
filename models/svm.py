# Support vector machine model
from .root_model import root_model

class support_vector_machine(root_model):

	def __init__(self):
		self.name = 'Support Vector Machine'

	def recognize(self, tag):
		return (tag == 'SVM') or (tag == self.name)
