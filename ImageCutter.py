class ImageCutter:

    @staticmethod
    def cut(image, p1, p2):
        return image[p1[1]:p2[1], p1[0]:p2[0]]