from dimensions import Dim2D
from utils import *

class Rectangle:
    def __init__(self, width, height):
        checkPositiveValue(width)
        checkPositiveValue(height)
        self.width = width
        self.height = height        

    def __str__(self):
        return "width x height: " + str(self.width) + " x " + str(self.height)

    def __repr__(self):
        return self.__str__()

class Hexagon:
    def __init__(self):
        pass
    
    def __str__(self):
        return "pass"

    def __repr__(self):
        return self.__str__()

class Circle:
    def __init__(self, centre, radius):
        checkPositiveValue(radius)
        checkType(centre, Dim2D)
        self.centre = centre
        self.radius = radius
    
    def __str__(self):
        return "centre: " + str(self.centre) + ", radius: " + str(self.radius) 

    def __repr__(self):
        return self.__str__()
