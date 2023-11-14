import numpy as np
import time
import os


class GameOfLife:

    def __init__(self, height=100, width=100):
        self.generations = 10000
        self.map_size = [height, width]
        self.population_density = 2
        self.population = np.random.randint(
            0, self.population_density, self.map_size)

    def get_map(self):
        return self.population

    def set_map_size(self, height, width):
        if isinstance(height, int) & isinstance(width, int):
            self.map_size = [height, width]

    def set_population(self, population):
        if isinstance(population, np.ndarray):
            self.population = population

    def set_generations(self, gens):
        if isinstance(gens, int):
            self.generations = gens

    def set_density(self, pd):
        self.population_density = pd

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
        else:
            if neighbours == 3:
                return True
            else:
                return False

    def transform_to_str(self, population):
        transformed = []
        string = ''
        for row in population:
            for cell in row:
                if cell == 1:
                    string += '\u2588'
                else:
                    string += ' '
            transformed.append([string])
            string = ''
        return transformed

    def start(self):
        tmp_population = np.zeros(self.map_size, np.int8)
        for gen in range(self.generations):
            for i in range(self.map_size[0] - 1):
                for j in range(self.map_size[1] - 1):
                    if self.is_alive([i, j]) is True:
                        tmp_population[i, j] = 1
                    else:
                        tmp_population[i, j] = 0
            os.system('clear')
            self.population = tmp_population
            print(*self.transform_to_str(self.population), sep='\n')
            print(gen)
            time.sleep(1/30)
