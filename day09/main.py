"""Run code on the updated integer computer."""

import sys
from intcomputer import Intcomputer


if __name__ == '__main__':
    code = [int(n) for n in sys.stdin.readline().strip().split(',')]

    computer = Intcomputer(code)
    _, keycode = computer.execute(1)
    print('part1', keycode)

    computer = Intcomputer(code)
    _, coordinates = computer.execute(2)
    print('part 2', coordinates)
