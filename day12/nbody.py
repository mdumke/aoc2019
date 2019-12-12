import re
import numpy as np
from tqdm import tqdm
from itertools import combinations
from functools import reduce


def compute_recurrence_period(pos, vel):
    states = precompute_states(pos, vel, 400_000)
    periods = set([find_period(states[:, i]) for i in range(states.shape[1])])
    return reduce(lambda a, b: a * b // np.gcd(a, b), periods)


def find_period(values):
    i, j, boundary = 0, 1, 1

    while i <= len(values) // 2:
        if i == boundary:
            return i

        if values[i] == values[j]:
            i += 1
            j += 1
        elif i > 0:
            boundary += 1
            j = boundary
            i = 0
        else:
            j += 1
            boundary = j


def precompute_states(pos, vel, n):
    states = np.empty((n, pos.size + vel.size))
    for i in tqdm(range(n)):
        states[i] = np.r_[pos.flatten(), vel.flatten()]
        update(pos, vel)
    return states


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

