import sys
from orbit import *

if __name__ == '__main__':
    serialized_map = sys.stdin.read().strip()
    orbit = parse_input(serialized_map)
    print(compute_checksum(orbit, 'COM'))
