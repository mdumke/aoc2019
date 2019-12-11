from unittest import TestCase
from robot import Robot


class TestRun(TestCase):
    def test_single_step(self):
        # get one input, then output 1 (white) and 0 (right)
        code = [3, 20, 104, 1, 104, 0, 99]
        robot = Robot(code)
        robot.run()
        self.assertEqual(robot.position, (-1, 0))
        self.assertEqual(robot.orientation, 3)
        self.assertEqual(robot.grid[(0, 0)], 1)

