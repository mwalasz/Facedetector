from detector import Detector
from validator import Validator
from mergeResults import MergeResults
import sys
import os

v = Validator(sys.argv)
d = Detector()

d.LoadImage(v.inputFilePath)
d.Run()
d.DisplayResultPhoto()

m = MergeResults(d.picturesOfFaces)
m.Show()
# d.SaveResult(v.outputFilePath)
