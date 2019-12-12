import sys
import numpy as np
from nbody import *

if __name__ == '__main__':
    pos = parse_input(sys.stdin.read().strip())
    vel = np.zeros_like(pos)

    for _ in range(1000):
        update(pos, vel)

    print('part 1:', compute_total_energy(pos, vel))
