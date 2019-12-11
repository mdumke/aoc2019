from collections import defaultdict
from operator import itemgetter
from intcomputer import Intcomputer


class Robot:
    def __init__(self, code, initial_color=0):
        self.computer = Intcomputer(code)
        self.grid = defaultdict(int)
        self.grid[(0, 0)] = initial_color
        self.orientation = 0
        self.position = (0, 0)

    def run(self):
        """Executes program and manages IO operations.

        Assumes that the program always follows the same pattern: take
        exactly one input, then output exactly two values (or halt)
        """
        while True:
            state, color = self.computer.execute(self.grid[self.position])

            if state == 'OUTPUT':
                self.grid[self.position] = color

            if state == 'HALT':
                break

            direction = self.computer.execute()[1]
            self.move(direction)

    def move(self, direction):
        """Set new position after move in given direction."""
        update = -1 if direction == 0 else 1
        self.orientation = (self.orientation + update) % 4
        step = [(0, 1), (1, 0), (0, -1), (-1, 0)][self.orientation]
        self.position = (self.position[0] + step[0], self.position[1] + step[1])

    def draw(self):
        """Return a string representation of the currently painted panels."""
        w_min = min(self.grid, key=itemgetter(0))[0]
        w_max = max(self.grid, key=itemgetter(0))[0]
        h_min = min(self.grid, key=itemgetter(1))[1]
        h_max = max(self.grid, key=itemgetter(1))[1]

        res = ''
        for j in range(h_max, h_min - 1, -1):
            for i in range(w_min, w_max + 1):
                res += ' ' if self.grid[(i, j)] == 0 else '█'
            res += '\n'

        return res

