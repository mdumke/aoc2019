import sys
from intcomputer import Intcomputer

if __name__ == '__main__':
    code = [int(n) for n in sys.stdin.readline().strip().split(',')]

    computer = Intcomputer(code)

    while True:
        status, out = computer.execute(1)

        print(status, out)

        if status == 'HALT':
            break
