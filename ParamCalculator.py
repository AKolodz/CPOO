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

    @staticmethod
    def evalHomogeneousness(roi1, roi2, roi3, roi4, referenceRoi):
        isHomogeneous = True
        mean1, _ = cv2.meanStdDev(roi1)
        mean2, _ = cv2.meanStdDev(roi2)
        mean3, _ = cv2.meanStdDev(roi3)
        mean4, _ = cv2.meanStdDev(roi4)
        referenceMean, _ = cv2.meanStdDev(referenceRoi)

        means = (mean1, mean2, mean3, mean4)
        for mean in means:
            if abs(referenceMean - mean) > 0.1 * referenceMean:
                isHomogeneous = False
        return isHomogeneous

