from unittest import TestCase
from wire import (
        get_wire_coordinates, find_crossing, deserialize_wire,
        manhattan)

U = 'U'
D = 'D'
L = 'L'
R = 'R'

class TestGetWireCoordinates(TestCase):
    def test_1(self):
        coords = list(get_wire_coordinates([('R', 1)]))
        self.assertEqual(coords, [(1, 0)])

    def test_2(self):
        coords = list(get_wire_coordinates([('U', 2)]))
        self.assertEqual(coords, [(0, 1), (0, 2)])

    def test_3(self):
        wire = [('U', 1), ('L', 2), ('D', 2), ('R', 1)]
        coords = list(get_wire_coordinates(wire))
        expectation = [(0, 1), (-1, 1), (-2, 1), (-2, 0), (-2, -1), (-1, -1)]
        self.assertEqual(coords, expectation)


class TestDeserializeWire(TestCase):
    def test_1(self):
        self.assertEqual(deserialize_wire('U1'), [('U', 1)])

    def test_2(self):
        self.assertEqual(deserialize_wire('D2,R5'), [('D', 2), ('R', 5)])


class TestFindCrossing(TestCase):
    def test_1(self):
        wire1 = [('U', 1)]
        wire2 = [('D', 1)]
        self.assertEqual(find_crossing(wire1, wire2), None)

    def test_2(self):
        wire1 = [('U', 1)]
        wire2 = [('U', 1)]
        self.assertEqual(find_crossing(wire1, wire2), (0, 1))

    def test_sample_1(self):
        wire1 = [(R, 75), (D, 30), (R, 83), (U, 83),
                 (L, 12), (D, 49), (R, 71), (U, 7), (L, 72)]
        wire2 = [(U, 62), (R, 66), (U, 55), (R, 34), (D, 71),
                 (R, 55), (D, 58), (R, 83)]
        crossing = find_crossing(wire1, wire2)
        self.assertEqual(manhattan(crossing), 159)

    def test_sample_2(self):
        wire1 = [(R, 98), (U, 47), (R, 26), (D, 63), (R, 33),
                 (U, 87), (L, 62), (D, 20), (R, 33), (U, 53), (R, 51)]
        wire2 = [(U, 98), (R, 91), (D, 20), (R, 16), (D, 67),
                 (R, 40), (U, 7), (R, 15), (U, 6), (R,  7)]
        crossing = find_crossing(wire1, wire2)
        self.assertEqual(manhattan(crossing), 135)
