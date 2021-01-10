import unittest

from dekespo_ai_sdk.core.dimensions import Dim2D
from dekespo_ai_sdk.core.neighbour import Neighbour, NeighbourData, NeighbourType


class NeighbourTest(unittest.TestCase):
    def test_get_neighbours_cross(self):
        pos = Dim2D(1, 1)
        poses_dic = dict(Neighbour.get_neighbours_cross(pos, lambda *_: True))
        self.assertEqual(len(poses_dic), 4)
        self.assertIn(Dim2D(0, 1), poses_dic)
        self.assertEqual(poses_dic[Dim2D(0, 1)], 1)
        self.assertIn(Dim2D(1, 2), poses_dic)
        self.assertEqual(poses_dic[Dim2D(1, 2)], 1)
        self.assertIn(Dim2D(2, 1), poses_dic)
        self.assertEqual(poses_dic[Dim2D(2, 1)], 1)
        self.assertIn(Dim2D(1, 0), poses_dic)
        self.assertEqual(poses_dic[Dim2D(1, 0)], 1)

    def test_get_neighbours_square(self):
        pos = Dim2D(1, 1)
        poses_dic = dict(Neighbour.get_neighbours_square(pos, lambda *_: True))
        self.assertEqual(len(poses_dic), 8)
        self.assertIn(Dim2D(0, 1), poses_dic)
        self.assertEqual(poses_dic[Dim2D(0, 1)], 1)
        self.assertIn(Dim2D(1, 2), poses_dic)
        self.assertEqual(poses_dic[Dim2D(1, 2)], 1)
        self.assertIn(Dim2D(2, 1), poses_dic)
        self.assertEqual(poses_dic[Dim2D(2, 1)], 1)
        self.assertIn(Dim2D(1, 0), poses_dic)
        self.assertEqual(poses_dic[Dim2D(1, 0)], 1)
        self.assertIn(Dim2D(0, 0), poses_dic)
        self.assertEqual(poses_dic[Dim2D(0, 0)], 2)
        self.assertIn(Dim2D(2, 2), poses_dic)
        self.assertEqual(poses_dic[Dim2D(2, 2)], 2)
        self.assertIn(Dim2D(0, 2), poses_dic)
        self.assertEqual(poses_dic[Dim2D(0, 2)], 2)
        self.assertIn(Dim2D(2, 0), poses_dic)
        self.assertEqual(poses_dic[Dim2D(2, 0)], 2)

    def test_get_neighbours_diamond(self):
        pos = Dim2D(1, 1)
        poses_dic = dict(
            Neighbour.get_neighbours_diamond(
                pos,
                lambda *_: True,
                NeighbourData(NeighbourType.DIAMOND, radius=2),
            )
        )
        self.assertEqual(len(poses_dic), 12)
        self.assertIn(Dim2D(0, 1), poses_dic)
        self.assertEqual(poses_dic[Dim2D(0, 1)], 1)
        self.assertIn(Dim2D(-1, 1), poses_dic)
        self.assertEqual(poses_dic[Dim2D(-1, 1)], 2)
        self.assertIn(Dim2D(1, 2), poses_dic)
        self.assertEqual(poses_dic[Dim2D(1, 2)], 1)
        self.assertIn(Dim2D(1, 3), poses_dic)
        self.assertEqual(poses_dic[Dim2D(1, 3)], 2)
        self.assertIn(Dim2D(2, 1), poses_dic)
        self.assertEqual(poses_dic[Dim2D(2, 1)], 1)
        self.assertIn(Dim2D(3, 1), poses_dic)
        self.assertEqual(poses_dic[Dim2D(3, 1)], 2)
        self.assertIn(Dim2D(2, 0), poses_dic)
        self.assertEqual(poses_dic[Dim2D(2, 0)], 2)
        self.assertIn(Dim2D(1, -1), poses_dic)
        self.assertEqual(poses_dic[Dim2D(1, -1)], 2)
        self.assertIn(Dim2D(0, 0), poses_dic)
        self.assertEqual(poses_dic[Dim2D(0, 0)], 2)
        self.assertIn(Dim2D(2, 2), poses_dic)
        self.assertEqual(poses_dic[Dim2D(2, 2)], 2)
        self.assertIn(Dim2D(0, 2), poses_dic)
        self.assertEqual(poses_dic[Dim2D(0, 2)], 2)
        self.assertIn(Dim2D(2, 0), poses_dic)
        self.assertEqual(poses_dic[Dim2D(2, 0)], 2)


if __name__ == "__main__":
    unittest.main()
