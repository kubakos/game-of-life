import numpy as np


class GameOfLife:

    def __init__(self, height=100, width=100):
        self.map_size = [height, width]
        self.population = np.zeros(self.map_size, np.int8)

    def get_map(self):
        return self.population

    def set_map_size(self, height, width):
        self.map_size = [height, width]

    def set_population(self, population):
        if population == 'random':
            self.population = np.random.randint(0, 2, self.map_size)
        elif isinstance(population, np.ndarray):
            self.population = population

    def is_alive(self, cell):
        neighbours = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i or j != 0) & (cell[0] + i >= 0) & (cell[1] + j >= 0):
                    neighbours += self.population[cell[0] + i, cell[1] + j]

        if self.population[cell[0], cell[1]] == 1:
            if neighbours < 2:
                self.population[cell[0], cell[1]] = 0
            elif neighbours > 3:
                self.population[cell[0], cell[1]] = 0
        elif self.population[cell[0], cell[1]] == 0:
            if neighbours == 3:
                self.population[cell[0], cell[1]] = 1

    def play(self):
        pass

    def pause(self):
        pass

    def visualize(self):
        pass
