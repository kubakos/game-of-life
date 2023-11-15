#!/usr/bin/env python3
import game

if __name__ == '__main__':
    x = game.GameOfLife()
    x.set_map_size(45, 170)
    x.set_density(3)
    x.start()
