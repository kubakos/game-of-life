import numpy as np
import matplotlib.pyplot as plt
import time
import os


class GameOfLife:

    def __init__(self, height=100, width=100):
        self.generations = 10000
        self.map_size = [height, width]
        self.population = np.random.randint(0, 2, self.map_size)

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

    def run_in_terminal(self):
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
            print(self.population)
            print(gen)
            time.sleep(1/24)

    def plot(self):
        fig, ax = plt.subplots(self.population)
        for img in self.population:
            ax.clear()
            ax.imshow(img)
            plt.pause(0.1)
