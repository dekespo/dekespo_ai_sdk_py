from dimensions import Dim2D
from utils import *
from motionPhysics import MotionPhysics2D
from abc import ABC, abstractmethod

class Shape2D(ABC):
    def addPosition(self, position):
        checkType(position, Dim2D)
        return position

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    def addMotionPhysics(self, motionPhysics):
        checkType(motionPhysics, MotionPhysics2D)
        self.motionPhysics = motionPhysics

    @staticmethod
    def circleVscircleIntersectionCheck(circle1, circle2):
        dist = Dim2D.getEuclidDistance(circle1.centre, circle2.centre)
        totalRadius = circle1.radius + circle2.radius
        return dist <= totalRadius

class Rectangle(Shape2D):
    def __init__(self, upperLeftCorner, width, height):
        self.upperLeftCorner = super().addPosition(upperLeftCorner)
        checkPositiveValue(width)
        checkPositiveValue(height)
        self.width = width
        self.height = height        

    def __str__(self):
        return "upperLeftCorner = " + str(self.upperLeftCorner)
        + "width x height: " + str(self.width) + " x " + str(self.height)

    def __repr__(self):
        return self.__str__()

class Hexagon(Shape2D):
    def __init__(self):
        pass
    
    def __str__(self):
        return "pass"

    def __repr__(self):
        return self.__str__()

class Circle(Shape2D):
    def __init__(self, centre, radius):
        self.centre = super().addPosition(centre)
        checkPositiveValue(radius)
        self.radius = radius
    
    def __str__(self):
        return "centre: " + str(self.centre) + ", radius: " + str(self.radius)

    def __repr__(self):
        return self.__str__()

class Point(Shape2D):
    def __init__(self, position):
        self.position = super().addPosition(position)

    def __str__(self):
        return "position: " + str(self.position)

    def __repr__(self):
        return self.__str__()
