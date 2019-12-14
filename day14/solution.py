import sys
from fuel import parse_input, ore_per_fuel_unit


if __name__ == '__main__':
    reactions, batch_sizes = parse_input(sys.stdin.read().strip())
    print(ore_per_fuel_unit(reactions, batch_sizes))

