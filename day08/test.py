import numpy as np
from unittest import TestCase
from image import check_corruption, decode_image

class TestCheckCorruption(TestCase):
    def test_sample(self):
        digits = np.array(list('123456789012'), dtype=np.int8)
        self.assertEqual(check_corruption(digits, 3, 2), 1)

class TestDecodeImage(TestCase):
    def test_sample(self):
        digits = np.array(list('0222112222120000'), dtype=np.int8)
        decoded = decode_image(digits, 2, 2)
        expectation = np.array([[0, 1], [1, 0]])
        self.assertTrue(np.allclose(decoded, expectation))

