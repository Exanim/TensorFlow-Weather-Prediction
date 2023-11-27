import unittest
import random
from model.output_transform.chaotic_randomizer import chaotic_random


class TestChaoticRandom(unittest.TestCase):
    def test_output_type(self):
        result = chaotic_random()
        self.assertTrue(isinstance(result, (float, int)), "Output should be of type float or int")

    def test_output_range(self):
        result = chaotic_random()
        self.assertTrue(0.0 <= result <= 25.0, "Output should be in the range [0.0, 25.0]")

    def test_upper_bound(self):
        for _ in range(1000):
            result = chaotic_random()
            self.assertTrue(0.0 <= result <= 25.0, "Output should be in the range [0.0, 25.0]")

    def test_lower_bound(self):
        for _ in range(1000):
            result = chaotic_random()
            self.assertTrue(isinstance(result, (float, int)), "Output should be of type float or int")


if __name__ == '__main__':
    unittest.main()
