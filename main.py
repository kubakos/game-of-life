#!/usr/bin/env python3
import game

if __name__ == '__main__':
    x = game.GameOfLife()
    x.set_map_size(50, 170)
    x.set_population_density('high')
    x.start()
