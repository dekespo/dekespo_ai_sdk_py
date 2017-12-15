
import sys
sys.path.insert(0, "../code/")

import unittest
from dimensions import *

class GeometryTest(unittest.TestCase):
    def testDim2D_1(self):
        pos = Dim2D(2, 3)
        self.assertEqual(pos.x, 2)
        self.assertEqual(pos.y, 3)

    def testDim3D_1(self):
        pos = Dim3D(2, 3, 4)
        self.assertEqual(pos.x, 2)
        self.assertEqual(pos.y, 3)
        self.assertEqual(pos.z, 4)

if __name__ == "__main__":
    unittest.main()