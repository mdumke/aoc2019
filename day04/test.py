from unittest import TestCase
from password import *

class TestIsValid(TestCase):
    def test_sample_1(self):
        self.assertTrue(is_valid(111111, False))

    def test_sample_2(self):
        self.assertFalse(is_valid(223450, False))

    def test_sample_3(self):
        self.assertFalse(is_valid(123789, False))


class TestNumValidPasswords(TestCase):
    def test_1(self):
        self.assertEqual(num_valid_passwords(10, 15, False), 1)

    def test_2(self):
        self.assertEqual(num_valid_passwords(108, 115, False), 4)

