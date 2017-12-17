from utils import *

class Dim2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x: " + str(self.x) + ", y: " + str(self.y)

    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        checkType(other, Dim2D)
        return self.x == other.x and self.y == other.y
    
    @staticmethod
    def listToDim2Ds(liste):
        checkType(liste, list)
        if not liste:
            return []
        checkType(liste[0], tuple)
        return [Dim2D(lx, ly) for lx, ly in liste]

class Dim3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "x: " + str(self.x) + ", y: " + str(self.y) + ", z: " + str(self.z)

    def __repr__(self):
        return self.__str__()
