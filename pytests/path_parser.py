import unittest
from model.weather_api import get_last_path_element


class TestPathFunctions(unittest.TestCase):

    def test_get_last_path_element_correct_budapest(self):
        path = "localhost:8000/budapest"
        result = get_last_path_element(path)
        self.assertEqual(result, "budapest")

    def test_get_last_path_element_correct_sopron(self):
        path = "localhost:8000/sopron"
        result = get_last_path_element(path)
        self.assertEqual(result, "sopron")

    def test_get_last_path_element_empty(self):
        path = ""
        result = get_last_path_element(path)
        self.assertEqual(result, "")

    def test_get_last_path_element_multiple_elements(self):
        path = "localhost:8000/budapest/some/other/path"
        result = get_last_path_element(path)
        self.assertEqual(result, "path")


if __name__ == '__main__':
    unittest.main()
