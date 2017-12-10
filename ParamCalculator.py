import cv2

from ImageCutter import ImageCutter


class ParamCalculator:

    @staticmethod
    def getSNR(image, p1, p2):
        snrPhantom = ImageCutter.cut(image, p1, p2)
        cv2.namedWindow("SNR", cv2.WINDOW_NORMAL)
        cv2.imshow("SNR", snrPhantom)
        mean, stddev = cv2.meanStdDev(snrPhantom)
        snr = mean / stddev
        print("ROI : mean {}, sd {} SNR {}".format(mean, stddev, snr))
        return snr
