import sys
sys.path.insert(0, "core/")

import unittest
from dimensions import Dim2D
from motionPhysics import *

class MotionPhysicsTest(unittest.TestCase):
    def test_velocity(self):
        pos = Dim2D(3, 5)
        vel = Dim2D(2, 2)
        obj = MotionPhysics2D(pos, vel)
        self.assertEqual(obj.position, Dim2D(3, 5))
        self.assertEqual(obj.velocity, Dim2D(2, 2))

# TODO: Some of these values should be changed according to the new input conditions
    def test_all(self):
        pos = Dim2D(3, 5)
        vel = Dim2D(2, 2)
        acc = Dim2D(1, -1)
        force = Dim2D(-5, 0)
        momentum = Dim2D(-9, 9)
        mass = 6.5
        obj = MotionPhysics2D(pos, vel, acc, force, momentum, mass)
        self.assertEqual(obj.position, Dim2D(3, 5))
        self.assertEqual(obj.velocity, Dim2D(2, 2))
        self.assertEqual(obj.acceleration, Dim2D(1, -1))
        self.assertEqual(obj.force, Dim2D(-5, 0))
        self.assertEqual(obj.momentum, Dim2D(-9, 9))
        self.assertEqual(obj.mass, 6.5)

    def test_random1(self):
        pos = Dim2D(3, 5)
        vel = Dim2D(2, 2)
        acc = Dim2D(1, -1)
        mass = 6.5
        obj = MotionPhysics2D(pos, vel, acceleration=acc, mass=mass)
        self.assertEqual(obj.position, Dim2D(3, 5))
        self.assertEqual(obj.velocity, Dim2D(2, 2))
        self.assertEqual(obj.acceleration, Dim2D(1, -1))
        self.assertEqual(obj.mass, 6.5)

    def test_random2(self):
        pos = Dim2D(3, 5)
        vel = Dim2D(2, 2)
        force = Dim2D(-5, 0)
        momentum = Dim2D(-9, 9)
        obj = MotionPhysics2D(pos, vel, force=force, momentum=momentum)
        self.assertEqual(obj.position, Dim2D(3, 5))
        self.assertEqual(obj.velocity, Dim2D(2, 2))
        self.assertEqual(obj.force, Dim2D(-5, 0))
        self.assertEqual(obj.momentum, Dim2D(-9, 9))

if __name__ == "__main__":
    unittest.main()