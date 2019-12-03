from typing import List, Tuple, Dict

def find_crossings(wire1: List[Tuple], wire2: List[Tuple]) -> List[Dict]:
    """Return all crossing points with distance and steps.

    Find all coordinates where the given wires cross. For each point,
    determine the manhattan distance to the origin ('dist') and the combined
    running lengths of both wires to that point ('steps').

    Args:
        wire1 (List[Tuple]): First wire as a sequence of
            (direction, distance) tuples indicating where the wire
            runs and how far.
        wire2 (List[Tuple]): Second wire.

    Returns:
        List[Dict]: All crossing points with information about
            manhattan distance ('dist') and combined wire length ('steps').

    Example:

    >>> find_crossings([('U', 1), ('U', 1)])
    [{
        'crossing': (0, 1),
        'dist': 1,
        'steps': 2
    }]
    """
    crossings = []

    # collect wire1 coordinates
    wire1_coords = dict(get_wire_coordinates(wire1))

    # compare wire2 coordinates to find crossing points
    for coord, steps in get_wire_coordinates(wire2):
        if coord in wire1_coords:
            crossings.append({
                'crossing': coord,
                'dist': manhattan(coord),
                'steps': steps + wire1_coords[coord]})

    return crossings


def get_wire_coordinates(wire: List[Tuple]) -> Tuple[Tuple, int]:
    """Yield all positions on the grid covered by the wire."""
    i = 0
    pos = (0, 0)

    for direction, distance in wire:
        for _ in range(distance):
            i += 1
            pos = get_next_coord(pos, direction)
            yield pos, i


def get_next_coord(position: Tuple, direction: str) -> Tuple:
    """Return the position after taking one step in 'direction'."""
    steps = {
        'U': (0, 1),
        'D': (0, -1),
        'L': (-1, 0),
        'R': (1, 0)}

    return tuple([i + j for i, j in zip(position, steps[direction])])


def manhattan(coord: Tuple) -> int:
    """Return manhattan distance of coordinate from the origin."""
    return abs(coord[0]) + abs(coord[1])


def deserialize_wire(wire: str) -> List[Tuple]:
    """Parse the given string into a tuple representation."""
    return [(s[0], int(s[1:])) for s in wire.split(',')]

