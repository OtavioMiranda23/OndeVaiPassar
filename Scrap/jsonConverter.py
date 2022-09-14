import json


class Json_Converter:
    def __init__(self, path, fileName, data):
        self.path = path
        self.fileName = fileName
        self.data = data

    def EscreveJsonFile(self):
        filePathNameExtension = './' + self.path + '/' + self.fileName + '.json'
        with open(filePathNameExtension, 'w') as f:
            json.dump(self.data, f)
