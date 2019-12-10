import numpy as np
from collections import defaultdict
from itertools import groupby


def find_nth_vaporized(asteroids, position, n):
    """Return position of the nth asteroid to be vaporized."""
    groups = group_by_angle(asteroids, position)
    deleted = 0
    i = 0

    while deleted < n - 1:
        if groups[i]:
            groups[i].pop(0)
            deleted += 1
        i = (i + 1) % len(groups)

    return groups[i].pop(0)


def find_best_position(asteroids):
    """Return position and count for asteroid with highest visibility."""
    counts = {a: len(group_by_angle(asteroids, a)) for a in asteroids}
    best = max(counts, key=counts.get)
    return best, counts[best]


def group_by_angle(asteroids, position):
    """Return asteroids grouped by angle, then sorted by distance from position.

    Angle refers to the clockwise angle of the position-asteroid-vector
    relative to the vector that goes straigt upwards, i.e. (0, -1).

    Example:

    >>> group_by_angle(set([(2, 0), (1, 0), (0, 1)]), (0, 0))
    [[(1, 0), (2, 0)], [(0, 1)]]
    """
    def angle(asteroid):
        diff = np.subtract(asteroid, position)
        return (360 - np.rad2deg(np.arctan2(*-diff))) % 360

    def dist(asteroid):
        diff = np.subtract(asteroid, position)
        return np.linalg.norm(diff)

    asteroids = [a for a in asteroids if a != position]
    asteroids.sort(key=lambda a: (angle(a), dist(a)))

    return [list(group) for _, group in groupby(asteroids, angle)]


def parse_input(asteroids):
    """Return a set of positions of all asteroids."""
    positions = set()

    for i, line in enumerate(asteroids.strip().split('\n')):
        for j, symbol in enumerate(line.strip()):
            if symbol == '#':
                positions.add((j, i))

    return positions

