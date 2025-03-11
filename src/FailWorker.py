class FileWorker:
    def __init__(self, filename):
        self.filename = filename

    def write_data(self, data):
        with open(self.filename, 'w') as file:
            file.write(data)

    def read_data(self):
        with open(self.filename, 'r') as file:
            return file.read()