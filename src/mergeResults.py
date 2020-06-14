class MergeResults:
    images = []
    numberOfImages = 0

    def __init__(self, img):
        length = len(img)

        if length != 0:
            self.numberOfImages = length
            self.images = img
