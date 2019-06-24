# Support vector machine model
from .root_model import root_model
import json
import os
import numpy as np

class support_vector_machine(root_model):
	_configs = "model_configs/svm_configs.json"

	def __init__(self):
		""" Default constructor.
		Creates dummy attributes for the class """
		super(support_vector_machine, self).__init__()
		self.weights = None
		self._initialize(support_vector_machine._configs)

	def _initialize(self, configs):
		""" Initializes the model with a given config file """
		super(support_vector_machine, self)._initialize(configs)
		self.weights = np.random.uniform(-1, 1, 3)

	def _get_config_file_name(self):
		return support_vector_machine._configs

	def clone(self):
		return support_vector_machine()
