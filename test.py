import matplotlib.pyplot as plt
import matplotlib.colors as clr

Blues = plt.get_cmap('Blues')
color = Blues(0.5)
hexx = clr.to_hex(color)
print(hexx)
