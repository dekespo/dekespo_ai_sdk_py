import math

class Dim2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x: " + str(self.x) + ", y: " + str(self.y)

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
    def toNumberValue(dim2D):
        if dim2D.x == dim2D.y:
            return dim2D.x
        if dim2D.x == 0 and dim2D.y != 0:
            return dim2D.y
        if dim2D.x != 0 and dim2D.y == 0:
            return dim2D.x
        raise AssertionError("It cannot be converted to a value as " \
            " x: ", dim2D.x, " and y: ", dim2D.y, " are not the same and nonzero")

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

class Dim3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "x: " + str(self.x) + ", y: " + str(self.y) + ", z: " + str(self.z)

    def __repr__(self):
        return self.__str__()
