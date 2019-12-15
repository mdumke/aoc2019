from collections import deque
from intcomputer import Intcomputer

WALL = 0
EMPTY = 1
OXYGEN = 2
MOVES = {(1, 0): 1, (-1, 0): 2, (0, -1): 3, (0, 1): 4}


class Droid:
    """Machine to explore an area.

    The droid will run an intcode program that produces environment
    signals given steps in different directions. It can explore the
    area to build up an internal representation, then use this model
    to find the optimal path to an oxygen source and the furthest point
    from any given position.
    """
    def __init__(self, code):
        self.cpu = Intcomputer(code)
        self.model = {}
        self.routes = {}
        self.position = (0, 0)

    def explore(self):
        """Build a model of the environment by moving around."""
        closed = set()
        fringe = deque()
        fringe.appendleft(((0, 0), None))
        while fringe:
            position, parent = fringe.pop()
            self.routes[position] = parent
            closed.add(position)
            signal = self.move_to(position)
            self.model[position] = signal

            if signal == WALL:
                continue
            for neighbor in self.get_neighbors(position):
                if neighbor not in closed:
                    fringe.appendleft((neighbor, position))

    def find_oxygen(self):
        """Return coordinates and path of oxygen systems's position."""
        for position, signal in self.model.items():
            if signal == OXYGEN:
                oxygen = position
        return oxygen, self.navigate((0, 0), oxygen)

    def find_max_dist_from(self, pos):
        """Return the position furthest away from the specified position."""
        max_dist = -1
        for coord, signal in self.model.items():
            if signal != WALL:
                max_dist = max(max_dist, len(self.navigate(coord, pos)) - 1)
        return max_dist

    def get_neighbors(self, position):
        """Return all four adjacent positions."""
        return [self.add(position, move) for move in MOVES.keys()]

    def move_to(self, target):
        """Return the last signal observed when trying to reach target."""
        if self.position == target:
            return EMPTY
        path = self.navigate(self.position, target)
        walk = self.create_walk(path)
        for step in walk:
            signal = self.cpu.execute(MOVES[step])[1]
            if signal == WALL:
                break
            self.position = self.add(self.position, step)
        return signal

    def navigate(self, pos1, pos2):
        """Return path from pos1 to pos2."""
        pos2_path = self.find_path(pos2)
        pos1_path = self.find_path(pos1)
        diff = set(pos2_path) - set(pos1_path)
        path = []
        for coord in pos2_path:
            path.append(coord)
            if coord not in diff:
                break
        i = pos1_path.index(coord)
        path.extend(reversed(pos1_path[:i]))
        path.reverse()
        return path

    def find_path(self, target):
        """Return path from target to center."""
        path = []
        current = target
        while current is not None:
            path.append(current)
            current = self.routes[current]
        return path

    def create_walk(self, path):
        """Return a sequence of steps that result in following the path."""
        return [self.subtract(p2, p1) for p1, p2 in zip(path, path[1:])]

    def subtract(self, pos1, pos2):
        return (pos1[0] - pos2[0], pos1[1] - pos2[1])

    def add(self, pos1, pos2):
        return (pos1[0] + pos2[0], pos1[1] + pos2[1])

