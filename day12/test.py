import numpy as np
from unittest import TestCase
from nbody import *


class TestTimestep(TestCase):
    def test_sample_1a(self):
        p = np.array([[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]])
        v = np.zeros_like(p)
        update(p, v)
        p_expected = np.array([[2, -1, 1], [3, -7, -4], [1, -7, 5], [2, 2, 0]])
        v_expected = np.array([[3, -1, -1], [1, 3, 3], [-3, 1, -3], [-1, -3, 1]])
        self.assertTrue(np.alltrue(p == p_expected))
        self.assertTrue(np.alltrue(v == v_expected))

    def test_sample_1b(self):
        p = np.array([[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]])
        v = np.zeros_like(p)
        for _ in range(10):
            update(p, v)
        p_expected = np.array([[2, 1, -3], [1, -8, 0], [3, -6, 1], [2, 0, 4]])
        v_expected = np.array([[-3, -2, 1], [-1, 1, 3], [3, 2, -3], [1, -1, -1]])
        self.assertTrue(np.alltrue(p == p_expected))
        self.assertTrue(np.alltrue(v == v_expected))


class TestTotalEnergy(TestCase):
    def test_sample_1(self):
        p = np.array([[2, 1, -3], [1, -8, 0], [3, -6, 1], [2, 0, 4]])
        v = np.array([[-3, -2, 1], [-1, 1, 3], [3, 2, -3], [1, -1, -1]])
        self.assertEqual(compute_total_energy(p, v), 179)


class TestE2E(TestCase):
    def test_sample_2(self):
        puzzle = """<x=-8, y=-10, z=0>
        <x=5, y=5, z=10>
        <x=2, y=-7, z=3>
        <x=9, y=-8, z=-3>
        """
        pos = parse_input(puzzle)
        vel = np.zeros_like(pos)
        for _ in range(100):
            update(pos, vel)
        self.assertEqual(compute_total_energy(pos, vel), 1940)


class TestComputeRecurrencePeriod(TestCase):
    def test_sample_1(self):
        p = np.array([[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]])
        v = np.zeros_like(p)
        self.assertEqual(compute_recurrence_period(p, v), 2772)

    def test_sample_2(self):
        p = np.array([[-8, -10, 0], [5, 5, 10], [2, -7, 3], [9, -8, -3]])
        v = np.zeros_like(p)
        self.assertEqual(compute_recurrence_period(p, v), 4686774924)


class TestFindPeriod(TestCase):
    def test_identical(self):
        values = [2, 2, 2, 2, 2, 2]
        self.assertEqual(find_period(values), 1)

    def test_two(self):
        values = [1, 3, 1, 3, 1, 3]
        self.assertEqual(find_period(values), 2)

    def test_four(self):
        values = [1, 2, 1, 3, 1, 2, 1, 3, 1, 2]
        self.assertEqual(find_period(values), 4)

    def test_from_sample_1(self):
        values = [-1, 2, 5, 5, 2, -1, -1, 2, 5, 5, 2, -1, -1, 2, 5, 5]
        self.assertEqual(find_period(values), 6)

    def test_no_period(self):
        values = [-1, 2, 5, 5, 2, -1, -1, 2]
        try:
            find_period(values)
        except IndexError:
            self.assertTrue(True)

    def test_from_stress_test_a(self):
        values = [0, 5, 0, 5, 3]
        self.assertEqual(find_period(values), 2)

    def test_from_stress_test_b(self):
        values = [1, 2, 1, 0, 1, 2, 1, 2, 1, 0, 1, 2, 1, 2, 1, 0, 1, 2]
        self.assertEqual(find_period(values), 6)
