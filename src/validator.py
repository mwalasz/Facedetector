import os


class Validator:
    outputFilePath = ''
    inputFilePath = ''
    inputFileName = ''

    def __init__(self, args):
        if len(args) == 2:
            if self.CheckIfCorrectInputFile(args[1]):
                self.CreateOutputFilePath()
        elif len(args) != 2:
            print("Wrong number of parameters!")
            os._exit(-1)

    def CheckIfCorrectInputFile(self, filePath):
        if ".jpg" in filePath or "png" in filePath:
            self.inputFilePath = filePath
            self.inputFileName = os.path.basename(filePath)
            return True
        else:
            print("Wrong input file!")
            os._exit(-1)

    def CreateOutputFilePath(self):
        self.outputFilePath = 'resources\output_img\\' + self.inputFileName
