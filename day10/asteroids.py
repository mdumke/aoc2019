import numpy as np
from collections import defaultdict


def find_best_position(asteroids):
    """Return the position with highest visibility count."""
    counts = count_visible(asteroids)
    best_position = max(counts, key=counts.get)
    return best_position, counts[best_position]


def count_visible(asteroids):
    """Return number of visible neighbors for each asteroid."""
    counts = defaultdict(int)

    for asteroid in asteroids:
        for neighbor in asteroids:
            if neighbor == asteroid:
                continue

            if is_visible(neighbor, asteroid, asteroids):
                counts[asteroid] += 1

    return dict(counts)


def is_visible(target, position, asteroids):
    """Return True if target is visible from given position."""
    # strategy: walk from postion to target in smallest possible steps
    # that are still integers. If an asteroid is in the way, return False.
    dx, dy = np.subtract(target, position)

    divisor = np.gcd(dx, dy)
    dx = dx // divisor
    dy = dy // divisor

    current = tuple(np.add(position, [dx, dy]))

    while not np.alltrue(current == target):
        if current in asteroids:
            return False
        current = tuple(np.add(current, [dx, dy]))

    return True


def parse_input(asteroids):
    """Return a set of positions of all asteroids."""
    positions = set()

    for i, line in enumerate(asteroids.strip().split('\n')):
        for j, symbol in enumerate(line.strip()):
            if symbol == '#':
                positions.add((j, i))

    return positions

