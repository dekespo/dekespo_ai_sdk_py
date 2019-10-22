import unittest

from py_ai_sdk.core.dimensions import Dim2D
from py_ai_sdk.core.shapes import Rectangle
from py_ai_sdk.core.neighbours import get_neighbours2d_rectangle_4_sides, get_neighbours2d_rectangle_8_sides, get_available_neighbours2d_rectangle

class RectangleNeighboursTest(unittest.TestCase):
    def test_rectangle_get_4_sides(self):
        pos = Dim2D(1, 1)
        poses = get_neighbours2d_rectangle_4_sides(pos)
        self.assertEqual(len(poses), 4)
        self.assertTrue(Dim2D(0, 1) in poses)
        self.assertTrue(Dim2D(1, 2) in poses)
        self.assertTrue(Dim2D(2, 1) in poses)
        self.assertTrue(Dim2D(1, 0) in poses)

    def test_rectangle_get_8_sides(self):
        pos = Dim2D(1, 1)
        poses = get_neighbours2d_rectangle_8_sides(pos)
        self.assertEqual(len(poses), 8)
        self.assertTrue(Dim2D(0, 1) in poses)
        self.assertTrue(Dim2D(1, 2) in poses)
        self.assertTrue(Dim2D(2, 1) in poses)
        self.assertTrue(Dim2D(1, 0) in poses)
        self.assertTrue(Dim2D(0, 0) in poses)
        self.assertTrue(Dim2D(2, 2) in poses)
        self.assertTrue(Dim2D(0, 2) in poses)
        self.assertTrue(Dim2D(2, 0) in poses)

    def test_available_rectangle_two_blocks(self):
        grid = Rectangle(Dim2D(0, 0), 3, 3)
        blocking_positions = Dim2D.convert_candiates_to_dimensions([(1, 1), (0, 1)])
        pos1 = Dim2D(0, 2)
        available_poses = get_available_neighbours2d_rectangle(grid, blocking_positions, get_neighbours2d_rectangle_4_sides, pos1)
        self.assertEqual(len(available_poses), 1)
        self.assertEqual(available_poses[0], Dim2D(1, 2))
        pos2 = Dim2D(1, 2)
        available_poses = get_available_neighbours2d_rectangle(grid, blocking_positions, get_neighbours2d_rectangle_4_sides, pos2)
        self.assertEqual(len(available_poses), 2)
        self.assertTrue(Dim2D(0, 2) in available_poses)
        self.assertTrue(Dim2D(2, 2) in available_poses)
        pos3 = Dim2D(2, 1)
        available_poses = get_available_neighbours2d_rectangle(grid, blocking_positions, get_neighbours2d_rectangle_8_sides, pos3)
        self.assertEqual(len(available_poses), 4)
        self.assertTrue(Dim2D(2, 0) in available_poses)
        self.assertTrue(Dim2D(2, 2) in available_poses)
        self.assertTrue(Dim2D(1, 0) in available_poses)
        self.assertTrue(Dim2D(1, 2) in available_poses)

    def test_available_rectangle_empty_map(self):
        grid = Rectangle(Dim2D(0, 0), 3, 3)
        blocking_positions = Dim2D.convert_candiates_to_dimensions([])
        pos1 = Dim2D(1, 1)
        available_poses = get_available_neighbours2d_rectangle(grid, blocking_positions, get_neighbours2d_rectangle_4_sides, pos1)
        self.assertEqual(len(available_poses), 4)
        self.assertTrue(Dim2D(0, 1) in available_poses)
        self.assertTrue(Dim2D(1, 2) in available_poses)
        self.assertTrue(Dim2D(2, 1) in available_poses)
        self.assertTrue(Dim2D(1, 0) in available_poses)
        available_poses = get_available_neighbours2d_rectangle(grid, blocking_positions, get_neighbours2d_rectangle_8_sides, pos1)
        self.assertEqual(len(available_poses), 8)
        self.assertTrue(Dim2D(0, 1) in available_poses)
        self.assertTrue(Dim2D(1, 2) in available_poses)
        self.assertTrue(Dim2D(2, 1) in available_poses)
        self.assertTrue(Dim2D(1, 0) in available_poses)
        self.assertTrue(Dim2D(0, 0) in available_poses)
        self.assertTrue(Dim2D(2, 2) in available_poses)
        self.assertTrue(Dim2D(0, 2) in available_poses)
        self.assertTrue(Dim2D(2, 0) in available_poses)


if __name__ == "__main__":
    unittest.main()
