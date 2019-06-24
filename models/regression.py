# Logicstic Regression model
from .root_model import *
import numpy as np
import copy

class logistic_regression(root_model):
	_configs = "model_configs/logistic_configs.json"
	def __init__(self):
		""" Default constructor.
		Creates dummy attributes for the class """
		super().__init__()
		self.weights = None
		self._initialize(logistic_regression._configs)

	def _initialize(self, configs):
		""" Initializes the model with a given config file """
		super()._initialize(configs)
		self.weights = np.random.uniform(-1, 1, 3)
		self._build_graph()

	def _get_config_file_name(self):
		return logistic_regression._configs

	def clone(self):
		return logistic_regression()

	def _build_graph(self):
		self._graph.as_default()
		W = Variables(self.weights)
		X = Placeholder('X')
		y = Sigmoid(Dot(W, X))
		self.infer_node = y

	def inference(self, X):
		sess = Session()
		X = copy.deepcopy(X)
		X.append(1)
		return sess.run(self.infer_node, feed_dict = {'X' : X})