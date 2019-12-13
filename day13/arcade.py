import sys
import numpy as np
from intcomputer import Intcomputer
from functools import reduce

BLOCK = 2


class Arcade:
    def __init__(self, code):
        self.tiles = self.compute_tiles(code)

    def compute_tiles(self, code):
        computer = Intcomputer(code)
        output = []
        while True:
            state, digit = computer.execute()
            if state == 'HALT':
                break
            output.append(digit)
        return [tuple(row) for row in np.reshape(output, (-1, 3))]

    def count_blocks(self):
        return reduce(lambda acc, tile: acc + int(tile[2] == BLOCK), self.tiles, 0)







if __name__ == '__main__':
    arcade = Arcade([int(i) for i in sys.stdin.readline().split(',')])
    print(arcade.count_blocks())

