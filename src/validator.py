import os


class Validator:
    outputFile = ''
    inputFile = ''

    def __init__(self, args):
        if len(args) == 2:
            self.CheckIfCorrectInputFile(args[1])
        elif len(args) != 2:
            print("Wrong number of parameters!")
            os._exit(-1)

    def CheckIfCorrectInputFile(self, fileName):
        if ".jpg" in fileName or "png" in fileName:
            self.inputFile = fileName
        else:
            print("Wrong input file!")
            os._exit(-1)
