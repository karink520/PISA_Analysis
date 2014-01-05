import sys
import os

__author__ = 'karin'
DATA_FOLDER = '../data'
DATA_FILES = [os.path.join(DATA_FOLDER, filename) for filename in os.listdir(DATA_FOLDER)]

def __main():
    d = DataFile(DATA_FILES[0])
    d.head(1)
class DataFile:
    def __init__(self, filename):
        self.filename = filename

    def head(self,n_lines=10):
        with open(self.filename) as f:
            counter = 0
            while counter < n_lines:
                print f.next()
                counter +=1

if __name__ == "__main__":
    sys.exit(__main())
