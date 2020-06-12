import cv2
import numpy as np


class Detector:
    numberOfDetectedFaces = 0
    numberOfDetectedEyes = 0
    fileName = ''
    img = ''
    grayImg = ''
    faceClassifier = 0
    eyeClassifier = 0
    facesCoords = 0
    eyesCoords = 0
    picturesOfFaces = []
    color = (0, 0, 255)

    def __init__(self):
        self.faceClassifier = cv2.CascadeClassifier(
            'resources\classifiers\haarcascade_frontalface_default.xml')
        self.eyeClassifier = cv2.CascadeClassifier(
            'resources\classifiers\haarcascade_eye.xml')

    def Run(self):
        self.DetectFaces()
        self.DetectEyes()

        self.DrawResults()

    def DrawResults(self):
        self.DrawNumberOfFaces()

        if (self.numberOfDetectedFaces * 2) == self.numberOfDetectedEyes:
            self.DrawDetectedEyes()

        self.DrawDetectedFaces()

    def LoadImage(self, file):
        self.fileName = file
        self.img = cv2.imread(self.fileName)

    def ConvertImgToGray(self):
        self.grayImg = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

    def DrawDetectedFaces(self):
        for (x, y, w, h) in self.facesCoords:
            cv2.rectangle(self.img, (x, y), (x + w, y + h),
                          self.color, 3)

    def DrawDetectedEyes(self):
        for face in self.picturesOfFaces:
            for (ex, ey, ew, eh) in self.eyesCoords:
                cv2.rectangle(face, (ex, ey),
                              (ex+ew, ey+eh), (0, 255, 0), 2)

    def DrawNumberOfFaces(self):
        height, width, channels = self.img.shape
        cv2.putText(self.img, "Detected: " + str(self.numberOfDetectedFaces),
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    self.color,
                    2)

    def DetectFaces(self):
        self.ConvertImgToGray()
        self.facesCoords = self.faceClassifier.detectMultiScale(
            self.grayImg, 1.3, 5)
        self.numberOfDetectedFaces = len(self.facesCoords)

    def DetectEyes(self):
        for (x, y, w, h) in self.facesCoords:
            grayFace = self.grayImg[y:y+h, x:x+w]
            self.picturesOfFaces.append(self.img[y:y+h, x:x+w])
            self.eyesCoords = self.eyeClassifier.detectMultiScale(
                grayFace)
            self.numberOfDetectedEyes += len(self.eyesCoords)

    def DisplayResultPhoto(self):
        cv2.imshow('Detection output for: ' + str(self.fileName), self.img)
        cv2.waitKey()

    def SaveResult(self, path):
        if (len(path) != 0):
            cv2.imwrite(path, self.img)
        else:
            oldFileName = str(self.fileName).split('.')
            newFileName = oldFileName[0] + '_output.' + oldFileName[1]
            cv2.imwrite(newFileName, self.img)
