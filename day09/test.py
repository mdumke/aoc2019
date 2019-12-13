from unittest import TestCase
from intcomputer import Intcomputer

class TestIntcomputer(TestCase):
    def test_command_1(self):
        code = [1, 5, 6, 7, 99, 2, 3, 0]
        computer = Intcomputer(code)
        computer.execute()
        self.assertEqual(computer.memory[:8], [1, 5, 6, 7, 99, 2, 3, 5])

    def test_command_101(self):
        code = [101, 10, 5, 6, 99, 5, 0]
        computer = Intcomputer(code)
        computer.execute()
        self.assertEqual(computer.memory[:7], [101, 10, 5, 6, 99, 5, 15])

    def test_command_1001(self):
        code = [1001, 5, 10, 6, 99, 7, 0]
        computer = Intcomputer(code)
        computer.execute()
        self.assertEqual(computer.memory[:7], [1001, 5, 10, 6, 99, 7, 17])

    def test_command_201(self):
        code = [201, -4, 5, 7, 99, 3, 1, 0]
        computer = Intcomputer(code)
        computer.relative_base = 10
        computer.execute()
        self.assertEqual(computer.memory[:8], [201, -4, 5, 7, 99, 3, 1, 4])

    def test_command_1101(self):
        code = [1101, 5, -4, 5, 99, 0]
        computer = Intcomputer(code)
        computer.execute()
        self.assertEqual(computer.memory[:6], [1101, 5, -4, 5, 99, 1])

    def test_command_2101(self):
        code = [2101, 1, -4, 5, 99, 0, 2]
        computer = Intcomputer(code)
        computer.relative_base = 10
        computer.execute()
        self.assertEqual(computer.memory[:7], [2101, 1, -4, 5, 99, 3, 2])

    def test_command_20001(self):
        code = [20001, 5, 6, -3, 99, 2, 4, 0]
        computer = Intcomputer(code)
        computer.relative_base = 10
        computer.execute()
        self.assertEqual(computer.memory[:8], [20001, 5, 6, -3, 99, 2, 4, 6])

    def test_command_21001(self):
        code = [21001, 5, 1, -4, 99, 2, 0]
        computer = Intcomputer(code)
        computer.relative_base = 10
        computer.execute()
        self.assertEqual(computer.memory[:7], [21001, 5, 1, -4, 99, 2, 3])

    def test_command_21101(self):
        code = [21101, 1, 1, -5, 99, 0]
        computer = Intcomputer(code)
        computer.relative_base = 10
        computer.execute()
        self.assertEqual(computer.memory[:6], [21101, 1, 1, -5, 99, 2])

    def test_command_20101(self):
        code = [20101, 5, 1, -5, 99, 0]
        computer = Intcomputer(code)
        computer.relative_base = 10
        computer.execute()
        self.assertEqual(computer.memory[:6], [20101, 5, 1, -5, 99, 10])

    def test_command_1005(self):
        code = [1005, 3, 4, 1, 99]
        computer = Intcomputer(code)
        computer.execute()
        self.assertTrue(True)

    def test_command_1105(self):
        code = [1105, 1, 4, 0, 99]
        computer = Intcomputer(code)
        computer.execute()
        self.assertTrue(True)

    def test_command_2105(self):
        code = [2105, 1, -7, 4, 99]
        computer = Intcomputer(code)
        computer.relative_base = 10
        computer.execute()
        self.assertTrue(True)

    def test_command_1006a(self):
        code = [1006, 3, 4, 0, 99]
        computer = Intcomputer(code)
        computer.execute()
        self.assertTrue(True)

    def test_command_1006b(self):
        code = [1006, 4, 5, 99, 1, 0]
        computer = Intcomputer(code)
        computer.execute()
        self.assertTrue(True)

    def test_command_1106(self):
        code = [1106, 0, 4, 0, 99]
        computer = Intcomputer(code)
        computer.execute()
        self.assertTrue(True)

    def test_command_2106(self):
        code = [2106, 0, -7, 4, 99]
        computer = Intcomputer(code)
        computer.relative_base = 10
        computer.execute()
        self.assertTrue(True)

    def test_command_1206(self):
        code = [1206, -7, 4, 0, 99]
        computer = Intcomputer(code)
        computer.relative_base = 10
        computer.execute()
        self.assertTrue(True)

    def test_command_107(self):
        code = [107, 1, 3, 5, 99, -1]
        computer = Intcomputer(code)
        computer.execute()
        self.assertEqual(computer.memory[:6], [107, 1, 3, 5, 99, 1])

    def test_command_1007(self):
        code = [1007, 3, 1, 5, 99, -1]
        computer = Intcomputer(code)
        computer.execute()
        self.assertEqual(computer.memory[:6], [1007, 3, 1, 5, 99, 0])

    def test_command_1008(self):
        code = [1008, 6, 3, 5, 99, -1, 3]
        computer = Intcomputer(code)
        computer.execute()
        self.assertEqual(computer.memory[:7], [1008, 6, 3, 5, 99, 1, 3])

    def test_command_109(self):
        code = [109, -1, 99]
        computer = Intcomputer(code)
        computer.relative_base = 10
        computer.execute()
        self.assertEqual(computer.relative_base, 9)

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

    def test_solution_part_1(self):
        with open('input.txt') as f:
            code = [int(i) for i in f.readline().strip().split(',')]
        self.assertEqual(Intcomputer(code).execute(1)[1], 2351176124)

#     def test_solution_part_2(self):
#         with open('input.txt') as f:
#             code = [int(i) for i in f.readline().strip().split(',')]
#         self.assertEqual(Intcomputer(code).execute(2)[1], 73110)

