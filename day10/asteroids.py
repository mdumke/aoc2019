import numpy as np
from tqdm import tqdm
from collections import defaultdict


def find_best_position(asteroids):
    """Return the position with highest visibility count."""
    counts = count_visible(asteroids)
    best_position = max(counts, key=counts.get)
    return best_position, counts[best_position]


def count_visible(positions):
    """Return number of positions in line of vision for each position."""
    counts = defaultdict(int)

    for source in tqdm(positions, ascii=True):
        for target in positions:
            if source == target:
                continue

            target_is_visible = True

            for obstacle in positions:
                if obstacle == source or obstacle == target:
                    continue

                if is_blocked(source, target, obstacle):
                    target_is_visible = False

            if target_is_visible:
                counts[source] += 1

    return dict(counts)


def is_blocked(source, target, obstacle):
    """Return True if target is visible from source, not blocked by obstacle."""
    dt = np.subtract(target, source)
    do = np.subtract(obstacle, source)

    # 1st condition: linear dependence of difference vectors
    if np.linalg.matrix_rank([dt, do]) == 2:
        return False

    # 2nd condition: obstacle must be between source and target
    return np.alltrue(np.sign(dt) == np.sign(do)) and \
           np.linalg.norm(do) < np.linalg.norm(dt)


def parse_input(asteroids):
    """Return a set of positions of all asteroids."""
    positions = set()

    for i, line in enumerate(asteroids.strip().split('\n')):
        for j, symbol in enumerate(line.strip()):
            if symbol == '#':
                positions.add((j, i))

    return positions

