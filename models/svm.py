# Support vector machine model
from .root_model import root_model
import json
import os

class support_vector_machine(root_model):

	def __init__(self):
		super(support_vector_machine, self).__init__()
		self.configs = "model_configs/svm_configs.json"
		self.name, self.params = self.initialize(self.configs)

	def recognize(self, tag):
		dir = os.path.join(os.path.dirname(__file__), self.configs)
		with open(dir) as f:
			data = json.load(f)
			if tag in data['tags']:
				return True
			else:
				return False


	def get_arguments(self):
		dir = os.path.join(os.path.dirname(__file__), self.configs)
		with open(dir) as f:
			data = json.load(f)
			params = data['params']
			print("haha")
			return [(key, params[key]["type"]) for key in params]

	def set_arguments(self, dict):
		self.params = dict

	def reset(self):
		self.params = self.initialize(self.configs)
