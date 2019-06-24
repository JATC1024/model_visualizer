import numpy as np
from .computational_graph import Graph

class Operation:
	""" A node in the computational graph
	Takes some objects as input, performs computation and produces some objects as output."""
	def __init__(self, input_nodes = []):
		self.consumers = []
		self.input_nodes = input_nodes

		for node in input_nodes:
			node.consumers.append(self)

		Graph._default_graph.operations.append(self)

	def compute(self):
		""" Computes the output of the operation, given the inputs
		Implementation is passed to the children classes """
		raise Exception("Not implemented")


class Add(Operation):
	""" Computes x + y element wise """
	def __init__(self, x, y):
		""" Constructs add operator """
		super().__init__([x, y])

	def compute(self, x, y):
		""" Computes the output """
		return x + y

class Sigmoid(Operation):
	""" Represents the sigmoid function """
	def __init__(self, x):
		super().__init__([x])

	def compute(self, val):
		return 1.0 / (1.0 + np.exp(-val))

class Dot(Operation):
	def __init__(self, x, y):
		super().__init__([x, y])

	def compute(self, x, y):
		return np.sum(x * y)