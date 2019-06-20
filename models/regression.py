# Logicstic Regression model
from .root_model import root_model

class logistic_regression(root_model):

	def __init__(self):
		self.name = 'Logicstic Regression'

	def recognize(self, tag):
		return (tag == 'LR') or (tag == self.name) or (tag == 'Regression')


