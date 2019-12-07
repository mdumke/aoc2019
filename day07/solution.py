"""Compute maximum signal to generate through a chain of amplifiers."""

import sys
from thruster import find_max_signal

if __name__ == '__main__':
    code = [int(n) for n in sys.stdin.readline().split(',')]
    print('part 1', find_max_signal(code, [0, 1, 2, 3, 4]))
    print('part 2', find_max_signal(code, [5, 6, 7, 8, 9]))

