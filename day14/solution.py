"""Compute chemical reactions to produce fuel from raw inputs."""

import sys
from fuel import parse_input, ore_per_fuel, fuel_from_ore


if __name__ == '__main__':
    puzzle = parse_input(sys.stdin.read().strip())

    print('part 1:', ore_per_fuel(*puzzle))
    print('part 2:', fuel_from_ore(*puzzle))

