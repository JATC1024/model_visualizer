from .computational_graph import Graph

class Placeholder:
	""" Represents a placeholder node on the graph.
	Has to be filled with a value. """
	def __init__(self, name):
		""" Constructs a place holder """
		self.consumers = []
		self.name = name
		Graph._default_graph.placeholders.append(self)