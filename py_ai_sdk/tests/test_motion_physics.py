import unittest

from py_ai_sdk.core.dimensions import Dim2D
from py_ai_sdk.core.shapes import Point
from py_ai_sdk.core.motion_physics import MotionPhysics2D

class MotionPhysics2DTest(unittest.TestCase):
    def test_velocity(self):
        position = Dim2D(3, 5)
        point = Point(position)
        motion_physics = MotionPhysics2D(position)
        motion_physics.velocity = Dim2D(2, 2)
        point.set_motion_physics(motion_physics)
        self.assertEqual(point.position, Dim2D(3, 5))
        self.assertEqual(point.motion_physics.position, Dim2D(3, 5))
        self.assertEqual(point.motion_physics.velocity, Dim2D(2, 2))

    def test_all_physics(self):
        position = Dim2D(3, 5)
        point = Point(position)
        motion_physics = MotionPhysics2D(position)
        motion_physics.velocity = Dim2D(2, 2)
        motion_physics.acceleration = Dim2D(1, -1)
        motion_physics.force = Dim2D(-5, 0)
        motion_physics.momentum = Dim2D(-9, 9)
        motion_physics.mass = 6.5
        point.set_motion_physics(motion_physics)
        self.assertEqual(point.position, Dim2D(3, 5))
        self.assertEqual(point.motion_physics.position, Dim2D(3, 5))
        self.assertEqual(point.motion_physics.velocity, Dim2D(2, 2))
        self.assertEqual(point.motion_physics.acceleration, Dim2D(1, -1))
        self.assertEqual(point.motion_physics.force, Dim2D(-5, 0))
        self.assertEqual(point.motion_physics.momentum, Dim2D(-9, 9))
        self.assertEqual(point.motion_physics.mass, 6.5)

    def test_update_motion_physics(self):
        position = Dim2D(3, 5)
        point = Point(position)
        motion_phyiscs = MotionPhysics2D(position)
        motion_phyiscs.velocity = Dim2D(2, 2)
        point.set_motion_physics(motion_phyiscs)
        self.assertEqual(point.position, Dim2D(3, 5))
        self.assertEqual(point.position, Dim2D(3, 5))
        self.assertEqual(point.motion_physics.velocity, Dim2D(2, 2))
        for i in range(20):
            point.update_motion_physics()
            self.assertEqual(point.position, Dim2D(3 + 2*(i+1), 5 + 2*(i+1)))
            self.assertEqual(point.motion_physics.velocity, Dim2D(2, 2))

if __name__ == "__main__":
    unittest.main()
