"""Run code on the updated integer computer."""

import sys
from intcomputer import Intcomputer


if __name__ == '__main__':
    code = [int(n) for n in sys.stdin.readline().strip().split(',')]

    print('part 1:', Intcomputer(code).execute(1)[1])
    print('part 2:', Intcomputer(code).execute(2)[1])
