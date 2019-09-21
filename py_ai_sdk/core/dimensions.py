import math
from py_ai_sdk.core.core_utils import checkNumberValue, checkType

class Dim2D:
    def __init__(self, x, y):
        checkNumberValue(x)
        checkNumberValue(y)
        self.x = x
        self.y = y

    def __str__(self):
        return "x: " + str(self.x) + ", y: " + str(self.y)

    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        checkType(other, Dim2D)
        return self.x == other.x and self.y == other.y
    
    def __add__(self, other):
        checkType(other, Dim2D)
        return Dim2D(self.x + other.x, self.y + other.y)
    
    def vectoralMultiply(self, other):
        checkType(other, Dim2D)
        return Dim2D(self.x * other.x, self.y * other.y)
    
    def constantMultiply(self, other):
        checkNumberValue(other)
        return Dim2D(self.x * other, self.y * other)

    def vectoralDivide(self, other):
        checkType(other, Dim2D)
        return Dim2D(self.x / other.x, self.y / other.y)
    
    def constantDivide(self, other):
        checkNumberValue(other)
        return Dim2D(self.x / other, self.y / other)
    
    def round(self):
        self.x = round(self.x)
        self.y = round(self.y)
    
    @staticmethod
    def listToDim2Ds(liste):
        checkType(liste, list)
        if not liste:
            return []
        checkType(liste[0], tuple)
        return [Dim2D(lx, ly) for lx, ly in liste]

    @staticmethod
    def toNumberValue(object):
        checkType(object, Dim2D)
        if object.x == object.y:
            return object.x
        if object.x == 0 and object.y != 0:
            return object.y
        if object.x != 0 and object.y == 0:
            return object.x
        raise AssertionError("It cannot be converted to a value as x: ", object.x, " and y: ", object.y, \
             " are not the same and nonzero")

    @staticmethod
    def getAverageOfDim2Ds(liste):
        checkType(liste, list)
        totalDim2D = Dim2D(0, 0)
        if not liste:
            return totalDim2D
        for object in liste:
            checkType(object, Dim2D)
            totalDim2D += object
        return totalDim2D.constantDivide(len(liste))
    
    @staticmethod
    def getEuclidDistance(point1, point2):
        checkType(point1, Dim2D)
        checkType(point2, Dim2D)
        return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)

    @staticmethod
    def getManathanDistance(point1, point2):
        checkType(point1, Dim2D)
        checkType(point2, Dim2D)
        return abs(point1.x - point2.x) + abs(point1.y - point2.y)

class Dim3D:
    def __init__(self, x, y, z):
        checkNumberValue(x)
        checkNumberValue(y)
        checkNumberValue(z)
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "x: " + str(self.x) + ", y: " + str(self.y) + ", z: " + str(self.z)

    def __repr__(self):
        return self.__str__()
