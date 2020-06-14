import numpy as np
import cv2
from PIL import Image
import concat_images as con


class MergeResults:
    images = []
    numberOfImages = 0
    imgPerRow = 2
    columns = 5
    mergedImages = 0

    def __init__(self, img):
        length = len(img)

        if length != 0:
            self.numberOfImages = length
            self.images = img
            print(length)

  def Merge(self):
        temp = [[]]  # 2d array with faces

        row = int(self.numberOfImages / self.columns)

        i = 0
        j = 0
        for x in self.images:
            if self.numberOfImages == 1:
                face = cv2.resize(x, dsize=(150, 150))
                temp[0].append(face)
            else:
                j = j + 1

                face = cv2.resize(x, dsize=(150, 150))
                temp[i].append(face)

                if j % self.columns == 0:
                    i = i + 1
                    if self.columns * i < self.numberOfImages:
                        temp.append([])

        self.mergedImages = con.concat_tile_resize(temp)
    def Show(self):
        if (self.numberOfImages > 1):
            cv2.imshow(str(self.numberOfImages) +
                       " detected faces:", self.mergedImages)
            cv2.waitKey()
            cv2.destroyAllWindows()
            