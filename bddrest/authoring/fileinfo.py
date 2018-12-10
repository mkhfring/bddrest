from os import path


class FileInfo:

    def __init__(self, filename):
        self.filename = filename

    @property
    def name(self):
        path = self.filename.rsplit('/', 1)
        return path[-1]

    @property
    def directory(self):
        path = self.filename.rsplit('/', 1)
        return path[0]

    def to_dict(self):
        return dict(name=self.name, directory=self.directory)

