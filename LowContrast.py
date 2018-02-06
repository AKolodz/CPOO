import cv2
import numpy as np


class LowContrast:
    @staticmethod
    def determineLowContrast(image):
        ref_roi = image[900:1000, 1480:1560]
        ref_mean = ref_roi.mean()
        cut = image[603:1630, 1560:1730]
        resized = cv2.resize(cut, (0, 0), fx=0.5, fy=0.5)
        median = cv2.medianBlur(resized, 7)
        equalized = cv2.equalizeHist(median)
        edges = cv2.Canny(equalized, 150, 140, None, 3)
        binary = cv2.adaptiveThreshold(edges, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                       cv2.THRESH_BINARY, 13, 4)
        circles = cv2.HoughCircles(binary, cv2.HOUGH_GRADIENT, 1, 20,
                                   param1=50, param2=30, minRadius=20, maxRadius=50)
        circles = np.uint16(np.around(circles))
        draw_circles(circles, ref_mean, equalized)


def draw_circles(circles, ref_mean, image):
    for i in range(2):
        cv2.circle(image, (circles[0, 0, 0], circles[0, i, 1]), circles[0, 0, 2], (0, 255, 0), 2)
        cv2.circle(image, (circles[0, 0, 0], circles[0, i, 1]), 2, (0, 0, 255), 3)

    circle3 = image[194:214, 34:54]
    circle4 = image[280:300, 34:54]
    circle5 = image[366:386, 34:54]
    circle6 = image[452:472, 34:54]
    if circle3.mean() > 1.5 * ref_mean:
        cv2.circle(image, (circles[0, 0, 0], 204), circles[0, 0, 2], (0, 255, 0), 2)
        cv2.circle(image, (circles[0, 0, 0], 204), 2, (0, 0, 255), 3)

    if circle4.mean() > 1.5 * ref_mean:
        cv2.circle(image, (circles[0, 0, 0], 290), circles[0, 0, 2], (0, 255, 0), 2)
        cv2.circle(image, (circles[0, 0, 0], 290), 2, (0, 0, 255), 3)

    if circle5.mean() > 1.5 * ref_mean:
        cv2.circle(image, (circles[0, 0, 0], 376), circles[0, 0, 2], (0, 255, 0), 2)
        cv2.circle(image, (circles[0, 0, 0], 376), 2, (0, 0, 255), 3)

    if circle6.mean() > 1.5 * ref_mean:
        cv2.circle(image, (circles[0, 0, 0], 462), circles[0, 0, 2], (0, 255, 0), 2)
        cv2.circle(image, (circles[0, 0, 0], 462), 2, (0, 0, 255), 3)
    cv2.imshow('detected circles ph', image)
