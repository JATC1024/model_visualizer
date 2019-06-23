import numpy as np


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

class Placeholder:
	""" Represents a placeholder node on the graph.
	Has to be filled with a value. """
	def __init__(self):
		""" Constructs a place holder """
		self.consumers = []
		Graph._default_graph.placeholders.append(self)

class Variables:
	""" Represents a variable of the graph """
	def __init__(self, init_value = None):
		self.value = init_value
		self.consumers = []
		Graph._default_graph.variables.append(self)


class Add(Operation):
	""" Computes x + y element wise """
	def __init__(self, x, y):
		""" Constructs add operator """
		super().__init__([x, y])

	def compute(self, x, y):
		""" Computes the output """
		return x + y


class Graph:
	_default_graph = None
	""" Represents a computational graph """
	def __init__(self):
		self.operations = []
		self.placeholders = []
		self.variables = []

	def as_default(self):
		Graph._default_graph = self

class Session:
	""" Represents a computation session of the computational graph """
	def run(self, operation, feed_dict = {}):
		order = Session._traverse_postorder(operation)
		for node in order:
			if type(node) == Variables:
				node.output = node.value
			elif type(node) == Placeholder:
				node.output = feed_dict[node]
			else:
				node.inputs = [input_node.output for input_node in node.input_nodes]
				node.output = node.compute(*node.inputs)

		if type(node.output) == list:
			node.output = np.array(node.output)
		return operation.output

	@staticmethod
	def _traverse_postorder(node):
		""" Traverses the graph in postorder """
		res = []
		if node == None:
			return res
		if isinstance(node, Operation):
			for input_node in node.input_nodes:
				res += Session._traverse_postorder(input_node)
		res.append(node)
		return res
