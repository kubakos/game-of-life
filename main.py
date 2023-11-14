#!/usr/bin/env python3
import game

if __name__ == '__main__':
    x = game.GameOfLife()
    x.set_map_size(30, 100)
    x.set_density(1000)
    x.start()
