"""Compute checksum and number of hops on an orbital map."""

import sys
from orbit import *

if __name__ == '__main__':
    orbit = parse_input(sys.stdin.read().strip())
    print('part 1', compute_checksum(orbit, 'COM'))
    print('part 2', count_orbital_transfers(orbit, 'YOU', 'SAN'))

