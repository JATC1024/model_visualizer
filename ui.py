# User interface
# Show information and read input from user
# Draw output to user

from functools import partial
from data.data_sample import data_sample
from model_manager import model_manager
import tkinter as tk
from tkinter import ttk, messagebox

class ui_manager:
	def __init__(self):
		# Model manager
		self.models = model_manager()
		self.samples = data_sample()
		self.pad = 10

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
			btn = tk.Button(self.tab_model, text = md, command = partial(self.choose_model, md))
			self.button_tab_model.append(btn)

		# Add Widgets to tab_model
		self.title_tab_model.grid(row=0,column=0, padx=self.pad, pady=self.pad, sticky = 'W')
		r = 0
		for btn in self.button_tab_model:
			r = r + 1
			btn.grid(row=r, column=0, padx=self.pad, pady=self.pad, sticky = 'W')

		# Disable other tabs
		self.tab_parent.tab(1, state="disabled")
		self.tab_parent.tab(2, state="disabled")
		self.tab_parent.tab(3, state="disabled")

		# Events
		self.tab_parent.bind("<<NotebookTabChanged>>", self.on_tab_selected)

		# Show
		self.tab_parent.pack(expand=1, fill="both")
		self.form.mainloop()

	def on_tab_selected(self, event):
		id = event.widget.index("current")
		if id == 1:
			self.enable_configure()
		elif id == 2:
			self.enable_data()
		
	def choose_model(self, tag):
		if self.models.recognize(tag):
			self.tab_parent.tab(1, state="normal")
			self.tab_parent.tab(2, state="disabled")
			self.tab_parent.tab(3, state="disabled")
			self.tab_parent.select(1)

	def enable_configure(self):
		# Set widget for tab_config
		self.title_tab_config = tk.Label(self.tab_config, text = self.models.name())
		args = self.models.get_arguments()
		self.label_tab_config = []
		self.entry_tab_config = []
		for name in args:
			label = tk.Label(self.tab_config, text = name)
			entry = self.get_entry(self.tab_config, args[name])
			self.label_tab_config.append(label)
			self.entry_tab_config.append(entry)
		self.button_tab_config = tk.Button(self.tab_config, text="Assign", command = self.set_configure)
	
		# Add widget to tab_config
		self.title_tab_config.grid(row=0, column=0, padx=self.pad, pady=self.pad, sticky='W')
		r = 0
		for pair in zip(self.label_tab_config, self.entry_tab_config):
			r = r+1			
			pair[0].grid(row=r, column=0, padx=self.pad, pady=self.pad, sticky='W')
			pair[1].grid(row=r, column=1, padx=self.pad, pady=self.pad, sticky='W')
		self.button_tab_config.grid(row=r+1, column=0, padx=self.pad, pady=self.pad)

	def get_entry(self, tab, arg):
		if arg["type"] == "float":
			ent = tk.Entry(tab)
			#ent.delete(0, end)
			ent.insert(0, arg["default"])
			return ent
		elif arg["type"] == "string":
			cb = ttk.Combobox(tab, values = arg["option"])
			cb.current(0)
			return cb
		else:
			return None

	def set_configure(self):
		if self.check_configure():
			args = {}
			for pair in zip(self.label_tab_config, self.entry_tab_config):
				name = pair[0]
				value = pair[1].get()
				args[name] = value
			self.models.set_arguments(args)
			self.tab_parent.tab(2, state="normal")
			self.tab_parent.select(2)
		else:
			messagebox.showinfo("Configure Error", "Invalid information")

	def check_configure(self):
		for entry in self.entry_tab_config:
			if isinstance(entry, ttk.Combobox):
				if not(entry.get() in entry["values"]):
					return False
			elif isinstance(entry, tk.Entry):
				try:
					checktype = float(entry.get())
				except ValueError:
					return False
		return True

	def enable_data(self):
		# Set widget for tab_data
		self.title_left_tab_data = tk.Label(self.tab_data, text = "Resample")
		self.preset_tab_data = []
		presets = self.samples.list()
		for preset in presets:
			btn = tk.Button(self.tab_data, text = preset, command = partial(self.set_preset, preset))
			self.preset_tab_data.append(btn)
		self.title_right_tab_data = tk.Label(self.tab_data, text = "Choose class, then draw point")
		self.side = 0
		self.radio0_tab_data = tk.Radiobutton(self.tab_data, text = "Class 0", variable = self.side, value = 0, state="active")
		self.radio1_tab_data = tk.Radiobutton(self.tab_data, text = "Class 1", variable = self.side, value = 1)
		self.radio0_tab_data.select()
		# Add widget to tab
		self.title_left_tab_data.grid(row=0, column=0, padx=self.pad, pady=self.pad, sticky='W')
		r = 0
		for preset in self.preset_tab_data:
			r = r+1
			preset.grid(row=r, column=0, padx=self.pad, pady=self.pad, sticky='W')
		self.title_right_tab_data.grid(row=0, column=1, columnspan=2, padx=self.pad, pady=self.pad, sticky='W')
		self.radio0_tab_data.grid(row=1, column=1, padx=self.pad, pady=self.pad, sticky='W')
		self.radio1_tab_data.grid(row=1, column=2, padx=self.pad, pady=self.pad, sticky='W')

	def set_preset(self, tag):
		pass
		
'''

def feed_data(model):
	n = int(input('Enter number of datas: '))
	for i in range(0,n):
		element = input('Enter data %d' %i)
		params = [int(x) for x in elelement.split(' ')]
		x1, x2, y = params
		model.add_one_data((x1,x2,y))
	model.feed_data()
'''

if __name__ == "__main__":
	manager = ui_manager()
