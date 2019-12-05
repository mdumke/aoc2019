"""Run test program on an Integer computer."""

import sys
from intcomputer import execute

def get_input():
    return [int(i) for i in sys.stdin.read().strip().split(',')]

if __name__ == '__main__':
    code = get_input()
    print(f'part 1: diagnostic code: {execute(code)[-1]}')
