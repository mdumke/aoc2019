"""Compute positions, velocity and periodicity of 4 celetial bodies."""

import sys
import numpy as np
from nbody import *

if __name__ == '__main__':
    original_pos = parse_input(sys.stdin.read().strip())

    pos = original_pos.copy()
    vel = np.zeros_like(pos)
    for _ in range(1000):
        update(pos, vel)
    print('part 1:', compute_total_energy(pos, vel))

    pos = original_pos.copy()
    vel = np.zeros_like(pos)
    print('part 2:', compute_recurrence_period(pos, vel))
