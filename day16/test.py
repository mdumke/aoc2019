from unittest import TestCase
from fft import fft, fft2


class TestFFT(TestCase):
    def test_sample_1(self):
        signal = [1, 2, 3, 4, 5, 6, 7, 8]
        signal = fft(signal)
        self.assertEqual(list(signal), [4, 8, 2, 2, 6, 1, 5, 8])
        signal = fft(signal)
        self.assertEqual(list(signal), [3, 4, 0, 4, 0, 4, 3, 8])
        signal = fft(signal)
        self.assertEqual(list(signal), [0, 3, 4, 1, 5, 5, 1, 8])

    def test_sample_2(self):
        signal = list(map(int, '80871224585914546619083218645595'))
        for _ in range(100):
            signal = fft(signal)
        self.assertEqual(list(signal)[:8], [2, 4, 1, 7, 6, 1, 7, 6])

    def test_sample_3(self):
        signal = list(map(int, '19617804207202209144916044189917'))
        for _ in range(100):
            signal = fft(signal)
        self.assertEqual(list(signal)[:8], [7, 3, 7, 4, 5, 4, 1, 8])


class TestFFT2(TestCase):
    def test_sample_2(self):
        signal = [1, 2, 3, 4, 5, 6, 7, 8]
        signal = fft(signal)
        self.assertEqual(list(signal)[4:], [6, 1, 5, 8])
        signal = fft(signal)
        self.assertEqual(list(signal)[4:], [0, 4, 3, 8])
        signal = fft(signal)
        self.assertEqual(list(signal)[4:], [5, 5, 1, 8])

