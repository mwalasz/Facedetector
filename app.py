from detector import Detector
import sys

d = Detector()

d.LoadImage(sys.argv[1])
d.DetectFaces()
d.DisplayResult()
