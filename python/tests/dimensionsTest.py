import sys
sys.path.insert(0, "core/")

import unittest
from dimensions import *

class Dimensions2D(unittest.TestCase):
    def test_simple(self):
        pos = Dim2D(2, 3)
        self.assertEqual(pos.x, 2)
        self.assertEqual(pos.y, 3)
    
    def test_listToDim2Ds(self):
        liste = [(2, 3), (0, 0), (-4, -5)]
        dim2Dlist = Dim2D.listToDim2Ds(liste)
        for idx, pos in enumerate(dim2Dlist):
            self.assertEqual(pos, Dim2D(liste[idx][0], liste[idx][1]))

    def test_multiply(self):
        vecA = Dim2D(2, 3)
        vecB = Dim2D(-1, 1)
        const = 5
        self.assertEqual(vecA.vectoralMultiply(vecB), Dim2D(-2, 3))
        self.assertEqual(vecB.vectoralMultiply(vecA), Dim2D(-2, 3))
        self.assertEqual(vecA.vectoralMultiply(vecA), Dim2D(4, 9))
        self.assertEqual(vecA.constantMultiply(const), Dim2D(10, 15))
        self.assertEqual(vecB.constantMultiply(const), Dim2D(-5, 5))

    def test_divide(self):
        vecA = Dim2D(2, 3)
        vecB = Dim2D(-1, 1)
        const = 5
        self.assertEqual(vecA.vectoralDivide(vecB), Dim2D(-2, 3))
        self.assertEqual(vecB.vectoralDivide(vecA), Dim2D(-1/2, 1/3))
        self.assertEqual(vecA.vectoralDivide(vecA), Dim2D(1, 1))
        self.assertEqual(vecA.constantDivide(const), Dim2D(2/5, 3/5))
        self.assertEqual(vecB.constantDivide(const), Dim2D(-1/5, 1/5))

    def test_toNumberValue(self):
        dim1 = Dim2D(2, 2)
        dim2 = Dim2D(3, 0)
        dim3 = Dim2D(0, -3)
        dim4 = Dim2D(0, 0)
        self.assertEqual(Dim2D.toNumberValue(dim1), 2)
        self.assertEqual(Dim2D.toNumberValue(dim2), 3)
        self.assertEqual(Dim2D.toNumberValue(dim3), -3)
        self.assertEqual(Dim2D.toNumberValue(dim4), 0)
        with self.assertRaises(AssertionError) as exception:
            dim5 = Dim2D(2, 1)
            Dim2D.toNumberValue(dim5)
            self.assertEqual(exception.error_code, 3)

class Dimensions3D(unittest.TestCase):
    def test_simple(self):
        pos = Dim3D(2, 3, 4)
        self.assertEqual(pos.x, 2)
        self.assertEqual(pos.y, 3)
        self.assertEqual(pos.z, 4)

if __name__ == "__main__":
    unittest.main()
