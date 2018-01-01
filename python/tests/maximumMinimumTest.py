import sys
import math
sys.path.insert(0, "core/")

import unittest
from dimensions import Dim2D
from maximumMinimum import *

class maximumMinimumTest(unittest.TestCase):
    def test_getMininumValues(self):
        def localSqrtFunction(value):
            return math.sqrt(Dim2D.toNumberValue(value))
        minimumValue = 100
        poses1 = [Dim2D(1, 1), Dim2D(2, 2), Dim2D(3, 3)]
        minimumValue1, chosenValue1 = getMaximumMinimumValues(poses1, minimumValue, localSqrtFunction, "<")
        self.assertEqual(minimumValue1, math.sqrt(1))
        self.assertEqual(chosenValue1, Dim2D(1, 1))
        poses2 = [Dim2D(1, 1), Dim2D(2, 2), Dim2D(3, 3), Dim2D(0, 0)]
        minimumValue2, chosenValue2 = getMaximumMinimumValues(poses2, minimumValue, localSqrtFunction, "<")
        self.assertEqual(minimumValue2, 0)
        self.assertEqual(chosenValue2, Dim2D(0, 0))

    def test_getMaximumValues(self):
        def localSqrtFunction(value):
            return math.sqrt(Dim2D.toNumberValue(value))
        maximumValue = -1
        poses1 = [Dim2D(1, 1), Dim2D(2, 2), Dim2D(3, 3)]
        maximumValue1, chosenValue1 = getMaximumMinimumValues(poses1, maximumValue, localSqrtFunction, ">")
        self.assertEqual(maximumValue1, math.sqrt(3))
        self.assertEqual(chosenValue1, Dim2D(3, 3))
        poses2 = [Dim2D(1, 1), Dim2D(2, 2), Dim2D(3, 3), Dim2D(4, 0)]
        maximumValue2, chosenValue2 = getMaximumMinimumValues(poses2, maximumValue, localSqrtFunction, ">")
        self.assertEqual(maximumValue2, math.sqrt(4))
        self.assertEqual(chosenValue2, Dim2D(4, 0))

if __name__ == "__main__":
    unittest.main()
