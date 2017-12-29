from utils import *

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
        elif object.x == 0 and object.y != 0:
            return object.y
        elif object.x != 0 and object.y == 0:
            return object.x
        else:
            raise AssertionError("It cannot be converted to a value as x: ", object.x, " and y: ", object.y, " are not the same and nonzero")

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
