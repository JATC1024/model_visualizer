from .Variables import Variables
from .Placeholder import Placeholder
from .Operation import Operation
import numpy as np

class Session:
	""" Represents a computation session of the computational graph """
	def run(self, operation, feed_dict = {}):
		order = Session._traverse_postorder(operation)
		for node in order:
			if type(node) == Variables:
				node.output = node.value
			elif type(node) == Placeholder:
				node.output = feed_dict[node.name]
			else:
				node.inputs = [input_node.output for
						input_node in node.input_nodes]
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
