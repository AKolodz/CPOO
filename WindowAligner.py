import cv2
import numpy as np


class WindowAligner:

    @staticmethod
    def align(image):
        resolutionMultiplier = 4
        lowResImg = lowerResolution(image, resolutionMultiplier)

        lowResImg = removeMargins(lowResImg, 10)
        image = removeMargins(image, 10 * resolutionMultiplier)

        edges = cv2.Canny(lowResImg, 400, 350, None, 3)
        cv2.namedWindow("Edges", cv2.WINDOW_NORMAL)
        cv2.imshow("Edges", edges)

        # morphological opening?

        angle = findRotationDegree(edges, lowResImg)
        cv2.namedWindow("Alignment line", cv2.WINDOW_NORMAL)
        cv2.imshow("Alignment line", lowResImg)

        rows, cols = image.shape
        rotationMatrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
        rotatedImage = cv2.warpAffine(image, rotationMatrix, (cols, rows))

        # let user choose 2 points (left upper corner and right bottom corner) that define boundaries of the result image
        # leftUpperCornerPoint = getPoint(rotatedImage)
        # rightBottomCornerPoint = getPoint(rotatedImage)
        # x1, y1 = leftUpperCornerPoint
        # x2, y2 = rightBottomCornerPoint

        x1, y1 = (448, 608)
        x2, y2 = (662 * 4, 705 * 4)
        
        return rotatedImage[y1:y2, x1:x2]


def lowerResolution(image, times):
    return cv2.resize(image, (0, 0), fx=1 / times, fy=1 / times)


def removeMargins(image, pxMargin):
    rows, cols = image.shape
    return image[pxMargin:cols - pxMargin, pxMargin:rows - pxMargin]


def findRotationDegree(edgesImage, destImage):
    angle = -1
    threshold = 180
    minLineLength = 100
    maxLineGap = 10
    lines = cv2.HoughLinesP(edgesImage, 1, np.pi / 180, threshold, None, minLineLength, maxLineGap)
    if lines is not None:
        chosenLine = 2
        for i in range(0, len(lines)):
            for x1, y1, x2, y2 in lines[chosenLine]:
                cv2.line(destImage, (x1, y1), (x2, y2), (0, 255, 0), 2)
                deltay = abs(y1 - y2)
                deltax = abs(x1 - x2)
                rads = np.math.atan(deltay / deltax)
                angle = rads * 360 / (2 * np.pi)
    else:
        angle = -999
    return angle


def getPoint(image):
    pass

