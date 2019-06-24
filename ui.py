# User interface
# Show information and read input from user
# Draw output to user

from model_manager import model_manager
import tkinter as tk
from tkinter import ttk

class ui_manager:
	def __init__(self):
		# Model manager
		self.models = model_manager()

		# Main form
		self.form = tk.Tk()
		self.form.title("Model visualizer")
		self.form.geometry("500x280")
		
		# Create tabs
		self.tab_parent = ttk.Notebook(self.form)
		self.tab_model = ttk.Frame(self.tab_parent)
		self.tab_config = ttk.Frame(self.tab_parent)
		self.tab_data = ttk.Frame(self.tab_parent)
		self.tab_visual = ttk.Frame(self.tab_parent)

		# Assign tabs to parents
		self.tab_parent.add(self.tab_model, text = "Model")
		self.tab_parent.add(self.tab_config, text = "Configure")
		self.tab_parent.add(self.tab_data, text = "Data")
		self.tab_parent.add(self.tab_visual, text = "Visualization")

		# Widgets for tab_model
		self.title_tab_model = tk.Label(self.tab_model, text = "Choose a model")
		model_list = self.models.list()
		self.button_tab_model = []
		for md in model_list:
			btn = tk.Button(self.tab_model, text = md)
			self.button_tab_model.append(btn)

		# Add Widgets to tab_model
		self.title_tab_model.grid(row=0,column=0, padx=15, pady=15, sticky = 'W')
		r = 0
		for btn in self.button_tab_model:
			r = r + 1
			btn.grid(row=r, column=0, padx=15, pady=15, sticky = 'W')

		# Show
		self.tab_parent.pack(expand=1, fill="both")
		self.form.mainloop()
		
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
	manager = ui_manager()
