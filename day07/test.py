from unittest import TestCase
from amplifier import Amplifier
from thruster import find_max_signal


class TestAmplifier(TestCase):
    def test_wait(self):
        code = [3, 3, 99, 0]
        amplifier = Amplifier(code)
        status, signal = amplifier.execute()
        self.assertEqual(status, 'WAITING')
        self.assertEqual(signal, None)
        status, signal = amplifier.execute(10)
        self.assertEqual(status, 'HALT')
        self.assertEqual(signal, None)

    def test_io(self):
        code = [3, 9, 1002, 9, 2, 10, 4, 10, 99, 0, 0]
        amplifier = Amplifier(code)
        status, signal = amplifier.execute(3)
        self.assertEqual(status, 'OUTPUT')
        self.assertEqual(signal, 6)
        status, signal = amplifier.execute()
        self.assertEqual(status, 'HALT')
        self.assertEqual(signal, None)

    def test_sample_9(self):
        code = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
        amplifier = Amplifier(code)
        status, signal = amplifier.execute(0)
        self.assertEqual(status, 'OUTPUT')
        self.assertEqual(signal, 1)
        status, signal = amplifier.execute()
        self.assertEqual(status, 'HALT')
        self.assertEqual(signal, None)

    def test_sample_11(self):
        code = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
        amplifier = Amplifier(code)
        status, signal = amplifier.execute(1)
        self.assertEqual(status, 'OUTPUT')
        self.assertEqual(signal, 1)
        status, signal = amplifier.execute()
        self.assertEqual(status, 'HALT')
        self.assertEqual(signal, None)


class TestFindMaxSignal(TestCase):
    def test_sample_1(self):
        code = '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0'
        code = [int(n) for n in code.split(',')]
        self.assertEqual(find_max_signal(code), 43210)

    def test_sample_2(self):
        code = '3,23,3,24,1002,24,10,24,1002,23,-1,23,' + \
               '101,5,23,23,1,24,23,23,4,23,99,0,0'
        code = [int(n) for n in code.split(',')]
        self.assertEqual(find_max_signal(code), 54321)

    def test_sample_3(self):
        code = '3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,' + \
               '1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0'
        code = [int(n) for n in code.split(',')]
        self.assertEqual(find_max_signal(code), 65210)

    def test_sample_4(self):
        code = '3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,' + \
               '27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5'
        code = [int(n) for n in code.split(',')]
        self.assertEqual(find_max_signal(code, [5, 6, 7, 8, 9]), 139629729)

    def test_sample_5(self):
        code = '3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,' + \
               '55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,' + \
               '1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,' + \
               '99,0,0,0,0,10'
        code = [int(n) for n in code.split(',')]
        self.assertEqual(find_max_signal(code, [5, 6, 7, 8, 9]), 18216)
