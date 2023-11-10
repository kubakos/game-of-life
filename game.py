import numpy as np


class GameOfLife:

    def __init__(self):
        self.map_height = 100
        self.map_width = 100
        self.map_size = [self.map_height, self.map_width]
        self.population = np.random.randint(0, 1, self.map_size)

    def set_map_size(self, height, width):
        self.map_height = height
        self.map_width = width
        self.population = np.random.randint(0, 1, self.map_size)

    def set_population(self, population):
        if population == 'random':
            self.population = np.random.randint(0, 2, self.map_size)
        elif isinstance(population, np.ndarray):
            self.population = population

    def play(self):
        pass

    def pause(self):
        pass

    def visualize(self):
        pass
