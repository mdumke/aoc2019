import sys
from thruster import find_max_signal

if __name__ == '__main__':
    code = [int(n) for n in sys.stdin.readline().split(',')]
    print('part 1', find_max_signal(code[:]))

