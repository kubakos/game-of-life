import numpy as np
import time
import os


class GameOfLife:

    def __init__(self):
        self.map_size = [10, 10]
        self.population_density = 2
        self.population = np.random.randint(
            0, self.population_density, self.map_size)

    def get_map(self):
        return self.population

    def set_map_size(self, height, width):
        if isinstance(height, int) & isinstance(width, int):
            self.map_size = [height, width]
            self.population = np.random.randint(
                0, self.population_density, self.map_size)
            print("Map size set!")
        else:
            print("Map size couldn't be set!")

    def set_population(self, population):
        if isinstance(population, np.ndarray):
            self.population = population
            print("Population map set!")
        else:
            print("Population map couldn't be set!")

    def set_density(self, pd):
        if isinstance(pd, int):
            self.population_density = pd
            self.population = np.random.randint(
                0, self.population_density, self.map_size)
            print("Population density set!")
        else:
            print("Population density couldn't be set!")

    def is_alive(self, cell):
        neighbours = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i or j != 0) & (0 <= cell[0] + i <= self.map_size[0] - 1) & (0 <= cell[1] + j <= self.map_size[1] - 1):
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
        tmp_population = np.zeros(self.map_size)
        generation = 0
        while True:
            for i in range(self.map_size[0]):
                for j in range(self.map_size[1]):
                    if self.is_alive([i, j]) is True:
                        tmp_population[i, j] = 1
                    else:
                        tmp_population[i, j] = 0
            os.system('clear')
            generation += 1
            self.population = tmp_population
            print(*self.transform_to_str(self.population), sep='\n')
            print(generation)
            time.sleep(1/30)
