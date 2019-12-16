import numpy as np
from itertools import cycle, islice

def fft(signal):
    """Return fft for the full signal."""
    n = len(signal)
    m = [list(islice(cycle(np.repeat([0, 1, 0, -1], i)), 1, n + 1))
         for i in range(1, n + 1)]
    return np.abs(np.dot(m, signal)) % 10


def fft2(signal):
    """Return fft, with correctness only guaranteed on the 2nd half!"""
    return np.cumsum(signal[::-1])[::-1] % 10

