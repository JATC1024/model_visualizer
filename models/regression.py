# Logicstic Regression model
from .root_model import *
from .Optimizer import *
import numpy as np
import copy

class logistic_regression(root_model):
	_configs = "model_configs/logistic_configs.json"
	def __init__(self):
		""" Default constructor.
		Creates dummy attributes for the class """
		super().__init__()
		self.weights = None
		self.graph = Graph()
		self.loss = None
		self.infer = None
		self.initialize(logistic_regression._configs)

	def initialize(self, configs):
		""" Initializes the model with a given config file """
		super().initialize(configs)
		self.weights = np.random.uniform(-1, 1, 3)
		self.getgraph()

	def get_config_file_name(self):
		return logistic_regression._configs

	def clone(self):
		return logistic_regression()

	def getgraph(self):
		self.graph.as_default()
		w = Variables(to_matrix(self.weights))
		X = Placeholder('X')
		y_predict = Sigmoid(Matmul(X, w))
		self.infer = y_predict

		one = Placeholder("one")
		y_truth = Placeholder('y')
		first = Matmul(Transpose(y_truth), Log(y_predict))
		b = Add(one, Negative(y_truth))
		c = Add(one, Negative(y_predict))
		second = Matmul(Transpose(b), Log(c))
		J = Negative(Add(first, second))
		self.loss = J
		self.minimizer = GradientDescentOptimizer(learning_rate = 0.01).minimize(self.loss)

	def inference(self, X = None):
		sess = Session()
		if X is None:
			X = self._X
		X = np.hstack((X, np.ones((len(X), 1))))
		return sess.run(self.infer, feed_dict = {'X' : X})

	def next_step(self):
		X = np.hstack((self._X, np.array([[1] * len(self._X)]).T))
		sess = Session()
		one = np.ones((len(self._y), 1))
		feed = {'X' : X, 'one' : one, 'y' : to_matrix(self._y)}
		sess.run(self.loss, feed)
		sess.run(self.minimizer, feed)

def to_matrix(A):
	if A.ndim == 1:
		return A[:,np.newaxis]