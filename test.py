from models.model_prototype import model_prototype
from models.computational_graph import Graph
from models.Session import Session
from models.Variables import Variables
from models.Operation import *
from models.Placeholder import Placeholder

if __name__ == '__main__':
	md = model_prototype.create_model("Logistic")
	# Calculates the value for point [2, 1]
	output = md.inference([2, 1])
	print(output)