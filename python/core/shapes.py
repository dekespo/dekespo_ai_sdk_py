from dimensions import Dim2D
from utils import *

class Shape:
    @staticmethod
    def circleVscircleIntersectionCheck(circle1, circle2):
        dist = Dim2D.getEuclidDistance(circle1.centre, circle2.centre)
        totalRadius = circle1.radius + circle2.radius
        return dist <= totalRadius

class Rectangle(Shape):
    def __init__(self, upLeftCorner, width, height):
        checkType(upLeftCorner, Dim2D)
        checkPositiveValue(width)
        checkPositiveValue(height)
        self.upLeftCorner = upLeftCorner
        self.width = width
        self.height = height        

    def __str__(self):
        return "upLeftCorner = " + str(self.upLeftCorner) 
        + "width x height: " + str(self.width) + " x " + str(self.height)

    def __repr__(self):
        return self.__str__()

class Hexagon(Shape):
    def __init__(self):
        pass
    
    def __str__(self):
        return "pass"

    def __repr__(self):
        return self.__str__()

class Circle(Shape):
    def __init__(self, centre, radius):
        checkPositiveValue(radius)
        checkType(centre, Dim2D)
        self.centre = centre
        self.radius = radius
    
    def __str__(self):
        return "centre: " + str(self.centre) + ", radius: " + str(self.radius) 

    def __repr__(self):
        return self.__str__()

class Point(Rectangle):
    def __init__(self, upLeftCorner):
        super().__init__(upLeftCorner, 1 ,1)

    def __str__(self):
        return super.__str__()

    def __repr__(self):
        return self.__str__()
