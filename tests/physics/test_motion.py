import unittest

from core.dimensions import Dim2D
from core.shapes import Point

from physics.motion import Motion2D

# TODO: Add tests with rectangle and circle
class MotionPhysics2DTest(unittest.TestCase):
    def setUp(self):
        position = Dim2D(3, 5)
        self.point = Point(position)

    def test_position(self):
        motion = Motion2D(self.point)
        self.assertEqual(motion.position, Dim2D(3, 5))

    def test_velocity(self):
        motion = Motion2D(self.point, velocity=Dim2D(2, 2))
        self.assertEqual(motion.velocity, Dim2D(2, 2))

    def test_acceleration_with_no_initial_velocity(self):
        motion = Motion2D(self.point, acceleration=Dim2D(3, 2))
        self.assertEqual(motion.velocity, Dim2D(0, 0))
        self.assertEqual(motion.acceleration, Dim2D(3, 2))

    def test_momentum_and_mass(self):
        motion = Motion2D(self.point, velocity=Dim2D(-2, 5), mass=4.0)
        self.assertEqual(motion.mass, 4.0)
        self.assertEqual(motion.momentum, Dim2D(-8.0, 20.0))

    def test_all_motion_fields(self):
        motion = Motion2D(self.point, velocity=Dim2D(2, 2), acceleration=Dim2D(1, -1), mass=6.5)
        self.assertEqual(motion.velocity, Dim2D(2, 2))
        self.assertEqual(motion.acceleration, Dim2D(1, -1))
        self.assertEqual(motion.mass, 6.5)
        self.assertEqual(motion.momentum, Dim2D(13, 13))
        self.assertEqual(
            str(motion),
            ("Position: (x: 3, y: 5)\nVelocity: (x: 2, y: 2)\n"
             "Acceleration: (x: 1, y: -1)\nMass: 6.5\n"
             "Momentum: (x: 13.0, y: 13.0)")
        )

    def test_update_motion(self):
        motion_with_constant_velocity = Motion2D(self.point, velocity=Dim2D(2, 2))
        motion_with_constant_acceleration = Motion2D(
            self.point,
            velocity=Dim2D(-1, 2),
            acceleration=Dim2D(1, 3)
        )
        motion_for_constant_force = Motion2D(
            self.point,
            mass=2,
            acceleration=Dim2D(-1.5, 2),
            velocity=Dim2D(3.5, -2)
        )

        for time in range(1, 21):
            motion_with_constant_velocity.update()
            self.assertAlmostEqual(
                motion_with_constant_velocity.position,
                Dim2D(3, 5) + Dim2D(2, 2).constant_multiply(time)
            )
            self.assertAlmostEqual(motion_with_constant_velocity.velocity, Dim2D(2, 2))

            motion_with_constant_acceleration.update()
            self.assertAlmostEqual(
                motion_with_constant_acceleration.velocity,
                Dim2D(-1, 2) + Dim2D(1, 3).constant_multiply(time)
            )
            self.assertAlmostEqual(
                motion_with_constant_acceleration.position,
                Dim2D(3, 5) + Dim2D(-1, 2).constant_multiply(time) + \
                    Dim2D(1, 3).constant_multiply(0.5 * time * time)
            )

            motion_for_constant_force.apply_force(Dim2D(5, 5))
            motion_for_constant_force.update()
            self.assertAlmostEqual(
                motion_for_constant_force.acceleration,
                Dim2D(-1.5, 2) + Dim2D(5, 5).constant_divide(2).constant_multiply(time)
            )
            self.assertAlmostEqual(
                motion_for_constant_force.velocity,
                Dim2D(3.5, -2) + \
                    Dim2D(-1.5, 2).constant_multiply(time) + \
                        Dim2D(5, 5).constant_divide(2).constant_multiply(time * time * 0.5)
            )
            self.assertAlmostEqual(
                motion_for_constant_force.position,
                Dim2D(3, 5) + \
                    Dim2D(3.5, -2).constant_multiply(time) + \
                        Dim2D(-1.5, 2).constant_multiply(time * time * 0.5) + \
                            Dim2D(5, 5).constant_divide(2).constant_multiply(time ** 3 * 1/6)
            )

if __name__ == "__main__":
    unittest.main()
