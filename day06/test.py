from unittest import TestCase
from orbit import *


class TestComputeChecksum(TestCase):
    def test_single_node(self):
        self.assertEqual(compute_checksum({'COM': ['A']}, 'COM'), 1)

    def test_two_nodes(self):
        orbit = {'COM': ['A'], 'A': ['B']}
        self.assertEqual(compute_checksum(orbit, 'COM'), 3)

    def test_tiny_map(self):
        orbit = {
            'COM': ['A', 'C'],
            'A': ['B']}
        self.assertEqual(compute_checksum(orbit, 'COM'), 4)

    def test_sample(self):
        orbit = {
            'COM': ['B'],
            'B': ['C', 'G'],
            'C': ['D'],
            'D': ['E', 'I'],
            'E': ['F', 'J'],
            'G': ['H'],
            'J': ['K'],
            'K': ['L']}
        self.assertEqual(compute_checksum(orbit, 'COM'), 42)


class TestParseInput(TestCase):
    def test_sample(self):
        sample_map_serialized = """COM)B
        B)C
        C)D
        D)E
        E)F
        B)G
        G)H
        D)I
        E)J
        J)K
        K)L"""

        self.assertEqual(parse_input(sample_map_serialized), {
            'COM': ['B'],
            'B': ['C', 'G'],
            'C': ['D'],
            'D': ['E', 'I'],
            'E': ['F', 'J'],
            'G': ['H'],
            'J': ['K'],
            'K': ['L']})
