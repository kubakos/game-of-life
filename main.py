#!/usr/bin/python3
import game

if __name__ == '__main__':
    x = game.GameOfLife(10, 10)
    x.set_population('random')
    x.start(100)
