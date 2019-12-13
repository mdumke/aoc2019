from typing import List, Tuple


class Intcomputer:
    def __init__(self, code: List[int]):
        self.memory = [0] * 2**16
        self.memory[:len(code)] = code
        self.relative_base = 0
        self.ip = 0
        self.ip_trace = []

    def execute(self, input_ : int = None) -> Tuple[str, int]:
        """Run the program and return on output, missing input, or halt.

        Args:
            input_ (int): An optional input value to supply to a store_input
                instruction. If this instruction finds no value,
                it will return the `WAITING` status

        Returns:
            Tuple[str, int]: A pair (status, value) which indicates
                the state of the machine and if necessary, an output value.
                The status is one of ['WAITING', 'OUTPUT', 'HALT']
        """
        def parse_instruction():
            opcode = self.memory[self.ip] % 100
            modes = [int(i) for i in list(str(self.memory[self.ip] // 100))]
            modes = [0] * 8 + modes
            return modes, opcode

        def get_operands(modes):
            i, j, k = self.memory[self.ip + 1:self.ip + 4]

            if modes[-1] == 0:
                a = self.memory[i]
            elif modes[-1] == 1:
                a = i
            elif modes[-1] == 2:
                a = self.memory[self.relative_base + i]

            if modes[-2] == 0:
                b = self.memory[j]
            elif modes[-2] == 1:
                b = j
            elif modes[-2] == 2:
                b = self.memory[self.relative_base + j]

            # assume that the 3rd parameter determines the address,
            # which is handled differently
            if modes[-3] == 0:
                c = k
            elif modes[-3] == 2:
                c = k + self.relative_base

            return a, b, c

        def add(modes):
            a, b, c = get_operands(modes)
            self.memory[c] = a + b
            self.ip += 4

        def mul(modes):
            a, b, c = get_operands(modes)
            self.memory[c] = a * b
            self.ip += 4

        def jump_if_true(modes):
            a, b, _ = get_operands(modes)
            self.ip = b if a else self.ip + 3

        def jump_if_false(modes):
            a, b, _ = get_operands(modes)
            self.ip = b if not a else self.ip + 3

        def less_than(modes):
            a, b, c = get_operands(modes)
            self.memory[c] = 1 if a < b else 0
            self.ip += 4

        def equals(modes):
            a, b, c = get_operands(modes)
            self.memory[c] = 1 if a == b else 0
            self.ip += 4

        def adjust_relative_base(modes):
            a, *_ = get_operands(modes)
            self.relative_base += a
            self.ip += 2

        def store_input(modes):
            nonlocal input_
            i = self.memory[self.ip + 1]
            if modes[-1] == 2:
                i += self.relative_base
            self.memory[i] = input_
            input_ = None
            self.ip += 2

        def write_output(modes):
            a, *_ = get_operands(modes)
            self.ip += 2
            return a

        while self.ip < len(self.memory):
            self.ip_trace.append(self.ip)
            modes, opcode = parse_instruction()

            if opcode == 1:
                add(modes)
            elif opcode == 2:
                mul(modes)
            elif opcode == 3:
                if input_ is None:
                    return 'WAITING', None
                store_input(modes)
            elif opcode == 4:
                return 'OUTPUT', write_output(modes)
            elif opcode == 5:
                jump_if_true(modes)
            elif opcode == 6:
                jump_if_false(modes)
            elif opcode == 7:
                less_than(modes)
            elif opcode == 8:
                equals(modes)
            elif opcode == 9:
                adjust_relative_base(modes)
            elif opcode == 99:
                break
            else:
                raise ValueError(f'unknown opcode: {opcode} at IP {self.ip}')

        return 'HALT', None

