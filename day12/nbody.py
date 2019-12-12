import re
import numpy as np
from tqdm import tqdm
from itertools import combinations
from functools import reduce


def compute_recurrence_period(pos, vel):
    """Return the timesteps after which the original state reoccurs."""
    # pre-compute enough states, then determine the period length
    # for each body in each dimension for both position and velocity,
    # the overall period is the least common multiple of the individuals.
    states = precompute_states(pos, vel, 400_000)
    return lcm(set(find_period(states[:, i]) for i in range(states.shape[1])))


def lcm(values):
    """Return the least common multiple of all given values."""
    return reduce(lambda a, b: a * b // np.gcd(a, b), values)


def find_period(values):
    """Return the length of the recurrence period in the values."""
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
    """Return the next n states."""
    states = np.empty((n, pos.size + vel.size))
    for i in tqdm(range(n)):
        states[i] = np.r_[pos.flatten(), vel.flatten()]
        update(pos, vel)
    return states


def update(pos, vel):
    """Mutate position and velocity values for timestep."""
    # apply gravity
    for i, j in combinations(range(pos.shape[0]), 2):
        updates = np.sign(pos[i] - pos[j])
        vel[i] -= updates
        vel[j] += updates

    # apply velocity
    pos += vel


def compute_total_energy(pos, vel):
    """Return overall energy (potential and kinetic) of the system."""
    pot = np.sum(np.abs(pos), axis=1)
    kin = np.sum(np.abs(vel), axis=1)
    return np.sum(pot * kin)


def parse_input(puzzle):
    """Return a matrix representation of the puzzle input."""
    return np.array([int(i) for i in re.findall('(-?\d+)', puzzle)])\
             .reshape(4, 3)

