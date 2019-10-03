import math

import unittest

from py_ai_sdk.core.dimensions import Dim2D
from py_ai_sdk.core.maximum_minimum import getMaximumMinimumValues

class maximumMinimumTest(unittest.TestCase):
    def test_getMaximumValues(self):
        def localSqrtFunction(value):
            return math.sqrt(Dim2D.toNumberValue(value))
        maximumValue = -1
        extraParameters = {}
        poses1 = [Dim2D(1, 1), Dim2D(2, 2), Dim2D(3, 3)]
        maximumValue1, chosenValue1 = getMaximumMinimumValues(poses1, maximumValue, localSqrtFunction, ">", **extraParameters)
        self.assertEqual(maximumValue1, math.sqrt(3))
        self.assertEqual(chosenValue1, Dim2D(3, 3))
        poses2 = [Dim2D(1, 1), Dim2D(2, 2), Dim2D(3, 3), Dim2D(4, 0)]
        maximumValue2, chosenValue2 = getMaximumMinimumValues(poses2, maximumValue, localSqrtFunction, ">", **extraParameters)
        self.assertEqual(maximumValue2, math.sqrt(4))
        self.assertEqual(chosenValue2, Dim2D(4, 0))

    def test_getMaximumValuesWithExtraParameters(self):
        def localDim2DDistanceFunction(value, **extraParameters):
            myPoint = extraParameters["myPoint"]
            return Dim2D.get_euclid_distance(value, myPoint)
        maximumValue = -1
        extraParameters = {"myPoint": Dim2D(-2, -2)}
        poses1 = [Dim2D(1, 1), Dim2D(2, 2), Dim2D(3, 3)]
        maximumValue1, chosenValue1 = getMaximumMinimumValues(poses1, maximumValue, localDim2DDistanceFunction, ">", **extraParameters)
        self.assertEqual(maximumValue1, math.sqrt(50))
        self.assertEqual(chosenValue1, Dim2D(3, 3))
        poses2 = [Dim2D(1, 1), Dim2D(2, 2), Dim2D(3, 3), Dim2D(4, 0)]
        maximumValue2, chosenValue2 = getMaximumMinimumValues(poses2, maximumValue, localDim2DDistanceFunction, ">", **extraParameters)
        self.assertEqual(maximumValue2, math.sqrt(50))
        self.assertEqual(chosenValue2, Dim2D(3, 3))

if __name__ == "__main__":
    unittest.main()
