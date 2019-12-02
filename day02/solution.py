#!/usr/bin/env python

"""Execute code on an intcomputer.

usage: ./solution.py < input.txt
"""

import sys
from intcomputer import execute

def get_input():
    return [int(i) for i in sys.stdin.read().strip().split(',')]


def solve_part_1(code):
    """Execute code with given noun and verb."""
    code = code[:]
    code[1:3] = [12, 2]
    execute(code)
    print(f'part 1: {code[0]}')


def solve_part_2(code):
    """Find noun and verb to produce 19690720."""
    target = 19690720

    for noun in range(100):
        for verb in range(100):
            test_code = code[:]
            test_code[1:3] = [noun, verb]
            execute(test_code)

            if test_code[0] == target:
                print(f'part 2: {100 * noun + verb}')


if __name__ == '__main__':
    code = get_input()
    solve_part_1(code)
    solve_part_2(code)

