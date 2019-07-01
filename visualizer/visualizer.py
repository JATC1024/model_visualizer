import matplotlib
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from PIL import Image
import sys
from PyQt5.QtWidgets import QApplication

class visualizer:
    dense = 100

    def __init__(self, model, figure_size, xlim, ylim):
        self.model = model
        self.figure_size = figure_size
        self.xlim = xlim
        self.ylim = ylim

    def visualize(self):
        app = QApplication(sys.argv)
        screen = app.screens()[0]
        dpi = screen.physicalDotsPerInch()
        app.quit()
        xx = np.linspace(self.xlim[0], self.xlim[1], visualizer.dense)
        yy = np.linspace(self.ylim[0], self.ylim[1], visualizer.dense)
        xx, yy = np.meshgrid(xx, yy)

        X = np.array([[p[0], p[1]] for p in zip(xx.flatten(), yy.flatten())])
        zz = self.model.inference(X).reshape(xx.shape)

        fig = plt.figure(figsize = (self.figure_size[0] / dpi, self.figure_size[1] / dpi))
        # ax = plt.gca()
        # fig = Figure(figsize = self.figure_size)
        # canvas = FigureCanvas(fig)
        ax = fig.gca()
        ax.pcolor(xx, yy, zz, cmap = 'RdBu_r')
        sns.scatterplot(self.model._X[:,0], self.model._X[:,1], hue = self.model._y, ax = ax)
        ax.set_xlim(self.xlim)
        ax.set_ylim(self.ylim)
        ax.axis('off')
        ax.legend().remove()

        plt.savefig("tmp.png", dpi = dpi)
        image = Image.open("tmp.png")
        return image
        # plt.show()
        # canvas.draw()
        # width, height = fig.get_size_inches() * fig.get_dpi()
        # image = np.fromstring(canvas.tostring_rgb(), dtype='uint8').reshape(int(height), int(width), 3)
        # img = Image.fromarray(image, 'RGB')

        #plt.show()

        # return np.array(fig.canvas.renderer.buffer_rgba())
