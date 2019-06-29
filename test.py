from models.model_prototype import model_prototype
from models.computational_graph import Graph
from models.Session import Session
from models.Variables import Variables
from models.Operation import *
from models.Placeholder import Placeholder
from models.computational_graph import Graph
from models.Optimizer import *
from visualizer import visualizer
import numpy as np
from PIL import Image

if __name__ == '__main__':
	# a = np.array([[1], [2], [3]])
	# # b = np.array([[1,2 , 3, 3],
	# # 		[4, 5, 6, 6],
	# # 		[7, 8, 9, 9]])
	# b = np.array([[4], [5], [6]])
	# print(a.T.dot(b) - 1)

	mp = model_prototype()
	W = np.random.uniform(2, 1, 3)
	x1 = np.random.uniform(-10, 10, 10)
	x2 = np.random.uniform(-10, 10, 10)
	x3 = np.array([1] * 10)
	X = np.array([x1, x2, x3]).transpose()
	y = np.array([1 if val >=0 else 0 for val in X.dot(W)])
	md = mp.recognize("Logistic")
	X = np.hstack((X[0:len(X),0:-1], np.array([y]).T))
	# print(X)
	md.feed_data(X)
	# print(md.weights)
	sess = Session()
	for i in range(0, 100):
		md.next_step()
	vs = visualizer(md, (5, 5), (-5, 5), (-5, 5))
	image = vs.visualize()
	image.save("bla.png")
	image.show()

	# yy = np.array([1 if val >=0 else 0 for val in X.dot(md.weights)])
	# print("yy = ", yy)
	# print("y = ", y)
	# print(md.weights)