import cv2
import numpy as np


class Detector:
    detectedFaces = 0
    fileName = ''
    img = ''
    gray_img = ''
    face_haar_classifiers = 0
    faces = 0
    r = 255
    g = 0
    b = 0

    def __init__(self):
        self.face_haar_classifiers = cv2.CascadeClassifier(
            'resources\classifiers\haarcascade_frontalface_default.xml')

    def LoadImage(self, file):
        self.fileName = file
        self.img = cv2.imread(self.fileName)

    def ConvertImgToGray(self):
        self.gray_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

    def MarkDetectedFaces(self):
        for (x, y, w, h) in self.faces:
            cv2.rectangle(self.img, (x, y), (x + w, y + h),
                          (self.b, self.g, self.r), 3)

    def DetectFaces(self):
        self.ConvertImgToGray()
        self.faces = self.face_haar_classifiers.detectMultiScale(
            self.gray_img, 1.3, 5)
        self.detectedFaces = len(self.faces)
        self.MarkDetectedFaces()

    def DisplayResult(self):
        cv2.imshow('Detection output for: ' + str(self.fileName), self.img)
        cv2.waitKey()

    def SaveResult(self, file):
        cv2.imwrite(file, self.img)
