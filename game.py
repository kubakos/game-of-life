import numpy as np
import time


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
                return False
            elif neighbours > 3:
                return False
            else:
                return True
        elif self.population[cell[0], cell[1]] == 0:
            if neighbours == 3:
                return True
            else:
                return False

    def visualize(self):
        pass

    def start(self, generations):
        tmp_pop = np.zeros(self.map_size, np.int8)
        for gen in range(generations):
            for i in range(self.map_size[0]):
                for j in range(self.map_size[1]):
                    if self.is_alive([i, j]) is True:
                        tmp_pop[i, j] = 1
                    else:
                        tmp_pop[i, j] = 0
            self.population = tmp_pop
            print(self.get_map())
            time.sleep(1)
