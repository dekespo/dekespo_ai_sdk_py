import sys
sys.path.insert(0, "core/")

import unittest
from dimensions import *

class Dimensions2D(unittest.TestCase):
    def test1(self):
        pos = Dim2D(2, 3)
        self.assertEqual(pos.x, 2)
        self.assertEqual(pos.y, 3)
        self.assertEqual(str(pos), "x: 2, y: 3")

class Dimensions3D(unittest.TestCase):
    def test1(self):
        pos = Dim3D(2, 3, 4)
        self.assertEqual(pos.x, 2)
        self.assertEqual(pos.y, 3)
        self.assertEqual(pos.z, 4)
        self.assertEqual(str(pos), "x: 2, y: 3, z: 4")

if __name__ == "__main__":
    unittest.main()
