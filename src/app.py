from detector import Detector
from validator import Validator
import sys
import os

v = Validator(sys.argv)

input_file_path = sys.argv[1]  # todo: walidacja
file_name = os.path.basename(input_file_path)

d = Detector()
d.LoadImage(input_file_path)
d.Run()
d.DisplayResultPhoto()
#d.SaveResult('resources\output_img\\' + file_name)
