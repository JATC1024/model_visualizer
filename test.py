from models import model_store

if __name__ == '__main__':
	if (model_store.recognize('SVM')):
		model = model_store.current
		print(model.get_arguments())
		print('OK')
	else:
		print('Not OK')