import unittest

from py_ai_sdk.core.dimensions import Dim2D
from py_ai_sdk.core.shapes import Rectangle
from py_ai_sdk.core.neighbours import getNeighbours2D_rectangle_4Sides, getNeighbours2D_rectangle_8Sides, getAvailableNeighbours2D_rectangle

class RectangleNeighboursTest(unittest.TestCase):
    def test_rectangleGet4Sides(self):
        pos = Dim2D(1, 1)
        poses = getNeighbours2D_rectangle_4Sides(pos)
        self.assertEqual(len(poses), 4)
        self.assertTrue(Dim2D(0, 1) in poses)
        self.assertTrue(Dim2D(1, 2) in poses)
        self.assertTrue(Dim2D(2, 1) in poses)
        self.assertTrue(Dim2D(1, 0) in poses)

    def test_rectangleGet8Sides(self):
        pos = Dim2D(1, 1)
        poses = getNeighbours2D_rectangle_8Sides(pos)
        self.assertEqual(len(poses), 8)
        self.assertTrue(Dim2D(0, 1) in poses)
        self.assertTrue(Dim2D(1, 2) in poses)
        self.assertTrue(Dim2D(2, 1) in poses)
        self.assertTrue(Dim2D(1, 0) in poses)
        self.assertTrue(Dim2D(0, 0) in poses)
        self.assertTrue(Dim2D(2, 2) in poses)
        self.assertTrue(Dim2D(0, 2) in poses)
        self.assertTrue(Dim2D(2, 0) in poses)

    def test_availableRectangleTwoBlocks(self):
        grid = Rectangle(Dim2D(0, 0), 3, 3)
        blockingPositions = Dim2D.convert_candiates_to_dimensions([(1, 1), (0, 1)])
        pos1 = Dim2D(0, 2)
        availablePoses = getAvailableNeighbours2D_rectangle(grid, blockingPositions, getNeighbours2D_rectangle_4Sides, pos1)
        self.assertEqual(len(availablePoses), 1)
        self.assertEqual(availablePoses[0], Dim2D(1, 2))
        pos2 = Dim2D(1, 2)
        availablePoses = getAvailableNeighbours2D_rectangle(grid, blockingPositions, getNeighbours2D_rectangle_4Sides, pos2)
        self.assertEqual(len(availablePoses), 2)
        self.assertTrue(Dim2D(0, 2) in availablePoses)
        self.assertTrue(Dim2D(2, 2) in availablePoses)
        pos3 = Dim2D(2, 1)
        availablePoses = getAvailableNeighbours2D_rectangle(grid, blockingPositions, getNeighbours2D_rectangle_8Sides, pos3)
        self.assertEqual(len(availablePoses), 4)
        self.assertTrue(Dim2D(2, 0) in availablePoses)
        self.assertTrue(Dim2D(2, 2) in availablePoses)
        self.assertTrue(Dim2D(1, 0) in availablePoses)
        self.assertTrue(Dim2D(1, 2) in availablePoses)

    def test_availableRectangleEmptyMap(self):
        grid = Rectangle(Dim2D(0, 0), 3, 3)
        blockingPositions = Dim2D.convert_candiates_to_dimensions([])
        pos1 = Dim2D(1, 1)
        availablePoses = getAvailableNeighbours2D_rectangle(grid, blockingPositions, getNeighbours2D_rectangle_4Sides, pos1)
        self.assertEqual(len(availablePoses), 4)
        self.assertTrue(Dim2D(0, 1) in availablePoses)
        self.assertTrue(Dim2D(1, 2) in availablePoses)
        self.assertTrue(Dim2D(2, 1) in availablePoses)
        self.assertTrue(Dim2D(1, 0) in availablePoses)
        availablePoses = getAvailableNeighbours2D_rectangle(grid, blockingPositions, getNeighbours2D_rectangle_8Sides, pos1)
        self.assertEqual(len(availablePoses), 8)
        self.assertTrue(Dim2D(0, 1) in availablePoses)
        self.assertTrue(Dim2D(1, 2) in availablePoses)
        self.assertTrue(Dim2D(2, 1) in availablePoses)
        self.assertTrue(Dim2D(1, 0) in availablePoses)
        self.assertTrue(Dim2D(0, 0) in availablePoses)
        self.assertTrue(Dim2D(2, 2) in availablePoses)
        self.assertTrue(Dim2D(0, 2) in availablePoses)
        self.assertTrue(Dim2D(2, 0) in availablePoses)


if __name__ == "__main__":
    unittest.main()
