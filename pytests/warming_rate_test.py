import unittest
import math
from model.output_transform.global_warming_rate import logarithmic_warming_rate


class TestLogarithmicWarmingRate(unittest.TestCase):
    def test_output_type(self):
        result = logarithmic_warming_rate(1990, 25.0)
        self.assertTrue(isinstance(result, float), "Output should be of type float")

    def test_output_value_after_1981(self):
        result = logarithmic_warming_rate(1990, 25.0)
        self.assertAlmostEqual(result, 25.5, places=0, msg="Incorrect calculation for temperature after 1981")

    def test_output_value_before_1981(self):
        result = logarithmic_warming_rate(1970, 25.0)
        self.assertAlmostEqual(result, 25.0, places=0, msg="Incorrect calculation for temperature before 1981")

    def test_output_value_at_1981(self):
        result = logarithmic_warming_rate(1981, 25.0)
        self.assertAlmostEqual(result, 25.0, places=0, msg="Incorrect calculation for temperature at 1981")


if __name__ == '__main__':
    unittest.main()
