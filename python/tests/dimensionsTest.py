import sys
sys.path.insert(0, "core/")

import unittest
from dimensions import *

class Dimensions2D(unittest.TestCase):
    def test1(self):
        pos = Dim2D(2, 3)
        self.assertEqual(pos.x, 2)
        self.assertEqual(pos.y, 3)
    
    def testListToDim2Ds(self):
        liste = [(2, 3), (0, 0), (-4, -5)]
        dim2Dlist = Dim2D.listToDim2Ds(liste)
        for idx, pos in enumerate(dim2Dlist):
            self.assertEqual(pos, Dim2D(liste[idx][0], liste[idx][1]))

class Dimensions3D(unittest.TestCase):
    def test1(self):
        pos = Dim3D(2, 3, 4)
        self.assertEqual(pos.x, 2)
        self.assertEqual(pos.y, 3)
        self.assertEqual(pos.z, 4)

if __name__ == "__main__":
    unittest.main()
