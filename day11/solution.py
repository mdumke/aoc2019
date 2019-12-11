"""Operate a hull painting robot to paint the spacecraft."""

import sys
from robot import Robot


if __name__ == '__main__':
    code = [int(i) for i in sys.stdin.readline().split(',')]

    robot = Robot(code)
    robot.run()
    print('part 1:', len(robot.grid))

    robot = Robot(code, 1)
    robot.run()
    print(f'part 2:\n{robot.draw()}')
