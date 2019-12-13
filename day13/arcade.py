"""An arcade running an intcode game."""

import numpy as np
from intcomputer import Intcomputer

BLOCK = 2
PADDLE = 3
BALL = 4


class Arcade:
    def __init__(self, code, mode=1):
        self.cpu = Intcomputer(code)
        self.cpu.memory[0] = mode
        self.tiles = np.empty((21, 40), dtype=np.int)
        self.score = 0
        self.x_ball = -1
        self.x_paddle = -1

    def play(self):
        state = 'INIT'

        while state != 'HALT':
            state, output = self.step(state)
            self.update(output)

    def step(self, state):
        output = []

        if state == 'WAITING':
            move = np.sign(self.x_ball - self.x_paddle)
            state, i = self.cpu.execute(move)
            output.append(i)

        while True:
            state, i = self.cpu.execute()
            if state != 'OUTPUT':
                break
            output.append(i)

        return state, output

    def update(self, output):
        for x, y, value in np.reshape(output, (-1, 3)):
            if x == -1 and y == 0:
                self.score = value
                continue

            if value == BALL:
                self.x_ball = x
            if value == PADDLE:
                self.x_paddle = x

            self.tiles[y, x] = value


if __name__ == '__main__':
    code = np.loadtxt('input.txt', delimiter=',', dtype=np.int)

    arcade = Arcade(code, mode=1)
    arcade.play()
    print('part 1:', np.sum(arcade.tiles == BLOCK))

    arcade = Arcade(code, mode=2)
    arcade.play()
    print('part 2:', arcade.score)

