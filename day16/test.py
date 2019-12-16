from unittest import TestCase
from itertools import islice
from fft import fft

class TestFFT(TestCase):
    def test_sample_1(self):
        signal = [1, 2, 3, 4, 5, 6, 7, 8]
        phase_gen = fft(signal)
        self.assertEqual(next(phase_gen), '48226158')
        next(phase_gen)
        next(phase_gen)
        self.assertEqual(next(phase_gen), '01029498')

    def test_sample_2(self):
        signal = [int(i) for i in list('80871224585914546619083218645595')]
        phase_gen = fft(signal)
        self.assertEqual(list(islice(phase_gen, 100 - 1, 100))[0][:8], '24176176')

    def test_sample_3(self):
        signal = [int(i) for i in list('19617804207202209144916044189917')]
        phase_gen = fft(signal)
        self.assertEqual(list(islice(phase_gen, 100 - 1, 100))[0][:8], '73745418')
