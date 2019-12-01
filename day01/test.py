import time
from unittest import TestCase
from lib import compute_module_fuel_naive, compute_module_fuel


class TestComputeModuleFuelNaive(TestCase):
    def test_sample_1(self):
        self.assertEqual(compute_module_fuel_naive(12), 2)

    def test_sample_2(self):
        self.assertEqual(compute_module_fuel_naive(14), 2)

    def test_sample_3(self):
        self.assertEqual(compute_module_fuel_naive(1969), 654)

    def test_sample_4(self):
        self.assertEqual(compute_module_fuel_naive(100756), 33583)


class TestComputeModuleFuel(TestCase):
    def test_sample_1(self):
        self.assertEqual(compute_module_fuel(14), 2)

    def test_sample_2(self):
        self.assertEqual(compute_module_fuel(1969), 966)

    def test_sample_3(self):
        self.assertEqual(compute_module_fuel(100756), 50346)
