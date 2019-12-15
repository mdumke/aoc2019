import sys
from collections import deque
from intcomputer import Intcomputer

WALL = 0
EMPTY = 1
OXYGEN = 2
MOVES = {(1, 0): 1, (-1, 0): 2, (0, -1): 3, (0, 1): 4}

class Droid:
    def __init__(self, code):
        self.cpu = Intcomputer(code)
        self.routes = {}
        self.position = (0, 0)

    def find_target(self):
        routes = {}
        closed = set()
        fringe = deque()
        fringe.appendleft(((0, 0), None))

        while fringe:
            position, parent = fringe.pop()
            self.routes[position] = parent
            closed.add(position)

            signal = self.move_to(position)

            if signal == OXYGEN:
                break
            if signal == WALL:
                continue

            for neighbor in self.get_neighbors(position):
                if neighbor in closed:
                    continue

                fringe.appendleft((neighbor, position))

        return self.find_path(self.position)

    def move_to(self, target):
        if self.position == target:
            return EMPTY

        path = [*self.find_path(self.position)[:-1],
                *reversed(self.find_path(target))]
        walk = self.create_walk(path)

        for step in walk:
            signal = self.cpu.execute(MOVES[step])[1]
            if signal == WALL:
                break
            self.position = self.add(self.position, step)

        return signal

    def find_path(self, target):
        path = []
        current = target
        while current is not None:
            path.append(current)
            current = self.routes[current]
        return path

    def create_walk(self, path):
        return [self.subtract(p2, p1) for p1, p2 in zip(path, path[1:])]

    def get_neighbors(self, position):
        return [self.add(self.position, move) for move in MOVES.keys()]

    def subtract(self, pos1, pos2):
        return (pos1[0] - pos2[0], pos1[1] - pos2[1])

    def add(self, pos1, pos2):
        return (pos1[0] + pos2[0], pos1[1] + pos2[1])


if __name__ == '__main__':
    code = [int(i) for i in sys.stdin.readline().split(',')]
    droid = Droid(code)
    path_to_oxygen = droid.find_target()
    print('part 1', len(path_to_oxygen) - 1)


