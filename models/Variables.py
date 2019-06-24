from .computational_graph import Graph

class Variables:
	""" Represents a variable of the graph """
	def __init__(self, init_value = None):
		self.value = init_value
		self.consumers = []
		Graph._default_graph.variables.append(self)