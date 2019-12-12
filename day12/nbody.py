import re
import numpy as np
from itertools import combinations


def update(pos, vel):
    # apply gravity
    for i, j in combinations(range(pos.shape[0]), 2):
        updates = np.sign(pos[i] - pos[j])
        vel[i] -= updates
        vel[j] += updates

    # apply velocity
    pos += vel


def compute_total_energy(pos, vel):
    pot = np.sum(np.abs(pos), axis=1)
    kin = np.sum(np.abs(vel), axis=1)
    return np.sum(pot * kin)


def parse_input(puzzle):
    return np.array([int(i) for i in re.findall('(-?\d+)', puzzle)])\
             .reshape(4, 3)
