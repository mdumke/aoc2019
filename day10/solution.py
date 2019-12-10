import sys
from asteroids import parse_input, find_best_position

if __name__ == '__main__':
    asteroids = parse_input(sys.stdin.read())
    print(find_best_position(asteroids))
