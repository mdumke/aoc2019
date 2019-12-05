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
        execute(code, iter([1]))
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

    def test_jump_if_true_mode_00_true(self):
        code = [5, 2, 3, 99]
        execute(code)
        self.assertEqual(code, [99, 2, 3, 99])

    def test_jump_if_true_mode_00_false(self):
        code = [5, 2, 0, 99]
        execute(code)
        self.assertEqual(code, [5, 2, 0, 99])

    def test_jump_if_true_mode_01_true(self):
        code = [105, 3, 4, 0, 99]
        execute(code)
        self.assertEqual(code, [99, 3, 4, 0, 99])

    def test_jump_if_true_mode_11_true(self):
        code = [101105, 1, 99]
        execute(code)
        self.assertEqual(code, [99, 1, 99])

    def test_jump_if_false_mode_00_false(self):
        code = [6, 3, 4, 0, 99]
        execute(code)
        self.assertEqual(code, [99, 3, 4, 0, 99])

    def test_jump_if_false_mode_00_true(self):
        code = [6, 4, 0, 99, 1]
        execute(code)
        self.assertEqual(code, [6, 4, 0, 99, 1])

    def test_jump_if_false_mode_01_false(self):
        code = [106, 0, 4, 0, 99]
        execute(code)
        self.assertEqual(code, [99, 0, 4, 0, 99])

    def test_jump_if_false_mode_11_false(self):
        code = [1001106, 0, 99]
        execute(code)
        self.assertEqual(code, [99, 0, 99])

    def test_less_than_mode_00_true(self):
        code = [7, 5, 6, 7, 99, 1, 2, -1]
        execute(code)
        self.assertEqual(code, [7, 5, 6, 7, 99, 1, 2, 1])

    def test_less_than_mode_11_false(self):
        code = [10001107, 10, -10, 5, 99, -1]
        execute(code)
        self.assertEqual(code, [10001107, 10, -10, 5, 99, 0])

    def test_equals_mode_00_true(self):
        code = [8, 5, 6, 7, 99, 3, 3, -1]
        execute(code)
        self.assertEqual(code, [8, 5, 6, 7, 99, 3, 3, 1])

    def test_equals_mode_11_false(self):
        code = [8, -1, -2, 5, 99, -1]
        execute(code)
        self.assertEqual(code, [8, -1, -2, 5, 99, 0])

    def test_sample_6_input_0(self):
        code = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
        output = execute(code, iter([0]))
        self.assertEqual(output, [0])

    def test_sample_6_input_8(self):
        code = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
        output = execute(code, iter([8]))
        self.assertEqual(output, [1])

    def test_sample_7_0lt8(self):
        code = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
        output = execute(code, iter([0]))
        self.assertEqual(output, [1])

    def test_sample_7_9lt8(self):
        code = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
        output = execute(code, iter([9]))
        self.assertEqual(output, [0])

    def test_sample_8_0eq8(self):
        code = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
        output = execute(code, iter([0]))
        self.assertEqual(output, [0])

    def test_sample_8_1eq8(self):
        code = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
        output = execute(code, iter([8]))
        self.assertEqual(output, [1])

    def test_sample_9_0lt8(self):
        code = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
        output = execute(code, iter([0]))
        self.assertEqual(output, [1])

    def test_sample_9_9lt8(self):
        code = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
        output = execute(code, iter([9]))
        self.assertEqual(output, [0])

    def test_sample_10_0(self):
        code = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
        output = execute(code, iter([0]))
        self.assertEqual(output, [0])

    def test_sample_10_1(self):
        code = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
        output = execute(code, iter([1]))
        self.assertEqual(output, [1])

    def test_sample_11_0(self):
        code = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
        output = execute(code, iter([0]))
        self.assertEqual(output, [0])

    def test_sample_11_1(self):
        code = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
        output = execute(code, iter([1]))
        self.assertEqual(output, [1])

    def test_io(self):
        code = [3, 9, 1002, 9, 2, 10, 4, 10, 99, 0, 0]
        output = execute(code, iter([3]))
        self.assertEqual(output, [6])
