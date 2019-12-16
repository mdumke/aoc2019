import numpy as np
from itertools import cycle

def fft(signal):
    pattern = lambda i: np.repeat([0, 1, 0, -1], i + 1)
    digit = lambda p: abs(sum(list(i * j for i, j in zip([0, *signal], cycle(pattern(p))))[1:])) % 10

    while True:
        signal = [digit(pos) for pos in range(len(signal))]
        yield ''.join([str(d) for d in signal])





if __name__ == '__main__':
    import sys
    from itertools import islice
    signal = [int(i) for i in sys.stdin.readline().strip()]
    phases = fft(signal)
    print(list(islice(phases, 99, 100))[0][:8])
