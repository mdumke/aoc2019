import math
from collections import defaultdict, deque


def fuel_from_ore(reactions, batch_sizes, capacity=10**12):
    """Return Fuel units to produce under ore capacity constraints."""
    lo, hi = 0, capacity

    while lo < hi - 1:
        fuel = lo + (hi - lo) // 2
        ore = ore_per_fuel(reactions, batch_sizes, fuel)

        if ore <= capacity:
            lo = fuel
        else:
            hi = fuel

    return lo


def ore_per_fuel(reactions, batch_sizes, amount=1):
    """Return ORE necessary to produce min quantity of target material."""
    ore = 0
    overhead = defaultdict(int)

    fringe = deque()
    fringe.append(('FUEL', amount))

    while fringe:
        target, target_units = fringe.pop()

        if target == 'ORE':
            ore += target_units
            continue

        for source, source_units in reactions[target].items():
            assert target_units % batch_sizes[target] == 0
            needed = target_units // batch_sizes[target] * source_units

            if overhead[source]:
                reuse = min(overhead[source], needed)
                overhead[source] -= reuse
                needed -= reuse

            source_batches = math.ceil(needed / batch_sizes[source])
            total_units = batch_sizes[source] * source_batches

            if total_units > needed:
                overhead[source] += total_units - needed

            fringe.append((source, total_units))

    return ore


def parse_input(puzzle):
    """Return reactions-graph and batch sizes for each material."""
    batch_sizes = {'ORE': 1}
    reactions = {}

    for line in puzzle.split('\n'):
        sources, target = line.split(' => ')
        batch_size, target = target.split(' ')
        batch_sizes[target] = int(batch_size)
        reactions[target] = {}

        for source in sources.split(','):
            quantity, name = source.strip().split(' ')
            reactions[target][name] = int(quantity)

    return reactions, batch_sizes

