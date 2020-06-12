import cv2
import numpy as np


class Detector:
    detectedFaces = 0
    fileName = ''
    img = ''
    gray_img = ''
    face_haar_classifier = 0
    eye_haar_classifier = 0
    faces = 0
    pictures_of_faces = []
    eyes = 0
    color = (0, 0, 255)

    def __init__(self):
        self.face_haar_classifier = cv2.CascadeClassifier(
            'resources\classifiers\haarcascade_frontalface_default.xml')
        self.eye_haar_classifier = cv2.CascadeClassifier(
            'resources\classifiers\haarcascade_eye.xml')

    def LoadImage(self, file):
        self.fileName = file
        self.img = cv2.imread(self.fileName)

    def ConvertImgToGray(self):
        self.gray_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

    def MarkDetectedFaces(self):
        for (x, y, w, h) in self.faces:
            cv2.rectangle(self.img, (x, y), (x + w, y + h),
                          self.color, 3)

    def MarkDetectedEyes(self):
        for face in self.pictures_of_faces:
            for (ex, ey, ew, eh) in self.eyes:
                cv2.rectangle(face, (ex, ey),
                              (ex+ew, ey+eh), (0, 255, 0), 2)

    def DrawNumberOfFaces(self):
        height, width, channels = self.img.shape
        cv2.putText(self.img, "Detected: " + str(self.detectedFaces),
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    self.color,
                    2)

    def DetectFaces(self):
        self.ConvertImgToGray()
        self.faces = self.face_haar_classifier.detectMultiScale(
            self.gray_img, 1.3, 5)
        self.detectedFaces = len(self.faces)
        self.DetectEyes()
        self.DrawNumberOfFaces()
        self.MarkDetectedEyes()
        self.MarkDetectedFaces()

    def DetectEyes(self):
        for (x, y, w, h) in self.faces:
            roi_gray = self.gray_img[y:y+h, x:x+w]
            self.pictures_of_faces.append(self.img[y:y+h, x:x+w])
            self.eyes = self.eye_haar_classifier.detectMultiScale(
                roi_gray)

    def DisplayResult(self):
        cv2.imshow('Detection output for: ' + str(self.fileName), self.img)
        cv2.waitKey()

    def SaveResult(self, path):
        if (len(path) != 0):
            cv2.imwrite(path, self.img)
        else:
            oldFileName = str(self.fileName).split('.')
            newFileName = oldFileName[0] + '_output.' + oldFileName[1]
            cv2.imwrite(newFileName, self.img)
