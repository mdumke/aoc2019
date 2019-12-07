from itertools import permutations
from intcomputer import execute


def find_max_signal(code):
    max_signal = float('-inf')

    for phase_setting in permutations([0, 1, 2, 3, 4]):
        signal = 0

        for i in range(5):
            signal = execute(code[:], iter([phase_setting[i], signal]))[0]

        max_signal = max(signal, max_signal)

    return max_signal
