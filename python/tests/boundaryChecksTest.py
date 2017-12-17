import sys
sys.path.insert(0, "core/")

import unittest
from boundaryChecks import *
from shapes import *

class RectangleMapTest(unittest.TestCase):
    def test1(self):
        corner = Dim2D(0, 0)
        map = Rectangle(corner, 200, 100)
        self.assertTrue(boundaryChecks2D_rectangle(map, Dim2D(2, 3)))
        self.assertTrue(boundaryChecks2D_rectangle(map, Dim2D(199, 99)))
        self.assertTrue(boundaryChecks2D_rectangle(map, Dim2D(100, 99)))
        self.assertTrue(boundaryChecks2D_rectangle(map, Dim2D(100, 75)))
        self.assertFalse(boundaryChecks2D_rectangle(map, Dim2D(199, 100)))
        self.assertFalse(boundaryChecks2D_rectangle(map, Dim2D(202, 100)))
        self.assertFalse(boundaryChecks2D_rectangle(map, Dim2D(-1, 3)))
        self.assertFalse(boundaryChecks2D_rectangle(map, Dim2D(-1, -4)))

class CircleMapTest(unittest.TestCase):
    def test1(self):
        pass

class HexagonMapTest(unittest.TestCase):
    def test1(self):
        pass

if __name__ == "__main__":
    unittest.main()