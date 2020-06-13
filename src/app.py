from detector import Detector
from validator import Validator
import sys
import os

v = Validator(sys.argv)
d = Detector()

d.LoadImage(v.inputFilePath)
d.Run()
d.DisplayResultPhoto()
d.SaveResult(v.outputFilePath)
