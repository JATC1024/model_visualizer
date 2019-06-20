# Support vector machine model
from .root_model import root_model
import json
import os

class support_vector_machine(root_model):

	def __init__(self):
		self.name = 'Support Vector Machine'

	def recognize(self, tag):
		dir = os.path.join(os.path.dirname(__file__),
				"model_parameters/svm_params.json")
		with open(dir) as f:
			data = json.load(f)
			if tag in data['names']:
				return True
			else:
				return False


	def get_arguments(self):
		dir = os.path.join(os.path.dirname(__file__),
				"model_parameters/svm_params.json")
		with open(dir) as f:
			data = json.load(f)
			return data['params']