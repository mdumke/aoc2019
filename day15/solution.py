"""Droid exploring an area running an intcode program."""

import sys
from droid import Droid

if __name__ == '__main__':
    code = [int(i) for i in sys.stdin.readline().split(',')]
    droid = Droid(code)
    droid.explore()
    position, path = droid.find_oxygen()

    print('part 1', len(path) - 1)
    print('part 2', droid.find_max_dist_from(position))

