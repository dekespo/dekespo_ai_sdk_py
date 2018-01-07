import sys
sys.path.insert(0, "core/")

import unittest
from shapes import *

class RectangleTest(unittest.TestCase):
    def test_simple(self):
        corner = Dim2D(0, 1)
        rec = Rectangle(corner, 20, 30)
        self.assertEqual(rec.upLeftCorner, Dim2D(0, 1))
        self.assertEqual(rec.width, 20)
        self.assertEqual(rec.height, 30)

class CircleTest(unittest.TestCase):
    def test_simple(self):
        pos = Dim2D(5, 5)
        circle = Circle(pos, 10)
        self.assertEqual(circle.centre, Dim2D(5, 5))
        self.assertEqual(circle.radius, 10)

class HexagonTest(unittest.TestCase):
    def test_simple(self):
        pass

class PointTest(unittest.TestCase):
    def test_simple(self):
        point = Point(Dim2D(2, 1))
        self.assertEqual(point.upLeftCorner, Dim2D(2, 1))
        self.assertEqual(point.width, 1)
        self.assertEqual(point.height, 1)

class ShapeTest(unittest.TestCase):
    def test_circleVscircleIntersectionCheck(self):
        circle1 = Circle(Dim2D(3, 3), 2)
        circle2 = Circle(Dim2D(1, 1), 2)
        circle3 = Circle(Dim2D(-2, -2), 2)
        circle4 = Circle(Dim2D(2, 2), 1.5)
        self.assertTrue(Shape.circleVscircleIntersectionCheck(circle1, circle2))
        self.assertTrue(Shape.circleVscircleIntersectionCheck(circle2, circle1))
        self.assertFalse(Shape.circleVscircleIntersectionCheck(circle1, circle3))
        self.assertFalse(Shape.circleVscircleIntersectionCheck(circle2, circle3))
        self.assertTrue(Shape.circleVscircleIntersectionCheck(circle1, circle4))
        self.assertTrue(Shape.circleVscircleIntersectionCheck(circle2, circle4))
        self.assertFalse(Shape.circleVscircleIntersectionCheck(circle3, circle4))

if __name__ == "__main__":
    unittest.main()