import matplotlib
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
from PIL import Image

class visualizer:
    dense = 100

    def __init__(self, model, figure_size, xlim, ylim):
        self.model = model
        self.figure_size = figure_size
        self.xlim = xlim
        self.ylim = ylim

    def visualize(self):        
        xx = np.linspace(self.xlim[0], self.xlim[1], visualizer.dense)
        yy = np.linspace(self.ylim[0], self.ylim[1], visualizer.dense)
        xx, yy = np.meshgrid(xx, yy)
        
        X = np.array([[p[0], p[1]] for p in zip(xx.flatten(), yy.flatten())])
        zz = self.model.inference(X).reshape(xx.shape)
        
        # fig = plt.figure(figsize = self.figure_size)
        # ax = plt.gca()
        fig, ax = plt.subplots()
        ax.pcolor(xx, yy, zz, cmap = 'RdBu_r')
        #sns.scatterplot(self.model._X[:,0], self.model._X[:,1], hue = self.model._y, ax = ax)
        ax.legend().remove()
        ax.set_xlim(self.xlim)
        ax.set_ylim(self.ylim)
        #plt.axis('off')
        fig.canvas.draw()
        #plt.show()

        return np.array(fig.canvas.renderer.buffer_rgba())