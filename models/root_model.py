# A virtual model
# All other particular models inheritage from this root_model
import os
import json
import numpy as np

class root_model:
	def __init__(self):
		""" Default constructor
		Creates dummy attributes for the class """
		self._name = 'Root Model'
		self._params = None
		self._data = None


	def _initialize(self, configs):
		""" Initializes a model with a set of hyperparameters.
		The set of hyperparameters is given in the configs file """
		dir = os.path.join(os.path.dirname(__file__), configs)
		with open(dir) as f:
			data = json.load(f)
			self._name = data["name"]
			self._params = data['params']

	def recognize(self, tag):
		""" Checks wheter the self model is associated with the given tag """
		config = self._load_config_file()
		tags = config['tags']
		if tag in tags:
			return True
		else:
			return False

	def next_step(self):
		""" Performs an optimization step.
		Return True if the step is performed (not converged), False otherwise.
		Implementation is passed to child classes """
		raise Exception("Not implemented")

	def reset(self):
		""" Cancels and deletes all train data (if any)
		Resets all the hyperparameters with default value """
		config = self._get_config_file_name()
		self._initialize(self, config)
		self.data = None


	def _get_config_file_name(self):
		""" Gets the name of the config file associatied with the model.
		Implementation is passed to child classes """
		raise Exception("Not implemented")

	def get_arguments(self):
		""" Returns an array of arguments needed for model to train.
		Each argument is a pair of 'name' and 'type' """
		config = self._load_config_file()
		params = config['params']
		return [(key, params[key]['type']) for key in params]

	def set_arguments(self, params):
		""" Sets value of arguments needed for model to train.
		Each element of array is a value """
		if _check_valid_params(params):
			for p in params:
				self._params[p] = params[p]
		else:
			raise Exception("An argument is not recoginized")

	def feed_data(self, array):
		""" Set the train data.
		Each element of array is (x1, x2, y) """
		self._data = np.array(array)

	def print(self):
		print(self._name)
		print(self._params)
		print(self.weights)

	def _check_valid_params(self, params):
		""" Checks if the given params are valid for the model. """
		config = self._load_config_file()
		default_params = config[params]
		for p in params:
			if not(p in default_params):
				return False
		return True

	def _load_config_file(self):
		""" Loads the config file of the model """
		dir = os.path.join(os.path.dirname(__file__), \
				self._get_config_file_name())
		with open(dir) as f:
			data = json.load(f)
			return data

	def clone(self):
		""" Creates a new instance of the model.
		Abstract  """
		raise Exception("Not implemented")