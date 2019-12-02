from typing import List

def execute(code: List[int]) -> None:
    """Run the given integer program code. Notice: mutates the code!"""
    def add(i):
        i, j, k = code[i + 1:i + 4]
        code[k] = code[i] + code[j]

    def mul(i):
        i, j, k = code[i + 1:i + 4]
        code[k] = code[i] * code[j]

    ip = 0

    while ip < len(code):
        opcode = code[ip]

        if opcode == 1:
            add(ip)
            ip += 4
        elif opcode == 2:
            mul(ip)
            ip += 4
        elif opcode == 99:
            break
        else:
            raise ValueError(f'unknown opcode: {opcode}')

