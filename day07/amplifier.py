from typing import List, Tuple


class Amplifier:
    def __init__(self, code: List[int]):
        self.code = code[:]
        self.ip = 0

    def execute(self, input_ : int = None) -> Tuple[str, int]:
        """Run the program and return on output, missing input, or halt.

        Args:
            input_ (int): An optional input value to supply to a read
                instruction. If a read instruction finds no value,
                it will pause and return the `WAITING` status

        Returns:
            Tuple[str, int]: A pair (status, value) which indicates
                the state of the machine and if necessary, an output value.
                The status is one of ['WAITING', 'OUTPUT', 'HALT']
        """
        def parse_instruction():
            opcode = self.code[self.ip] % 100
            modes = [int(i) for i in list(str(self.code[self.ip] // 100))]
            return modes, opcode

        def add(modes):
            i, j, k = self.code[self.ip + 1:self.ip + 4]
            x1 = i if modes[-1] == 1 else self.code[i]
            x2 = j if len(modes) >= 2 and modes[-2] == 1 else self.code[j]
            self.code[k] = x1 + x2
            self.ip += 4

        def mul(modes):
            i, j, k = self.code[self.ip + 1:self.ip + 4]
            x1 = i if modes[-1] == 1 else self.code[i]
            x2 = j if len(modes) >= 2 and modes[-2] == 1 else self.code[j]
            self.code[k] = x1 * x2
            self.ip += 4

        def jump_if_true(modes):
            i, j = self.code[self.ip + 1:self.ip + 3]
            x1 = i if modes[-1] == 1 else self.code[i]
            if x1 != 0:
                x2 = j if len(modes) >= 2 and modes[-2] == 1 else self.code[j]
                self.ip = x2
            else:
                self.ip += 3

        def jump_if_false(modes):
            i, j = self.code[self.ip + 1:self.ip + 3]
            x1 = i if modes[-1] == 1 else self.code[i]
            if x1 == 0:
                x2 = j if len(modes) >= 2 and modes[-2] == 1 else self.code[j]
                self.ip = x2
            else:
                self.ip += 3

        def less_than(modes):
            i, j, k = self.code[self.ip + 1:self.ip + 4]
            x1 = i if modes[-1] == 1 else self.code[i]
            x2 = j if len(modes) >= 2 and modes[-2] == 1 else self.code[j]
            self.code[k] = 1 if x1 < x2 else 0
            self.ip += 4

        def equals(modes):
            i, j, k = self.code[self.ip + 1:self.ip + 4]
            x1 = i if modes[-1] == 1 else self.code[i]
            x2 = j if len(modes) >= 2 and modes[-2] == 1 else self.code[j]
            self.code[k] = 1 if x1 == x2 else 0
            self.ip += 4

        def write():
            i = self.code[self.ip + 1]
            self.code[i] = next(input_)
            self.ip += 2

        def read(modes):
            i = self.code[self.ip + 1]
            self.ip += 2
            return i if modes[0] == 1 else self.code[i]

        input_ = iter([]) if input_ is None else iter([input_])

        while self.ip < len(self.code):
            modes, opcode = parse_instruction()

            if opcode == 1:
                add(modes)
            elif opcode == 2:
                mul(modes)
            elif opcode == 3:
                try:
                    write()
                except StopIteration:
                    return 'WAITING', None
            elif opcode == 4:
                return 'OUTPUT', read(modes)
            elif opcode == 5:
                jump_if_true(modes)
            elif opcode == 6:
                jump_if_false(modes)
            elif opcode == 7:
                less_than(modes)
            elif opcode == 8:
                equals(modes)
            elif opcode == 99:
                break
            else:
                raise ValueError(f'unknown opcode: {opcode} at {self.ip}')

        return 'HALT', None

