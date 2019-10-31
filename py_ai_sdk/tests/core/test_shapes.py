import unittest

from py_ai_sdk.core.dimensions import Dim2D
from py_ai_sdk.core.shapes import Rectangle, Circle, Point

class RectangleTest(unittest.TestCase):
    def test_simple(self):
        top_left_corner = Dim2D(0, 1)
        rec = Rectangle(top_left_corner, 20, 30)
        self.assertEqual(rec.top_left_corner, Dim2D(0, 1))
        self.assertEqual(rec.width, 20)
        self.assertEqual(rec.height, 30)

    def test_check_boundaries(self):
        top_left_corner = Dim2D(0, 0)
        graph = Rectangle(top_left_corner, 200, 100)
        self.assertTrue(graph.check_boundaries(Dim2D(2, 3)))
        self.assertTrue(graph.check_boundaries(Dim2D(199, 99)))
        self.assertTrue(graph.check_boundaries(Dim2D(100, 99)))
        self.assertTrue(graph.check_boundaries(Dim2D(100, 75)))
        self.assertFalse(graph.check_boundaries(Dim2D(199, 100)))
        self.assertFalse(graph.check_boundaries(Dim2D(202, 100)))
        self.assertFalse(graph.check_boundaries(Dim2D(-1, 3)))
        self.assertFalse(graph.check_boundaries(Dim2D(-1, -4)))

class CircleTest(unittest.TestCase):
    def test_simple(self):
        pos = Dim2D(5, 5)
        circle = Circle(pos, 10)
        self.assertEqual(circle.centre, Dim2D(5, 5))
        self.assertEqual(circle.radius, 10)

    def test_circle_vs_circle_intersection_check(self):
        circle1 = Circle(Dim2D(3, 3), 2)
        circle2 = Circle(Dim2D(1, 1), 2)
        circle3 = Circle(Dim2D(-2, -2), 2)
        circle4 = Circle(Dim2D(2, 2), 1.5)
        self.assertTrue(Circle.circle_vs_circle_intersection_check(circle1, circle2))
        self.assertTrue(Circle.circle_vs_circle_intersection_check(circle2, circle1))
        self.assertFalse(Circle.circle_vs_circle_intersection_check(circle1, circle3))
        self.assertFalse(Circle.circle_vs_circle_intersection_check(circle2, circle3))
        self.assertTrue(Circle.circle_vs_circle_intersection_check(circle1, circle4))
        self.assertTrue(Circle.circle_vs_circle_intersection_check(circle2, circle4))
        self.assertFalse(Circle.circle_vs_circle_intersection_check(circle3, circle4))

class PointTest(unittest.TestCase):
    def test_simple(self):
        point1 = Point(Dim2D(2, 1))
        self.assertEqual(point1.position, Dim2D(2, 1))
        point2 = Point(Dim2D(-5, -3))
        self.assertEqual(point2.position, Dim2D(-5, -3))

class Shape2DTest(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()
