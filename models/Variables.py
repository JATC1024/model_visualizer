from .computational_graph import Graph
import numpy as np
class Variables:
	""" Represents a variable of the graph """
	def __init__(self, init_value = None):
		self.value = init_value
		if (self.value.ndim == 1):
			self.value = self.value[:,np.newaxis]
		self.consumers = []
		Graph._default_graph.variables.append(self)