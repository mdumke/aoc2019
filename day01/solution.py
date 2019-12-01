#!/usr/bin/env python

"""Compute total fuel required to launch a spacecraft."""

import sys
from lib import compute_module_fuel_naive, compute_module_fuel


def solve_part_1(masses):
    total = sum([compute_module_fuel_naive(m) for m in masses])
    print(f'part 1: {total}')


def solve_part_2(masses):
    total = sum([compute_module_fuel(m) for m in masses])
    print(f'part 2: {total}')


def get_input():
    return [int(n) for n in sys.stdin.read().strip().split('\n')]


if __name__ == '__main__':
    masses = get_input()
    solve_part_1(masses)
    solve_part_2(masses)

