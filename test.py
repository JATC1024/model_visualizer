from model_store import model_store

if __name__ == '__main__':
	ms = model_store()
	ms.recognize('SVM')
	print(ms.current.get_arguments())