from queue import Queue
from .Operation import *
from .Variables import *
from .Placeholder import *
class GradientDescentOptimizer:
	def __init__(self, learning_rate):
		self.learning_rate = learning_rate

	def minimize(self, loss):
		learning_rate = self.learning_rate

		class MinimizationOperation(Operation):
			def compute(self):
				grad_table = GradientDescentOptimizer.compute_gradients(loss)
				for node in grad_table:
					if type(node) == Variables:
						grad = grad_table[node]
						node.value -= learning_rate * grad

		return MinimizationOperation()

	from queue import Queue

	@staticmethod
	def compute_gradients(loss):
		grad_table = {}
		grad_table[loss] = np.array([[1]])

		queue = Queue()
		queue.put(loss)

		while not queue.empty():
			node = queue.get()
			flag = False
			for consumer in node.consumers:
				if not(consumer in grad_table):
					flag = True
					break
			if flag:
				continue
			if node != loss:
				grad_table[node] = 0
				for consumer in node.consumers:
					lossgrad_wrt_consumer_output = grad_table[consumer]

					consumer_op_type = consumer.__class__
					bprop = RegisterGradient._gradient_registry[consumer_op_type]

					lossgrads_wrt_consumer_inputs = bprop(consumer, lossgrad_wrt_consumer_output)

					if len(consumer.input_nodes) == 1:
						grad_table[node] += lossgrads_wrt_consumer_inputs

					else:
						node_index_in_consumer_inputs = consumer.input_nodes.index(node)

						lossgrad_wrt_node = lossgrads_wrt_consumer_inputs[node_index_in_consumer_inputs]

						grad_table[node] += lossgrad_wrt_node

			if hasattr(node, "input_nodes"):
				for input_node in node.input_nodes:
					if not input_node in grad_table:
						queue.put(input_node)
		return grad_table

class RegisterGradient:
	_gradient_registry = {}
	def __init__(self, op_type):
		self._op_type = eval(op_type)

	def __call__(self, f):
		RegisterGradient._gradient_registry[self._op_type] = f
		return f


@RegisterGradient("Add")
def _add_gradient(op, grad):
	"""Computes the gradients for `add`.
	"""
	a = op.inputs[0]
	b = op.inputs[1]
	grad_wrt_a = grad
	while np.ndim(grad_wrt_a) > len(a.shape):
		grad_wrt_a = np.sum(grad_wrt_a, axis=0)
	for axis, size in enumerate(a.shape):
		if size == 1:
			grad_wrt_a = np.sum(grad_wrt_a, axis=axis, keepdims=True)

	grad_wrt_b = grad
	while np.ndim(grad_wrt_b) > len(b.shape):
		grad_wrt_b = np.sum(grad_wrt_b, axis=0)
	for axis, size in enumerate(b.shape):
		if size == 1:
			grad_wrt_b = np.sum(grad_wrt_b, axis=axis, keepdims=True)
	return [grad_wrt_a, grad_wrt_b]


@RegisterGradient("Negative")
def _negative_gradient(op, grad):
	return -grad

@RegisterGradient("Log")
def _log_gradient(op, grad):
	x = op.inputs[0]
	return grad / x

@RegisterGradient("Sigmoid")
def _sigmoid_gradient(op, grad):
	tmp = op.output
	return grad * tmp * (1 - tmp)

# @RegisterGradient("Multiply")
# def _multiply_gradient(op, grad):
# 	A = op.inputs[0]
# 	B = op.inputs[1]
# 	grad_A = flatten(grad * B)
# 	grad_B = flatten(grad * A)
# 	# print("a = ", grad_A)
# 	# print("b = ", grad_B)
# 	return [grad_A, grad_B]

@RegisterGradient("Matmul")
def _matmul_gradient(op, grad):
	A = op.inputs[0]
	B = op.inputs[1]
	grad_A = grad.dot(B.T)
	grad_B = A.T.dot(grad)
	return [grad_A, grad_B]

@RegisterGradient("ReduceSum")
def _reduce_sum_gradient(op, grad):
	A = op.inputs[0]
	output_shape = np.array(A.shape)
	output_shape[op.axis] = 1
	tile_scaling = A.shape // output_shape
	grad = np.reshape(grad, output_shape)
	return np.tile(grad, tile_scaling)

@RegisterGradient("Transpose")
def _tranpose_gradient(op, grad):
	return grad.T