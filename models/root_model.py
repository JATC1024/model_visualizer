# A virtual model
# All other particular models inheritage from this root_model
import os
import json

class root_model:

	def __init__(self):
		self.name = 'Root Model'

	def initialize(self, config):
		dir = os.path.join(os.path.dirname(__file__), config)
		with open(dir) as f:
			data = json.load(f)
			return data["name"], data['params']

	# User choose a tag
	def recognize(self, tag):
		pass

	# Return true if not converge
	def next_step(self):
		pass

	# Cancel and delete all train data (if any)
	# Reset all the argument with default value
	def reset(self):
		pass


	# Return array of arguments needed for model to train
	# Each argument is a pair of 'name' and 'type'
	def get_arguments(self):
		pass

	# Set value of arguments needed for model to train
	# Each element of array is a value
	def set_arguments(self, array):
		pass

	# Set the train data
	# Each element of array is (x1, x2, y)
	def feed_data(self, array):
		pass
