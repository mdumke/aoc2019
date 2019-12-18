from unittest import TestCase

def split(sequence, maxlen=10):
    """Return three subsequences - building blocks of the sequence."""
    is_match = lambda i, j, l: l > 0 and sequence[i:i + l] == sequence[j:j + l]

    a_pos = b_pos = c_pos = 0
    a_len = b_len = c_len = 0
    i = 0

    while i < len(sequence):
        if is_match(i, a_pos, a_len):
            i += a_len
        elif  is_match(i, b_pos, b_len):
            i += b_len
        elif is_match(i, c_pos, c_len):
            i += c_len
        elif c_len < maxlen:
            if c_len == 0: c_pos = i
            c_len += 1
            i = 0
        elif b_len < maxlen:
            if b_len == 0: b_pos = i
            b_len += 1
            c_len = 0
            i = 0
        elif a_len < maxlen:
            a_len += 1
            b_len = c_len = 0
            i = 0
        else:
            return None

    return (sequence[a_pos:a_pos + a_len],
            sequence[b_pos:b_pos + b_len],
            sequence[c_pos:c_pos + c_len])


class TestSplit(TestCase):
    def test_empty(self):
        sequence = []
        self.assertEqual(split(sequence), ([], [], []))

    def test_single(self):
        sequence = [1]
        self.assertEqual(split(sequence), ([], [], [1]))

    def test_three(self):
        sequence = [1, 2, 3]
        self.assertEqual(split(sequence), ([], [], [1, 2, 3]))

    def test_max_len_1(self):
        sequence = [1, 2, 3]
        self.assertEqual(split(sequence, 2), ([], [3], [1, 2]))

    def test_max_len_2(self):
        sequence = [1, 2, 3, 4, 5]
        self.assertEqual(split(sequence, 2), ([1], [4, 5], [2, 3]))

    def test_no_split(self):
        sequence = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(split(sequence, 2), None)

    def test_repetition_1(self):
        sequence = [1, 2, 1, 2]
        self.assertEqual(split(sequence, 2), ([], [], [1, 2]))

    def test_repetition_2(self):
        sequence = [1, 2, 3, 1, 2]
        self.assertEqual(split(sequence, 2), ([], [3], [1, 2]))

    def test_repetition_3(self):
        sequence = [1, 2, 1, 2, 3, 4]
        self.assertEqual(split(sequence, 2), ([], [3, 4], [1, 2]))

    def test_repetition_4(self):
        sequence = [1, 2, 3, 4, 1, 2, 5, 6]
        self.assertEqual(split(sequence, 2), ([1, 2], [5, 6], [3, 4]))

    def test_complex_example(self):
        sequence = [1, 2, 1, 2, 3, 4, 1, 2, 5, 6, 3, 4, 5, 6, 5, 6, 1, 2]
        self.assertEqual(split(sequence, 2), ([1, 2], [5, 6], [3, 4]))

    def test_steps(self):
        steps = 'L,12,R,4,R,4,R,12,R,4,L,12,R,12,R,4,L,12,R,12,R,4,L,6,'\
                'L,8,L,8,R,12,R,4,L,6,L,8,L,8,L,12,R,4,R,4,L,12,R,4,R,4,R,'\
                '12,R,4,L,12,R,12,R,4,L,12,R,12,R,4,L,6,L,8,L,8'
        sequence = []
        for i in steps.split(','):
            try:
                sequence.append(int(i))
            except ValueError:
                sequence.append(i)

        self.assertTrue(split(sequence, 12))
