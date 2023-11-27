import unittest
from model.weather_api import city_in_default_cities


class TestCityFunctions(unittest.TestCase):

    def test_city_in_default_cities_positive(self):
        result = city_in_default_cities("budapest")
        self.assertTrue(result)

    def test_city_in_default_cities_negative(self):
        result = city_in_default_cities("debrecen")
        self.assertFalse(result)

    def test_city_in_default_cities_foreign(self):
        result = city_in_default_cities("Munich")
        self.assertFalse(result)

    def test_city_in_default_cities_empty_string(self):
        result = city_in_default_cities("")
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
