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

    def test_acceleration_with_no_initial_velocity(self):
        position = Dim2D(2, 3)
        point = Point(position)
        motion = Motion2D(point)
        motion.acceleration = Dim2D(3, 2)
        self.assertEqual(motion.position, Dim2D(2, 3))
        self.assertEqual(motion.velocity, Dim2D(0, 0))
        self.assertEqual(motion.acceleration, Dim2D(3, 2))

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
        self.assertEqual(motion.velocity, Dim2D(2, 2))
        self.assertEqual(motion.acceleration, Dim2D(1, -1))
        self.assertEqual(motion.force, Dim2D(-5, 0))
        self.assertEqual(motion.momentum, Dim2D(-9, 9))
        self.assertEqual(motion.mass, 6.5)
        self.assertEqual(
            str(motion),
            ("Position: (x: 3, y: 5)\nVelocity: (x: 2, y: 2)\n"
             "Acceleration: (x: 1, y: -1)\nForce: (x: -5, y: 0)\n"
             "Momentum: (x: -9, y: 9)\nMass: 6.5")
        )

    def test_update_motion(self):
        position = Dim2D(3, 5)
        point = Point(position)

        motion_with_constant_velocity = Motion2D(point)
        motion_with_constant_velocity.velocity = Dim2D(2, 2)

        motion_with_constant_acceleration = Motion2D(point)
        motion_with_constant_acceleration.velocity = Dim2D(-1, 2)
        motion_with_constant_acceleration.acceleration = Dim2D(1, 3)

        for time in range(1, 21):
            motion_with_constant_velocity.update()
            self.assertEqual(
                motion_with_constant_velocity.position,
                Dim2D(3, 5) + Dim2D(2, 2).constant_multiply(time)
            )
            self.assertEqual(motion_with_constant_velocity.velocity, Dim2D(2, 2))

            motion_with_constant_acceleration.update()
            self.assertEqual(
                motion_with_constant_acceleration.velocity,
                Dim2D(-1, 2) + Dim2D(1, 3).constant_multiply(time)
            )
            self.assertEqual(
                motion_with_constant_acceleration.position,
                Dim2D(3, 5) + Dim2D(-1, 2).constant_multiply(time) + \
                    Dim2D(1, 3).constant_multiply(0.5 * time * time)
            )

if __name__ == "__main__":
    unittest.main()
