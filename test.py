from models.model_prototype import model_prototype
from models.computational_graph import Graph

if __name__ == '__main__':
	# md = model_prototype.create_model("Support Vector Machines")
	# md.print()
	Graph().as_default()
	x = Placeholder()
	y = Placeholder()
	plus = Add(x, y)
	sess = Session()
	output = sess.run(plus, {x : [2, 3], y : [3, 1]})
	print(output)