import sys
sys.path.insert(0, "core/")

import unittest
from dimensions import Dim2D
from shapes import *
from neighbours import *

class RectangleNeighbours4SidesTest(unittest.TestCase):
    def test_rectangleGet4Sides(self):
        pos = Dim2D(1,1)
        poses = getNeighbours2D_rectangle_4Sides(pos)
        self.assertEqual(len(poses), 4)
        self.assertTrue(Dim2D(0, 1) in poses)
        self.assertTrue(Dim2D(1, 2) in poses)
        self.assertTrue(Dim2D(2, 1) in poses)
        self.assertTrue(Dim2D(1, 0) in poses)

    def test_rectangleGet8Sides(self):
        pos = Dim2D(1,1)
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
        map = Rectangle(Dim2D(0, 0), 3, 3)
        blockingPositions = Dim2D.listToDim2Ds([(1,1), (0, 1)])
        pos1 = Dim2D(0, 2)
        availablePoses = getAvailableNeighbours2D_rectangle_4Sides(map, blockingPositions, pos1)
        self.assertEqual(len(availablePoses), 1)
        self.assertEqual(availablePoses[0], Dim2D(1, 2))
        pos2 = Dim2D(1, 2)
        availablePoses = getAvailableNeighbours2D_rectangle_4Sides(map, blockingPositions, pos2)
        self.assertEqual(len(availablePoses), 2)
        self.assertTrue(Dim2D(0, 2) in availablePoses)
        self.assertTrue(Dim2D(2, 2) in availablePoses)

    def test_availableRectangleEmptyMap(self):
        map = Rectangle(Dim2D(0, 0), 3, 3)
        blockingPositions = Dim2D.listToDim2Ds([])
        pos1 = Dim2D(1, 1)
        availablePoses = getAvailableNeighbours2D_rectangle_4Sides(map, blockingPositions, pos1)
        self.assertEqual(len(availablePoses), 4)
        self.assertTrue(Dim2D(0, 1) in availablePoses)
        self.assertTrue(Dim2D(1, 2) in availablePoses)
        self.assertTrue(Dim2D(2, 1) in availablePoses)
        self.assertTrue(Dim2D(1, 0) in availablePoses)

if __name__ == "__main__":
    unittest.main()

