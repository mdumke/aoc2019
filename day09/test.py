from unittest import TestCase
from intcomputer import Intcomputer


class TestIntcomputer(TestCase):
    def test_adjust_relative_mode_0(self):
        code = [9, 3, 99, 10]
        computer = Intcomputer(code)
        computer.execute()
        self.assertEqual(computer.relative_base, 10)

    def test_adjust_relative_mode_1(self):
        code = [109, 3, 99]
        computer = Intcomputer(code)
        computer.execute()
        self.assertEqual(computer.relative_base, 3)

    def test_adjust_relative_mode_2(self):
        code = [209, -1, 99, 20]
        computer = Intcomputer(code)
        computer.relative_base = 4
        computer.execute()
        self.assertEqual(computer.relative_base, 24)

    def test_add_mode_21(self):
        code = [2101, 5, -5, 6, 99, 11]
        computer = Intcomputer(code)
        computer.relative_base = 10
        computer.execute()
        self.assertEqual(computer.memory[:7], [2101, 5, -5, 6, 99, 11, 16])

    def test_add_mode_12(self):
        code = [1201, -5, 5, 3, 99, 11]
        computer = Intcomputer(code)
        computer.relative_base = 10
        computer.execute()
        self.assertEqual(computer.memory[:6], [1201, -5, 5, 16, 99, 11])

    def test_mul_mode_21(self):
        code = [2102, 2, -5, 3, 99, 6]
        computer = Intcomputer(code)
        computer.relative_base = 10
        computer.execute()
        self.assertEqual(computer.memory[:6], [2102, 2, -5, 12, 99, 6])

    def test_mul_mode_12(self):
        code = [1202, -5, 2, 3, 99, 6]
        computer = Intcomputer(code)
        computer.relative_base = 10
        computer.execute()
        self.assertEqual(computer.memory[:6], [1202, -5, 2, 12, 99, 6])

    def test_jump_if_true_mode_2_a(self):
        code = [1205, 3, 4, 0, 99, 1]
        computer = Intcomputer(code)
        computer.relative_base = 2
        computer.execute()
        self.assertTrue(True)

    def test_jump_if_true_mode_2_b(self):
        code = [205, 3, 6, 0, 99, 1, 4]
        computer = Intcomputer(code)
        computer.relative_base = 2
        computer.execute()
        self.assertTrue(True)

    def test_jump_if_false_mode_2(self):
        code = [1206, 3, 4, 1, 99, 0]
        computer = Intcomputer(code)
        computer.relative_base = 2
        computer.execute()
        self.assertTrue(True)

    def test_io(self):
        code = [3, 9, 1002, 9, 2, 10, 4, 10, 99, 0, 0]
        computer = Intcomputer(code)
        status, output = computer.execute(3)
        self.assertEqual(status, 'OUTPUT')
        self.assertEqual(output, 6)

    def test_sample_1(self):
        code = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100,
                16, 101, 1006, 101, 0, 99]
        computer = Intcomputer(code)
        output = []
        while True:
            status, out = computer.execute()
            if status == 'HALT': break
            output.append(out)
        self.assertEqual(code, output)

    def test_sample_2(self):
        code = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]
        computer = Intcomputer(code)
        output = []
        while True:
            status, out = computer.execute()
            if status == 'HALT': break
            output.append(out)
        self.assertEqual(len(str(output[0])), 16)

    def test_sample_3(self):
        code = [104, 1125899906842624, 99]
        computer = Intcomputer(code)
        status, out = computer.execute()
        self.assertEqual(out, 1125899906842624)

    def test_203_input(self):
        code = [203, -6, 99, -1, -1]
        computer = Intcomputer(code)
        computer.relative_base = 10
        status, out = computer.execute(1)
        self.assertEqual(computer.memory[:5], [203, -6, 99, -1, 1])

    def test_21107_less_than(self):
        code = [21107, 1, 2, -5, 99, -1]
        computer = Intcomputer(code)
        computer.relative_base = 10
        computer.execute()
        self.assertEqual(computer.memory[:6], [21107, 1, 2, -5, 99, 1])

