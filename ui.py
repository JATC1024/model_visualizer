# User interface
# Show information and read input from user
# Draw output to user

from model_store import model_store

def choose_model(model):
	while True:
		tag = input('Choose a model: (SVM or LR) ')
		ok = model.recognize(tag)
		if ok == True:
			break
	
def configure_model(model):
	args = model.get_arguments()
	values = {}
	for arg in args
		val = input('%s (%s): ' %(arg[0], arg[1]))
		values[arg[0]] = val
	model.set_arguments(values)

def feed_data(model):
	n = int(input('Enter number of datas: '))
	for i in range(0,n):
		element = input('Enter data %d' %i)
		params = [int(x) for x in elelement.split(' ')]
		x1, x2, y = params
		model.add_one_data((x1,x2,y))
	model.feed_data()

def control_model(model):
	print('This work is not done')

if __name__ == "__main__":
	
	model = model_store()
	choose_model(model)
	configure_model(model)
	feed_data(model)
	control_model(model)
