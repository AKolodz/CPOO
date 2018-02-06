import cv2
from pylab import *
from matplotlib import pyplot
import numpy as np
import peakutils
from peakutils.plot import plot as pplot

class DynamicContrast:
    def determineDynamicContrast(image):
        dynamicContrastModul = image[1240:2348, 977:1083]
        cv2.imshow("modul", dynamicContrastModul)
        dynamicContrastModul = cv2.medianBlur(dynamicContrastModul, 7)
        column = dynamicContrastModul[0:1020, 100]
        column = np.asarray(column, dtype=np.float)
        indexes = peakutils.indexes(column, thres=0.02 / max(column), min_dist=100)
        title('Wykres')
        pyplot.plot(column)
        savefig('wykres.png')
        x = np.linspace(0, 1019, 1020)
        pplot(x, column, indexes)
        savefig('wykres2.png')