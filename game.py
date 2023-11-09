import numpy as np


class GameOfLife:

    def __init__(self):
        self.map_width = 100
        self.map_height = 100
        self.map_size = [self.map_width, self.map_height]
        self.population = np.zeros(self.map_size, dtype=np.int8)

    def set_map_size(self, width, height):
        self.map_width = width
        self.map_height = height
        self.population = np.zeros(self.map_size, dtype=np.int8)

    def set_population(self, popsize):
        pass

    def play(self):
        pass

    def pause(self):
        pass

    def visualize(self):
        pass
