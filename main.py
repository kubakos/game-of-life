#!/usr/bin/env python3
import game

if __name__ == '__main__':
    x = game.GameOfLife()
    x.set_map_size(10, 40)
    x.set_population_density('high')
    x.start()
