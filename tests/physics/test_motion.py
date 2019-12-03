import unittest

from core.dimensions import Dim2D
from core.shapes import Point

from physics.motion import Motion2D

# TODO: Add tests with rectangle and circle
class MotionPhysics2DTest(unittest.TestCase):
    def test_velocity(self):
        position = Dim2D(3, 5)
        point = Point(position)
        motion = Motion2D(point)
        motion.velocity = Dim2D(2, 2)
        self.assertEqual(motion.position, Dim2D(3, 5))
        self.assertEqual(motion.velocity, Dim2D(2, 2))

    def test_all_motion_fields(self):
        position = Dim2D(3, 5)
        point = Point(position)
        motion = Motion2D(point)
        motion.velocity = Dim2D(2, 2)
        motion.acceleration = Dim2D(1, -1)
        motion.force = Dim2D(-5, 0)
        motion.momentum = Dim2D(-9, 9)
        motion.mass = 6.5
        self.assertEqual(motion.position, Dim2D(3, 5))
        self.assertEqual(motion.position, Dim2D(3, 5))
        self.assertEqual(motion.velocity, Dim2D(2, 2))
        self.assertEqual(motion.acceleration, Dim2D(1, -1))
        self.assertEqual(motion.force, Dim2D(-5, 0))
        self.assertEqual(motion.momentum, Dim2D(-9, 9))
        self.assertEqual(motion.mass, 6.5)

    def test_update_motion(self):
        position = Dim2D(3, 5)
        point = Point(position)
        motion = Motion2D(point)
        motion.velocity = Dim2D(2, 2)
        self.assertEqual(motion.position, Dim2D(3, 5))
        self.assertEqual(motion.velocity, Dim2D(2, 2))
        for time in range(20):
            motion.update()
            self.assertEqual(motion.position, Dim2D(3 + 2*(time+1), 5 + 2*(time+1)))
            self.assertEqual(motion.velocity, Dim2D(2, 2))

if __name__ == "__main__":
    unittest.main()
