import math

class Dim2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"(x: {self.x}, y: {self.y})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Dim2D(self.x + other.x, self.y + other.y)

    def vectoral_multiply(self, other):
        return Dim2D(self.x * other.x, self.y * other.y)

    def constant_multiply(self, other):
        return Dim2D(self.x * other, self.y * other)

    def vectoral_divide(self, other):
        return Dim2D(self.x / other.x, self.y / other.y)

    def constant_divide(self, other):
        return Dim2D(self.x / other, self.y / other)

    def round(self):
        self.x = round(self.x)
        self.y = round(self.y)

    @staticmethod
    def convert_candiates_to_dimensions(candidates):
        if not candidates:
            return []
        return [Dim2D(x, y) for x, y in candidates]

    @staticmethod
    def get_average_value(dimensions):
        total_dimensions_values = Dim2D(0, 0)
        if not dimensions:
            return total_dimensions_values
        for dimension in dimensions:
            total_dimensions_values += dimension
        return total_dimensions_values.constant_divide(len(dimensions))

    @staticmethod
    def get_euclid_distance(point1, point2):
        return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)

    @staticmethod
    def get_manathan_distance(point1, point2):
        return abs(point1.x - point2.x) + abs(point1.y - point2.y)

    @staticmethod
    def get_minimum_index_and_value(dimensions, criteria_function, **kwargs):
        def minimum_operator(value, minimum):
            return value < minimum
        return Dim2D.get_optimum_index_and_value(
            dimensions,
            criteria_function,
            minimum_operator,
            **kwargs
        )

    @staticmethod
    def get_maximum_index_and_value(dimensions, criteria_function, **kwargs):
        def maximum_operator(value, maximum):
            return value > maximum
        return Dim2D.get_optimum_index_and_value(
            dimensions,
            criteria_function,
            maximum_operator,
            **kwargs
        )

    @staticmethod
    def get_optimum_index_and_value(dimensions, criteria_function, operator_function, **kwargs):
        start_index = 0
        optimum_dimension = dimensions[start_index]
        optimum_value = criteria_function(dimensions[start_index], **kwargs)
        for dimension in dimensions:
            new_value = criteria_function(dimension, **kwargs)
            if operator_function(new_value, optimum_value):
                optimum_dimension = dimension
                optimum_value = new_value
        return optimum_dimension, optimum_value

    def __hash__(self):
        return hash((self.x, self.y))

    def __iter__(self):
        return iter((self.x, self.y))


class Dim3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "x: " + str(self.x) + ", y: " + str(self.y) + ", z: " + str(self.z)

    def __repr__(self):
        return self.__str__()
