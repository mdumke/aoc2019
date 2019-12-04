from unittest import TestCase
from password import *

class TestIsValid(TestCase):
    def test_sample_1(self):
        self.assertTrue(is_valid_password('111111', False))

    def test_sample_2(self):
        self.assertFalse(is_valid_password('223450', False))

    def test_sample_3(self):
        self.assertFalse(is_valid_password('123789', False))


class TestNumValidPasswords(TestCase):
    def test_1(self):
        self.assertEqual(count_valid_passwords(10, 15, False), 1)

    def test_2(self):
        self.assertEqual(count_valid_passwords(108, 115, False), 4)

    def test_3(self):
        self.assertEqual(count_valid_passwords(240920, 789857, False), 1154)

    def test_4(self):
        self.assertEqual(count_valid_passwords(240920, 789857, True), 750)
