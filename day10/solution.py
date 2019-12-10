"""Find and destroy visible asteroids."""

import sys
from asteroids import parse_input, find_best_position, find_nth_vaporized

if __name__ == '__main__':
    asteroids = parse_input(sys.stdin.read())
    position, count = find_best_position(asteroids)

    print('part 1:', count)
    print('part 2:', find_nth_vaporized(asteroids, position, 200))

