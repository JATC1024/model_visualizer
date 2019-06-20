# User interface
# Show information and read input from user
# Draw output to user

from model_store import model_store

def choose_model():
	model = model_store()
	while True:
		tag = input('Choose a model: (SVM or LR) ')
		ok = model.recognize(tag)
		if ok == True:
			break
	return model
	
def configure_model(model):
	print('This work is not done')

def control_model(model):
	print('This work is not done')

if __name__ == "__main__":
	
	model = choose_model()
	configure_model(model)
	control_model(model)
