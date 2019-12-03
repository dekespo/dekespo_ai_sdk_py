import unittest

from core.dimensions import Dim2D
from core.shapes import Rectangle, Circle, Point

class RectangleTest(unittest.TestCase):
    def test_simple(self):
        top_left_corner = Dim2D(0, 1)
        rec = Rectangle(top_left_corner, 20, 30)
        self.assertEqual(rec.top_left_corner, Dim2D(0, 1))
        self.assertEqual(rec.width, 20)
        self.assertEqual(rec.height, 30)
        self.assertEqual(
            str(rec),
            "top_left_corner = (x: 0, y: 1), width x height: 20x30"
        )
        self.assertEqual(rec.get_position(), Dim2D(0, 1))
        four_corner_points = (
            Dim2D(0, 1),
            Dim2D(20, 1),
            Dim2D(0, 31),
            Dim2D(20, 31)
        )
        self.assertEqual(rec.get_four_corner_points(), four_corner_points)

    def test_check_boundaries(self):
        top_left_corner = Dim2D(0, 0)
        rectangle = Rectangle(top_left_corner, 200, 100)
        self.assertTrue(rectangle.check_boundaries(Dim2D(2, 3)))
        self.assertTrue(rectangle.check_boundaries(Dim2D(199, 99)))
        self.assertTrue(rectangle.check_boundaries(Dim2D(100, 99)))
        self.assertTrue(rectangle.check_boundaries(Dim2D(100, 75)))
        self.assertFalse(rectangle.check_boundaries(Dim2D(199, 100)))
        self.assertFalse(rectangle.check_boundaries(Dim2D(202, 100)))
        self.assertFalse(rectangle.check_boundaries(Dim2D(-1, 3)))
        self.assertFalse(rectangle.check_boundaries(Dim2D(-1, -4)))

class CircleTest(unittest.TestCase):
    def test_simple(self):
        pos = Dim2D(5, 5)
        circle = Circle(pos, 10)
        self.assertEqual(circle.centre, Dim2D(5, 5))
        self.assertEqual(circle.radius, 10)
        self.assertEqual(
            str(circle),
            "centre: (x: 5, y: 5), radius: 10"
        )
        self.assertEqual(circle.get_position(), Dim2D(5, 5))

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
        point = Point(Dim2D(2, 1))
        self.assertEqual(point.position, Dim2D(2, 1))
        self.assertEqual(
            str(point),
            "position: (x: 2, y: 1)"
        )
        self.assertEqual(point.get_position(), Dim2D(2, 1))

class Shape2DTest(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()
