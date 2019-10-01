import math

import unittest
from py_ai_sdk.core.dimensions import Dim2D, Dim3D

class Dimensions2D(unittest.TestCase):
    def test_simple(self):
        pos = Dim2D(2, 3)
        self.assertEqual(pos.x, 2)
        self.assertEqual(pos.y, 3)

    def test_listToDim2Ds(self):
        liste = [(2, 3), (0, 0), (-4, -5)]
        dim2Dlist = Dim2D.convert_candiates_to_dimensions(liste)
        for idx, pos in enumerate(dim2Dlist):
            self.assertEqual(pos, Dim2D(liste[idx][0], liste[idx][1]))

    def test_add(self):
        dim1 = Dim2D(2, 3)
        dim2 = Dim2D(-1, 1)
        self.assertEqual(dim1 + dim2, Dim2D(1, 4))

    def test_round(self):
        dim = Dim2D(2.4, 3.7)
        dim.round()
        self.assertEqual(dim, Dim2D(2, 4))

    def test_multiply(self):
        vecA = Dim2D(2, 3)
        vecB = Dim2D(-1, 1)
        const = 5
        self.assertEqual(vecA.vectoral_multiply(vecB), Dim2D(-2, 3))
        self.assertEqual(vecB.vectoral_multiply(vecA), Dim2D(-2, 3))
        self.assertEqual(vecA.vectoral_multiply(vecA), Dim2D(4, 9))
        self.assertEqual(vecA.constant_multiply(const), Dim2D(10, 15))
        self.assertEqual(vecB.constant_multiply(const), Dim2D(-5, 5))

    def test_divide(self):
        vecA = Dim2D(2, 3)
        vecB = Dim2D(-1, 1)
        const = 5
        self.assertEqual(vecA.vectoral_divide(vecB), Dim2D(-2, 3))
        self.assertEqual(vecB.vectoral_divide(vecA), Dim2D(-1/2, 1/3))
        self.assertEqual(vecA.vectoral_divide(vecA), Dim2D(1, 1))
        self.assertEqual(vecA.constant_divide(const), Dim2D(2/5, 3/5))
        self.assertEqual(vecB.constant_divide(const), Dim2D(-1/5, 1/5))

    def test_toNumberValue(self):
        dim1 = Dim2D(2, 2)
        dim2 = Dim2D(3, 0)
        dim3 = Dim2D(0, -3)
        dim4 = Dim2D(0, 0)
        self.assertEqual(Dim2D.toNumberValue(dim1), 2)
        self.assertEqual(Dim2D.toNumberValue(dim2), 3)
        self.assertEqual(Dim2D.toNumberValue(dim3), -3)
        self.assertEqual(Dim2D.toNumberValue(dim4), 0)
        def error_method_check():
            dim5 = Dim2D(2, 1)
            Dim2D.toNumberValue(dim5)
        self.assertRaises(AssertionError, error_method_check)

    def test_getAverageOfDim2Ds(self):
        liste = [(2, 3), (0, 0), (-4, -5), (2, -2), (-5, 0)]
        dim2Dlist = Dim2D.convert_candiates_to_dimensions(liste)
        self.assertEqual(Dim2D.get_average_value(dim2Dlist), Dim2D(-1, -4 / 5))

    def test_getEuclidDistance(self):
        pos1 = Dim2D(0, 0)
        pos2 = Dim2D(1, 1)
        pos3 = Dim2D(-2, -1)
        pos4 = Dim2D(1, -2)
        pos5 = Dim2D(-3, 4)
        self.assertEqual(Dim2D.get_euclid_distance(pos1, pos2), math.sqrt(2))
        self.assertEqual(Dim2D.get_euclid_distance(pos2, pos3), math.sqrt(13))
        self.assertEqual(Dim2D.get_euclid_distance(pos3, pos4), math.sqrt(10))
        self.assertEqual(Dim2D.get_euclid_distance(pos4, pos5), math.sqrt(52))
        self.assertEqual(Dim2D.get_euclid_distance(pos3, pos3), 0)
        self.assertEqual(Dim2D.get_euclid_distance(pos1, pos3), Dim2D.get_euclid_distance(pos3, pos1))

    def test_getManathanDistance(self):
        pos1 = Dim2D(0, 0)
        pos2 = Dim2D(1, 1)
        pos3 = Dim2D(-2, -1)
        pos4 = Dim2D(1, -2)
        pos5 = Dim2D(-3, 4)
        self.assertEqual(Dim2D.get_manathan_distance(pos1, pos2), 2)
        self.assertEqual(Dim2D.get_manathan_distance(pos2, pos3), 5)
        self.assertEqual(Dim2D.get_manathan_distance(pos3, pos4), 4)
        self.assertEqual(Dim2D.get_manathan_distance(pos4, pos5), 10)
        self.assertEqual(Dim2D.get_manathan_distance(pos3, pos3), 0)
        self.assertEqual(Dim2D.get_manathan_distance(pos1, pos3), Dim2D.get_manathan_distance(pos3, pos1))

class Dimensions3D(unittest.TestCase):
    def test_simple(self):
        pos = Dim3D(2, 3, 4)
        self.assertEqual(pos.x, 2)
        self.assertEqual(pos.y, 3)
        self.assertEqual(pos.z, 4)

if __name__ == "__main__":
    unittest.main()
