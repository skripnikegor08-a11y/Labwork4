import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):

    def test_zero_area(self):
        result = area(10, 0)
        self.assertEqual(result, 0)

    def test_square_area(self):
        result = area(10, 10)
        self.assertEqual(result, 100)

    def test_rectangle_area(self):
        result = area(10, 5)
        self.assertEqual(result, 50)

    def test_rectangle_perimeter(self):
        result = perimeter(10, 5)
        self.assertEqual(result, 30)

    def test_square_perimeter(self):
        result = perimeter(10, 10)
        self.assertEqual(result, 40)


if __name__ == "__main__":
    unittest.main()