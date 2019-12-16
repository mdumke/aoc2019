"""Compute transformations on transmission signal."""

import sys
import numpy as np
from fft import fft, fft2


if __name__ == '__main__':
    input_ = [int(i) for i in sys.stdin.read().strip()]

    signal = input_[:]
    for _ in range(100):
        signal = fft(signal)
    print('part 1:', signal[:8])

    signal = input_ * 10000
    for _ in range(100):
        signal = fft2(signal)
    # the read index refers to the second part of the signal,
    # so using fft2 is valid
    i = int(''.join(map(str, input_[:7])))
    print('part 2:', signal[i:i + 8])

