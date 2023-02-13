import numpy as np

class Maze:
    def __init__(self, size = 4):
        self.size  = size
        self.grid  = np.zeros((size, size))
        self.begin = None
        self.end   = None

    def reroal(self):
        self.