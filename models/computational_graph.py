class Graph:
	_default_graph = None
	""" Represents a computational graph """
	def __init__(self):
		self.operations = []
		self.placeholders = []
		self.variables = []

	def as_default(self):
		Graph._default_graph = self