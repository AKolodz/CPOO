import cv2
from pylab import *
from matplotlib import pyplot
import numpy as np
import peakutils
from peakutils.plot import plot as pplot


class DynamicContrast:
    @staticmethod
    def determineDynamicContrast(image):
        rows, cols = image.shape
        dynamicContrastModule = cv2.medianBlur(image, 7)
        # column = dynamicContrastModule[0:rows, cols-1]
        column = np.asarray(dynamicContrastModule, dtype=np.float)
        column = np.sum(column, 1)
        indexes = peakutils.indexes(column, thres=0.1 / max(column), min_dist=120)

        pyplot.plot(column)
        savefig('dynamicContrast.png')
        x = np.linspace(0, rows-1, rows)
        pplot(x, column, indexes)
        savefig('dynamiContrastPeaks.png')
