import sys
from wire import *

def get_input():
    wire1 = deserialize_wire(sys.stdin.readline())
    wire2 = deserialize_wire(sys.stdin.readline())
    return wire1, wire2

if __name__ == '__main__':
    wire1, wire2 = get_input()
    print(f'part 1: {manhattan(find_crossing(wire1, wire2))}')
