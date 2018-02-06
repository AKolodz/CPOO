import cv2
import numpy as np


class NoiseGenerator:
    @staticmethod
    def addGaussian(image, mean, stddev):
        noise = np.copy(image)
        cv2.randn(noise, mean, stddev)
        noisedImage = image + noise
        return noisedImage
