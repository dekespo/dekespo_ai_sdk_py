import unittest

from core.dimensions import Dim2D
from core.neighbour import Neighbour

class NeighbourTest(unittest.TestCase):
    def test_get_neighbours_cross(self):
        pos = Dim2D(1, 1)
        poses = Neighbour.get_neighbours_cross(pos, lambda *_: True)
        poses = list(poses)
        self.assertEqual(len(poses), 4)
        self.assertTrue(Dim2D(0, 1) in poses)
        self.assertTrue(Dim2D(1, 2) in poses)
        self.assertTrue(Dim2D(2, 1) in poses)
        self.assertTrue(Dim2D(1, 0) in poses)

    def test_get_neighbours_square(self):
        pos = Dim2D(1, 1)
        poses = Neighbour.get_neighbours_square(pos, lambda *_: True)
        poses = list(poses)
        self.assertEqual(len(poses), 8)
        self.assertTrue(Dim2D(0, 1) in poses)
        self.assertTrue(Dim2D(1, 2) in poses)
        self.assertTrue(Dim2D(2, 1) in poses)
        self.assertTrue(Dim2D(1, 0) in poses)
        self.assertTrue(Dim2D(0, 0) in poses)
        self.assertTrue(Dim2D(2, 2) in poses)
        self.assertTrue(Dim2D(0, 2) in poses)
        self.assertTrue(Dim2D(2, 0) in poses)

    def test_get_neighbours_diamond(self):
        pos = Dim2D(1, 1)
        poses = Neighbour.get_neighbours_diamond(
            pos,
            lambda *_: True,
            Neighbour.Data(Neighbour.Data.Type.DIAMOND, radius=2)
        )
        poses = list(poses)
        self.assertEqual(len(poses), 12)
        self.assertTrue(Dim2D(0, 1) in poses)
        self.assertTrue(Dim2D(-1, 1) in poses)
        self.assertTrue(Dim2D(1, 2) in poses)
        self.assertTrue(Dim2D(1, 3) in poses)
        self.assertTrue(Dim2D(2, 1) in poses)
        self.assertTrue(Dim2D(3, 1) in poses)
        self.assertTrue(Dim2D(1, 0) in poses)
        self.assertTrue(Dim2D(1, -1) in poses)
        self.assertTrue(Dim2D(0, 0) in poses)
        self.assertTrue(Dim2D(2, 2) in poses)
        self.assertTrue(Dim2D(0, 2) in poses)
        self.assertTrue(Dim2D(2, 0) in poses)

if __name__ == "__main__":
    unittest.main()
