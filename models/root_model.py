# A virtual model
# All other particular models inheritage from this root_model
import os
import json
import numpy as np
from.computational_graph import Graph
from .Operation import *
from .Variables import *
from .Placeholder import *
from .Session import *

class root_model:
	def __init__(self):
		""" Default constructor
		Creates dummy attributes for the class """
		self.name = 'Root Model'
		self.params = None
		self.data = None


	def initialize(self, configs):
		""" Initializes a model with a set of hyperparameters.
		The set of hyperparameters is given in the configs file """
		dir = os.path.join(os.path.dirname(__file__), configs)
		with open(dir) as f:
			data = json.load(f)
			self.name = data["name"]
			self.params = data['params']

	def recognize(self, tag):
		""" Checks wheter the self model is associated with the given tag """
		config = self.load_config_file()
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
		config = self.get_config_file_name()
		self.initialize(self, config)
		self.data = None


	def get_config_file_name(self):
		""" Gets the name of the config file associatied with the model.
		Implementation is passed to child classes """
		raise Exception("Not implemented")

	def get_arguments(self):
		""" Returns an array of arguments needed for model to train.
		Each argument is a pair of 'name' and 'type' """
		config = self.load_config_file()
		params = config['params']
		# return [(key, params[key]['type']) for key in params]
		return params

	def set_arguments(self, params):
		""" Sets value of arguments needed for model to train.
		Each element of array is a value """
		if self.check_validparams(params):
			for p in params:
				self.params[p] = params[p]
		else:
			print(params)
			raise Exception("An argument is not recoginized")

	def feed_data(self, array):
		data = np.array(array)
		self._X = data[0:len(data),0:-1]
		self._y = np.array(data[0:len(data),-1])
		self._y.reshape((len(self._y), 1))

	def check_validparams(self, params):
		""" Checks if the given params are valid for the model. """
		config = self.load_config_file()
		defaultparams = config["params"]
		for p in params:
			if not(p in defaultparams):
				return False
		return True

	def load_config_file(self):
		""" Loads the config file of the model """
		dir = os.path.join(os.path.dirname(__file__), \
				self.get_config_file_name())
		with open(dir) as f:
			data = json.load(f)
			return data

	def clone(self):
		""" Creates a new instance of the model.
		Abstract  """
		raise Exception("Not implemented")

	def inference(self, x):
		""" Calculates the value estimated for a datapoint.
		Implementation is passed to children classes """
		raise Exception("Not implemented")