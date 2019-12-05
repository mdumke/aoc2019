from typing import List

def execute(code: List[int]) -> None:
    """Run the given integer program code. Notice: mutates the code!"""
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

    def write(ip):
        i = code[ip + 1]
        code[i] = 1

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
        elif opcode == 99:
            break
        else:
            raise ValueError(f'unknown opcode: {opcode}')

    return output
