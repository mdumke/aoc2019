#!/usr/bin/env python

"""Compute minimum distance and steps of wire crossings."""

import sys
from wire import deserialize_wire, find_crossings

def get_input():
    wire1 = deserialize_wire(sys.stdin.readline())
    wire2 = deserialize_wire(sys.stdin.readline())
    return wire1, wire2


if __name__ == '__main__':
    crossings = find_crossings(*get_input())

    min_dist = min(c['dist'] for c in crossings)
    min_steps = min(c['steps'] for c in crossings)

    print(f'part 1: {min_dist}')
    print(f'part 2: {min_steps}')
