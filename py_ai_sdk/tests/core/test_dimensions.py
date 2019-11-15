import math

import unittest
from py_ai_sdk.core.dimensions import Dim2D, Dim3D

class Dimensions2D(unittest.TestCase):
    def test_simple(self):
        pos = Dim2D(2, 3)
        self.assertEqual(pos.x, 2)
        self.assertEqual(pos.y, 3)

    def test_convert_candiates_to_dimensions(self):
        candidates = [(2, 3), (0, 0), (-4, -5)]
        dimensions = Dim2D.convert_candiates_to_dimensions(candidates)
        for index, dimension in enumerate(dimensions):
            self.assertEqual(dimension, Dim2D(candidates[index][0], candidates[index][1]))

    def test_add(self):
        dim1 = Dim2D(2, 3)
        dim2 = Dim2D(-1, 1)
        self.assertEqual(dim1 + dim2, Dim2D(1, 4))

    def test_multiply(self):
        vec1 = Dim2D(2, 3)
        vec2 = Dim2D(-1, 1)
        const = 5
        self.assertEqual(vec1.vectoral_multiply(vec2), Dim2D(-2, 3))
        self.assertEqual(vec2.vectoral_multiply(vec1), Dim2D(-2, 3))
        self.assertEqual(vec1.vectoral_multiply(vec1), Dim2D(4, 9))
        self.assertEqual(vec1.constant_multiply(const), Dim2D(10, 15))
        self.assertEqual(vec2.constant_multiply(const), Dim2D(-5, 5))

    def test_divide(self):
        vec1 = Dim2D(2, 3)
        vec2 = Dim2D(-1, 1)
        const = 5
        self.assertEqual(vec1.vectoral_divide(vec2), Dim2D(-2, 3))
        self.assertEqual(vec2.vectoral_divide(vec1), Dim2D(-1/2, 1/3))
        self.assertEqual(vec1.vectoral_divide(vec1), Dim2D(1, 1))
        self.assertEqual(vec1.constant_divide(const), Dim2D(2/5, 3/5))
        self.assertEqual(vec2.constant_divide(const), Dim2D(-1/5, 1/5))

    def test_get_average_value(self):
        candidates = [(2, 3), (0, 0), (-4, -5), (2, -2), (-5, 0)]
        dimensions = Dim2D.convert_candiates_to_dimensions(candidates)
        self.assertEqual(Dim2D.get_average_value(dimensions), Dim2D(-1, -4 / 5))

    def test_get_euclid_distance(self):
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
        self.assertEqual(
            Dim2D.get_euclid_distance(pos1, pos3),
            Dim2D.get_euclid_distance(pos3, pos1)
        )

    def test_get_manathan_distance(self):
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
        self.assertEqual(
            Dim2D.get_manathan_distance(pos1, pos3),
            Dim2D.get_manathan_distance(pos3, pos1)
        )

    def test_simple_get_minimum_index_and_value(self):
        def local_sqrt_function(value):
            return math.sqrt(value.x)
        poses1 = [Dim2D(1, 1), Dim2D(2, 2), Dim2D(3, 3)]
        chosen_pos1, minimum_value1 = Dim2D.get_minimum_index_and_value(poses1, local_sqrt_function)
        self.assertEqual(minimum_value1, 1)
        self.assertEqual(chosen_pos1, Dim2D(1, 1))
        poses2 = [Dim2D(1, 1), Dim2D(2, 2), Dim2D(3, 3), Dim2D(0, 0)]
        chosen_pos2, minimum_value2 = Dim2D.get_minimum_index_and_value(poses2, local_sqrt_function)
        self.assertEqual(minimum_value2, 0)
        self.assertEqual(chosen_pos2, Dim2D(0, 0))

    def test_get_minimum_index_and_value_with_extra_parameters(self):
        def local_distance_function(value, **extra_parameters):
            current_point = extra_parameters["current_point"]
            return Dim2D.get_euclid_distance(value, current_point)
        extra_parameters = {"current_point": Dim2D(-2, -2)}
        poses1 = [Dim2D(1, 1), Dim2D(2, 2), Dim2D(3, 3)]
        chosen_pos1, minimum_value1 = Dim2D.get_minimum_index_and_value(
            poses1,
            local_distance_function,
            **extra_parameters
        )
        self.assertEqual(minimum_value1, math.sqrt(18))
        self.assertEqual(chosen_pos1, Dim2D(1, 1))
        poses2 = [Dim2D(1, 1), Dim2D(-2, 2), Dim2D(3, 3), Dim2D(4, 0)]
        chosen_pos2, minimum_value2 = Dim2D.get_minimum_index_and_value(
            poses2,
            local_distance_function,
            **extra_parameters
        )
        self.assertEqual(minimum_value2, math.sqrt(16))
        self.assertEqual(chosen_pos2, Dim2D(-2, 2))

    def test_get_minimum_index_and_value_with_complex_criteria_function(self):
        def complex_function(value, **extra_parameters):
            point1 = extra_parameters["point1"]
            point2 = extra_parameters["point2"]
            if Dim2D.get_manathan_distance(value, point1) > 10:
                return 20
            if Dim2D.get_manathan_distance(value, point2) < 5:
                return 50
            return Dim2D.get_manathan_distance(value, point1) + \
                Dim2D.get_manathan_distance(value, point2)
        extra_parameters = {
            "point1": Dim2D(5, 5),
            "point2": Dim2D(0, 0)
        }
        poses1 = [Dim2D(2, 3), Dim2D(-1, -1), Dim2D(2, 2), Dim2D(3, 3)]
        chosen_pos1, minimum_value1 = Dim2D.get_minimum_index_and_value(
            poses1,
            complex_function,
            **extra_parameters
        )
        self.assertEqual(minimum_value1, 10)
        self.assertEqual(chosen_pos1, Dim2D(2, 3))
        poses2 = [Dim2D(1, 1), Dim2D(2, 2), Dim2D(3, 3), Dim2D(4, 4), Dim2D(0, 0)]
        chosen_pos2, minimum_value2 = Dim2D.get_minimum_index_and_value(
            poses2,
            complex_function,
            **extra_parameters
        )
        self.assertEqual(minimum_value2, 10)
        self.assertEqual(chosen_pos2, Dim2D(3, 3))

    def test_simple_get_maximum_index_and_value(self):
        def local_sqrt_function(value):
            return math.sqrt(value.x)
        poses1 = [Dim2D(1, 1), Dim2D(2, 2), Dim2D(3, 3)]
        chosen_pos1, maximum_value1 = Dim2D.get_maximum_index_and_value(poses1, local_sqrt_function)
        self.assertEqual(maximum_value1, math.sqrt(3))
        self.assertEqual(chosen_pos1, Dim2D(3, 3))
        poses2 = [Dim2D(1, 1), Dim2D(2, 2), Dim2D(3, 3), Dim2D(5, 5)]
        chosen_pos2, maximum_value2 = Dim2D.get_maximum_index_and_value(poses2, local_sqrt_function)
        self.assertEqual(maximum_value2, math.sqrt(5))
        self.assertEqual(chosen_pos2, Dim2D(5, 5))

    def test_get_maximum_index_and_value_with_extra_parameters(self):
        def local_distance_function(value, **extra_parameters):
            current_point = extra_parameters["current_point"]
            return Dim2D.get_euclid_distance(value, current_point)
        extra_parameters = {"current_point": Dim2D(-2, -2)}
        poses1 = [Dim2D(1, 1), Dim2D(2, 2), Dim2D(3, 3)]
        chosen_pos1, maximum_value1 = Dim2D.get_maximum_index_and_value(
            poses1,
            local_distance_function,
            **extra_parameters
        )
        self.assertEqual(maximum_value1, math.sqrt(50))
        self.assertEqual(chosen_pos1, Dim2D(3, 3))
        poses2 = [Dim2D(1, 1), Dim2D(-2, 2), Dim2D(3, 3), Dim2D(5, 0)]
        chosen_pos2, maximum_value2 = Dim2D.get_maximum_index_and_value(
            poses2,
            local_distance_function,
            **extra_parameters
        )
        self.assertEqual(maximum_value2, math.sqrt(53))
        self.assertEqual(chosen_pos2, Dim2D(5, 0))

    def test_get_maximum_index_and_value_with_complex_criteria_function(self):
        def complex_function(value, **extra_parameters):
            point1 = extra_parameters["point1"]
            point2 = extra_parameters["point2"]
            if Dim2D.get_manathan_distance(value, point1) > 10:
                return 20
            if Dim2D.get_manathan_distance(value, point2) < 5:
                return 50
            return Dim2D.get_manathan_distance(value, point1) + \
                Dim2D.get_manathan_distance(value, point2)
        extra_parameters = {
            "point1": Dim2D(5, 5),
            "point2": Dim2D(0, 0)
        }
        poses1 = [Dim2D(2, 3), Dim2D(-1, -1), Dim2D(2, 2), Dim2D(3, 3)]
        chosen_pos1, maximum_value1 = Dim2D.get_maximum_index_and_value(
            poses1,
            complex_function,
            **extra_parameters
        )
        self.assertEqual(maximum_value1, 50)
        self.assertEqual(chosen_pos1, Dim2D(2, 2))
        poses2 = [Dim2D(3, 2), Dim2D(4, 2)]
        chosen_pos2, maximum_value2 = Dim2D.get_maximum_index_and_value(
            poses2,
            complex_function,
            **extra_parameters
        )
        self.assertEqual(maximum_value2, 10)
        self.assertEqual(chosen_pos2, Dim2D(3, 2))

class Dimensions3D(unittest.TestCase):
    def test_simple(self):
        pos = Dim3D(2, 3, 4)
        self.assertEqual(pos.x, 2)
        self.assertEqual(pos.y, 3)
        self.assertEqual(pos.z, 4)

    def test_equal(self):
        pos1 = Dim3D(3, 8, 9)
        pos2 = Dim3D(4, 8, 7)
        pos3 = Dim3D(3, 8, 9)
        self.assertNotEqual(pos1, pos2)
        self.assertEqual(pos1, pos3)

if __name__ == "__main__":
    unittest.main()
