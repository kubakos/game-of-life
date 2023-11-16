import numpy as np
import time
import os


class GameOfLife:

    def __init__(self):
        self.map_size = [10, 10]
        self.population = np.zeros(self.map_size, dtype=np.int8)

    def get_map(self):
        return self.population

    def set_map_size(self, height=int, width=int):
        self.map_size = [height, width]
        self.population = np.zeros(self.map_size, dtype=np.int8)

    def set_population(self, population=np.ndarray):
        self.population = population

    def set_population_density(self, pd=str):
        if pd == 'low':
            self.population = np.random.randint(0, 3, self.map_size)
        elif pd == 'high':
            self.population = np.random.randint(0, 2, self.map_size)
        else:
            print("Population density is out of range!")

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
        if isinstance(self.population, np.ndarray):
            tmp_population = np.zeros(self.map_size, dtype=np.int8)
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
        else:
            print("Map's not right!")
