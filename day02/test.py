from unittest import TestCase
from intcomputer import execute

class TestExecute(TestCase):
    def test_sample_1(self):
        code = [1, 0, 0, 0, 99]
        execute(code)
        self.assertEqual(code, [2, 0, 0, 0, 99])

    def test_sample_2(self):
        code = [2, 3, 0, 3, 99]
        execute(code)
        self.assertEqual(code, [2, 3, 0, 6, 99])

    def test_sample_3(self):
        code = [2, 4, 4, 5, 99, 0]
        execute(code)
        self.assertEqual(code, [2, 4, 4, 5, 99, 9801])

    def test_sample_4(self):
        code = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        execute(code)
        self.assertEqual(code, [30, 1, 1, 4, 2, 5, 6, 0, 99])
