import sys
sys.path.insert(0, "core/")

import unittest
from shapes import *

class RectangleTest(unittest.TestCase):
    def test1(self):
        corner = Dim2D(0, 1)
        rec = Rectangle(corner, 20, 30)
        self.assertEqual(rec.upLeftCorner, Dim2D(0, 1))
        self.assertEqual(rec.width, 20)
        self.assertEqual(rec.height, 30)

class CircleTest(unittest.TestCase):
    def test1(self):
        pos = Dim2D(5, 5)
        circle = Circle(pos, 10)
        self.assertEqual(circle.centre, Dim2D(5, 5))
        self.assertEqual(circle.radius, 10)

class HexagonTest(unittest.TestCase):
    def test1(self):
        pass

if __name__ == "__main__":
    unittest.main()