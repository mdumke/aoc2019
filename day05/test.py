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

    def test_save(self):
        code = [3, 0, 99]
        execute(code)
        self.assertEqual(code, [1, 0, 99])

    def test_read(self):
        code = [4, 2, 99]
        output = execute(code)
        self.assertEqual(code, [4, 2, 99])
        self.assertEqual(output, [99])

    def test_modes_add_a(self):
        code = [1101, 4, 5, 3, 99]
        execute(code)
        self.assertEqual(code, [1101, 4, 5, 9, 99])

    def test_modes_add_b(self):
        code = [101, 4, 4, 3, 99]
        execute(code)
        self.assertEqual(code, [101, 4, 4, 103, 99])

    def test_modes_add_c(self):
        code = [1001101, 4, 4, 3, 99]
        execute(code)
        self.assertEqual(code, [1001101, 4, 4, 8, 99])

    def test_modes_mul_1(self):
        code = [1102, 4, 5, 3, 99]
        execute(code)
        self.assertEqual(code, [1102, 4, 5, 20, 99])

    def test_modes_mul_2(self):
        code = [1001102, 4, 5, 3, 99]
        execute(code)
        self.assertEqual(code, [1001102, 4, 5, 20, 99])

    def test_modes_read(self):
        code = [104, 5, 99]
        output = execute(code)
        self.assertEqual(code, [104, 5, 99])
        self.assertEqual(output, [5])

    def test_sample_5(self):
        code = [1101, 100, -1, 4, 0]
        execute(code)
        self.assertEqual(code, [1101, 100, -1, 4, 99])
