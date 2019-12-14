"""Compute chemical reactions to produce fuel from raw inputs."""

import sys
from fuel import parse_input, get_required_ore, max_fuel


if __name__ == '__main__':
    puzzle = parse_input(sys.stdin.read().strip())

    print('part 1:', get_required_ore(*puzzle))
    print('part 2:', max_fuel(*puzzle))

