from itertools import permutations
from amplifier import Amplifier


def find_max_signal(code, phase_values=[0, 1, 2, 3, 4]):
    """Return the maximum signal that can be sent to thusters."""
    max_signal = -1

    for phase_setting in permutations(phase_values):
        amplifiers = initialize(phase_setting, code)
        signal = get_output_signal(amplifiers)
        max_signal = max(max_signal, signal)

    return max_signal


def initialize(phase_sequence, code):
    """Return amplifiers initialized according to phase sequence.

    Assumes that upon initialization, amplifiers will have no output.
    """
    amplifiers = [Amplifier(code) for _ in range(5)]

    for amp, phase in zip(amplifiers, phase_sequence):
        amp.execute(phase)

    return amplifiers


def get_output_signal(amplifiers):
    """Return the signal of the last amplifier after all halt."""
    signal = 0
    output = None

    while True:
        for amp in amplifiers:
            status, signal = amp.execute(signal)

        if status == 'OUTPUT':
            output = signal

        if status == 'HALT':
            return output

