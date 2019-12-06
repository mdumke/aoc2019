from unittest import TestCase
from orbit import *


class TestCountOrbitalTransfers(TestCase):
    def test_single_orbit(self):
        orbit = {
            'COM': ['YOU', 'SAN'],
            'YOU': ['COM'],
            'SAN': ['COM']}
        self.assertEqual(count_orbital_transfers(orbit, 'YOU', 'SAN'), 0)


class TestComputeChecksum(TestCase):
    def test_single_node(self):
        orbit = {'COM': ['A'], 'A': ['COM']}
        self.assertEqual(compute_checksum(orbit, 'COM'), 1)

    def test_two_nodes(self):
        orbit = {'COM': ['A'], 'A': ['COM', 'B'], 'B': ['A']}
        self.assertEqual(compute_checksum(orbit, 'COM'), 3)

    def test_tiny_map(self):
        orbit = {
            'COM': ['A', 'C'],
            'A': ['COM', 'B'],
            'B': ['A'],
            'C': ['COM', 'A']}
        self.assertEqual(compute_checksum(orbit, 'COM'), 4)
        self.assertEqual(compute_checksum(orbit, 'A'), 4)

    def test_sample(self):
        orbit = {
            'COM': ['B'],
            'B': ['COM', 'C', 'G'],
            'C': ['B', 'D'],
            'D': ['C', 'E', 'I'],
            'E': ['D', 'F', 'J'],
            'F': ['E'],
            'G': ['B', 'H'],
            'H': ['G'],
            'I': ['D'],
            'J': ['E', 'K'],
            'K': ['J', 'L'],
            'L': ['K']}
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
            'B': ['COM', 'C', 'G'],
            'C': ['B', 'D'],
            'D': ['C', 'E', 'I'],
            'E': ['D', 'F', 'J'],
            'F': ['E'],
            'G': ['B', 'H'],
            'H': ['G'],
            'I': ['D'],
            'J': ['E', 'K'],
            'K': ['J', 'L'],
            'L': ['K']})
