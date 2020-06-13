import os
import constans as const


class Validator:
    outputFilePath = ''
    inputFilePath = ''
    inputFileName = ''

    def __init__(self, args):
        if len(args) == 2:
            if self.CheckIfCorrectInputFile(args[1]):
                self.CreateOutputFilePath()
        elif len(args) != 2:
            print(const.wrongParameters)
            os._exit(-1)

    def CheckIfCorrectInputFile(self, filePath):
        if const.img in filePath or const.png in filePath:
            self.inputFilePath = filePath
            self.inputFileName = os.path.basename(filePath)
            return True
        else:
            print(const.wrongFile)
            os._exit(-1)

    def CreateOutputFilePath(self):
        self.outputFilePath = const.outputDirectory + self.inputFileName
