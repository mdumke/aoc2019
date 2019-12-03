def step(position, direction):
    steps = {
        'U': (0, 1),
        'D': (0, -1),
        'L': (-1, 0),
        'R': (1, 0)}

    return tuple([i + j for i, j in zip(position, steps[direction])])


def get_wire_coordinates(wire):
    pos = (0, 0)

    for direction, distance in wire:
        for _ in range(distance):
            pos = step(pos, direction)
            yield pos


def manhattan(coord):
    return abs(coord[0]) + abs(coord[1])


def deserialize_wire(wire):
    return [(s[0], int(s[1:])) for s in wire.split(',')]


def find_crossing(wire1, wire2):
    crossings = list()
    wire1_coords = set()

    # collect wire1 coordinates
    for coord in get_wire_coordinates(wire1):
        wire1_coords.add(coord)

    # compare wire2 coordinates to find crossing points
    for coord in get_wire_coordinates(wire2):
        if coord in wire1_coords:
            crossings.append(coord)

    # return crossing with minimum MH distance
    if not crossings:
        return

    return min(crossings, key=manhattan)

