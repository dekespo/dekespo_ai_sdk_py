import unittest

from py_ai_sdk.core.dimensions import Dim2D
from py_ai_sdk.core.shapes import Rectangle, Point, Circle
from py_ai_sdk.core.motion_physics import MotionPhysics2D

class MotionPhysics2DTest(unittest.TestCase):
    def test_velocity(self):
        pos = Dim2D(3, 5)
        point = Point(pos)
        vel = Dim2D(2, 2)
        point.addMotionPhysics(MotionPhysics2D(vel))
        self.assertEqual(point.position, Dim2D(3, 5))
        self.assertEqual(point.motionPhysics.velocity, Dim2D(2, 2))

    def test_all(self):
        pos = Dim2D(3, 5)
        point = Point(pos)
        vel = Dim2D(2, 2)
        acc = Dim2D(1, -1)
        force = Dim2D(-5, 0)
        momentum = Dim2D(-9, 9)
        mass = 6.5
        point.addMotionPhysics(MotionPhysics2D(vel, acc, force, momentum, mass))
        self.assertEqual(point.position, Dim2D(3, 5))
        self.assertEqual(point.motionPhysics.velocity, Dim2D(2, 2))
        self.assertEqual(point.motionPhysics.acceleration, Dim2D(1, -1))
        self.assertEqual(point.motionPhysics.force, Dim2D(-5, 0))
        self.assertEqual(point.motionPhysics.momentum, Dim2D(-9, 9))
        self.assertEqual(point.motionPhysics.mass, 6.5)

    def test_random1(self):
        pos = Dim2D(3, 5)
        point = Point(pos)
        vel = Dim2D(2, 2)
        acc = Dim2D(1, -1)
        mass = 6.5
        point.addMotionPhysics(MotionPhysics2D(vel, acceleration=acc, mass=mass))
        self.assertEqual(point.position, Dim2D(3, 5))
        self.assertEqual(point.motionPhysics.velocity, Dim2D(2, 2))
        self.assertEqual(point.motionPhysics.acceleration, Dim2D(1, -1))
        self.assertEqual(point.motionPhysics.force, Dim2D(6.5, -6.5))
        self.assertEqual(point.motionPhysics.momentum, Dim2D(13, 13))
        self.assertEqual(point.motionPhysics.mass, 6.5)

    def test_random2(self):
        pos = Dim2D(3, 5)
        point = Point(pos)
        vel = Dim2D(2, 2)
        mass = 4.5
        force = Dim2D(-5, 0)
        point.addMotionPhysics(MotionPhysics2D(vel, force=force, mass=mass))
        self.assertEqual(point.position, Dim2D(3, 5))
        self.assertEqual(point.motionPhysics.velocity, Dim2D(2, 2))
        self.assertEqual(point.motionPhysics.acceleration, Dim2D(-5 / 4.5, 0))
        self.assertEqual(point.motionPhysics.force, Dim2D(-5, 0))
        self.assertEqual(point.motionPhysics.momentum, Dim2D(9, 9))
        self.assertEqual(point.motionPhysics.mass, 4.5)

    def test_random3(self):
        pos = Dim2D(3, 5)
        point = Point(pos)
        vel = Dim2D(2, 3)
        force = Dim2D(-5, 0)
        momentum = Dim2D(6, 9)
        point.addMotionPhysics(MotionPhysics2D(vel, force=force, momentum=momentum))
        self.assertEqual(point.position, Dim2D(3, 5))
        self.assertEqual(point.motionPhysics.velocity, Dim2D(2, 3))
        self.assertEqual(point.motionPhysics.acceleration, Dim2D(-5 / 3, 0))
        self.assertEqual(point.motionPhysics.force, Dim2D(-5, 0))
        self.assertEqual(point.motionPhysics.momentum, Dim2D(6, 9))
        self.assertEqual(point.motionPhysics.mass, 3)

    def test_randomWithCircle(self):
        pos = Dim2D(3, 5)
        radius = 3
        circle = Circle(pos, radius)
        vel = Dim2D(2, 2)
        acc = Dim2D(1, -1)
        mass = 6.5
        circle.addMotionPhysics(MotionPhysics2D(vel, acceleration=acc, mass=mass))
        self.assertEqual(circle.centre, Dim2D(3, 5))
        self.assertEqual(circle.radius, 3)
        self.assertEqual(circle.motionPhysics.velocity, Dim2D(2, 2))
        self.assertEqual(circle.motionPhysics.acceleration, Dim2D(1, -1))
        self.assertEqual(circle.motionPhysics.force, Dim2D(6.5, -6.5))
        self.assertEqual(circle.motionPhysics.momentum, Dim2D(13, 13))
        self.assertEqual(circle.motionPhysics.mass, 6.5)

    def test_randomWithRectangle(self):
        pos = Dim2D(3, 5)
        width, height = 4, 5
        rec = Rectangle(pos, width, height)
        vel = Dim2D(2, 2)
        mass = 4.5
        force = Dim2D(-5, 0)
        rec.addMotionPhysics(MotionPhysics2D(vel, force=force, mass=mass))
        self.assertEqual(rec.top_left_corner, Dim2D(3, 5))
        self.assertEqual(rec.width, 4)
        self.assertEqual(rec.height, 5)
        self.assertEqual(rec.motionPhysics.velocity, Dim2D(2, 2))
        self.assertEqual(rec.motionPhysics.acceleration, Dim2D(-5 / 4.5, 0))
        self.assertEqual(rec.motionPhysics.force, Dim2D(-5, 0))
        self.assertEqual(rec.motionPhysics.momentum, Dim2D(9, 9))
        self.assertEqual(rec.motionPhysics.mass, 4.5)

    def test_updateMotionPhysics(self):
        pos = Dim2D(3, 5)
        point = Point(pos)
        vel = Dim2D(2, 2)
        point.addMotionPhysics(MotionPhysics2D(vel))
        self.assertEqual(point.position, Dim2D(3, 5))
        self.assertEqual(point.motionPhysics.velocity, Dim2D(2, 2))
        for i in range(20):
            point.updateMotionPhysics()
            self.assertEqual(point.position, Dim2D(3 + 2*(i+1), 5 + 2*(i+1)))
            self.assertEqual(point.motionPhysics.velocity, Dim2D(2, 2))

    def test_updateMotionPhysicsWithRectangle(self):
        pos = Dim2D(3, 5)
        width, height = 4, 5
        rec = Rectangle(pos, width, height)
        vel = Dim2D(2, 2)
        mass = 4.5
        force = Dim2D(-5, 0)
        rec.addMotionPhysics(MotionPhysics2D(vel, force=force, mass=mass))
        self.assertEqual(rec.top_left_corner, Dim2D(3, 5))
        self.assertEqual(rec.width, 4)
        self.assertEqual(rec.height, 5)
        self.assertEqual(rec.motionPhysics.velocity, Dim2D(2, 2))
        self.assertEqual(rec.motionPhysics.acceleration, Dim2D(-5 / 4.5, 0))
        self.assertEqual(rec.motionPhysics.force, Dim2D(-5, 0))
        self.assertEqual(rec.motionPhysics.momentum, Dim2D(9, 9))
        self.assertEqual(rec.motionPhysics.mass, 4.5)
        rec.updateMotionPhysics()
        self.assertEqual(rec.top_left_corner, Dim2D(5, 7))
        self.assertEqual(rec.width, 4)
        self.assertEqual(rec.height, 5)
        self.assertEqual(rec.motionPhysics.velocity, Dim2D(2, 2))
        self.assertEqual(rec.motionPhysics.acceleration, Dim2D(0, 0))
        self.assertEqual(rec.motionPhysics.force, Dim2D(0, 0))
        self.assertEqual(rec.motionPhysics.momentum, Dim2D(9, 9))
        self.assertEqual(rec.motionPhysics.mass, 4.5)
        rec.updateMotionPhysics(newForce=Dim2D(4.5, 4.5))
        self.assertEqual(rec.top_left_corner, Dim2D(8, 10))
        self.assertEqual(rec.width, 4)
        self.assertEqual(rec.height, 5)
        self.assertEqual(rec.motionPhysics.velocity, Dim2D(3, 3))
        self.assertEqual(rec.motionPhysics.acceleration, Dim2D(1, 1))
        self.assertEqual(rec.motionPhysics.force, Dim2D(4.5, 4.5))
        self.assertEqual(rec.motionPhysics.momentum, Dim2D(13.5, 13.5))
        self.assertEqual(rec.motionPhysics.mass, 4.5)

if __name__ == "__main__":
    unittest.main()
