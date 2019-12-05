from typing import List, Iterable

def execute(code: List[int], input_: Iterable[int] = None) -> List[int]:
    """Run the given integer program code.

    Args:
        code (List[int]): The program code to run.

        input_ (Iterable[int]): Input for write instructions. Assumes
            that there are enough input values for the program to use.

    Returns:
        List[int]: Values the program outputs during execution.

    Notice:
        Mutates the code!

    Example:

    >>>
    # multiply input 3 by 2
    execute([3, 9, 1002, 9, 2, 10, 4, 10, 99, 0, 0], iter([3]))
    6
    """
    def parse_instruction(ip):
        opcode = code[ip] % 100
        modes = [int(i) for i in list(str(code[ip] // 100))]
        return modes, opcode

    def add(ip, modes):
        i, j, k = code[ip + 1:ip + 4]
        x1 = i if modes[-1] == 1 else code[i]
        x2 = j if len(modes) >= 2 and modes[-2] == 1 else code[j]
        code[k] = x1 + x2

    def mul(ip, modes):
        i, j, k = code[ip + 1:ip + 4]
        x1 = i if modes[-1] == 1 else code[i]
        x2 = j if len(modes) >= 2 and modes[-2] == 1 else code[j]
        code[k] = x1 * x2

    def jump_if_true(ip, modes):
        i, j = code[ip + 1:ip + 3]
        x1 = i if modes[-1] == 1 else code[i]
        if x1 != 0:
            x2 = j if len(modes) >= 2 and modes[-2] == 1 else code[j]
            code[ip] = x2
            return True

    def jump_if_false(ip, modes):
        i, j = code[ip + 1:ip + 3]
        x1 = i if modes[-1] == 1 else code[i]
        if x1 == 0:
            x2 = j if len(modes) >= 2 and modes[-2] == 1 else code[j]
            code[ip] = x2
            return True

    def less_than(ip, modes):
        i, j, k = code[ip + 1:ip + 4]
        x1 = i if modes[-1] == 1 else code[i]
        x2 = j if len(modes) >= 2 and modes[-2] == 1 else code[j]
        code[k] = 1 if x1 < x2 else 0

    def equals(ip, modes):
        i, j, k = code[ip + 1:ip + 4]
        x1 = i if modes[-1] == 1 else code[i]
        x2 = j if len(modes) >= 2 and modes[-2] == 1 else code[j]
        code[k] = 1 if x1 == x2 else 0

    def write(ip):
        i = code[ip + 1]
        code[i] = next(input_)

    def read(ip, modes):
        i = code[ip + 1]
        output.append(i if modes[0] == 1 else code[i])

    # initialize instruction pointer
    ip = 0
    output = []

    while ip < len(code):
        modes, opcode = parse_instruction(ip)

        if opcode == 1:
            add(ip, modes)
            ip += 4
        elif opcode == 2:
            mul(ip, modes)
            ip += 4
        elif opcode == 3:
            write(ip)
            ip += 2
        elif opcode == 4:
            read(ip, modes)
            ip += 2
        elif opcode == 5:
            modified = jump_if_true(ip, modes)
            ip = code[ip] if modified else ip + 3
        elif opcode == 6:
            modified = jump_if_false(ip, modes)
            ip = code[ip] if modified else ip + 3
        elif opcode == 7:
            less_than(ip, modes)
            ip += 4
        elif opcode == 8:
            equals(ip, modes)
            ip += 4
        elif opcode == 99:
            break
        else:
            raise ValueError(f'unknown opcode: {opcode}')

    return output

