# User interface
# Show information and read input from user
# Draw output to user

#from model_store import model_store
import tkinter as tk
from tkinter import ttk

'''
def choose_model(model):
	while True:
		tag = input('Choose a model: (SVM or LR) ')
		ok = model.recognize(tag)
		if ok == True:
			break
	
def configure_model(model):
	args = model.get_arguments()
	values = {}
	for arg in args:
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
'''

if __name__ == "__main__":
	# Main form
	form = tk.Tk()
	form.title("Model visualizer")
	form.geometry("500x280")
	
	# Create tabs
	tab_parent = ttk.Notebook(form)
	tab_model = ttk.Frame(tab_parent)
	tab_config = ttk.Frame(tab_parent)
	tab_data = ttk.Frame(tab_parent)
	tab_visual = ttk.Frame(tab_parent)

	# Assign tabs to parents
	tab_parent.add(tab_model, text = "Model")
	tab_parent.add(tab_config, text = "Configure")
	tab_parent.add(tab_data, text = "Data")
	tab_parent.add(tab_visual, text = "Visualization")

	# Widgets for tab_model
	title_tab_model = tk.Label(tab_model, text = "Choose a model")
	

	# Show
	tab_parent.pack(expand=1, fill="both")
	form.mainloop()
