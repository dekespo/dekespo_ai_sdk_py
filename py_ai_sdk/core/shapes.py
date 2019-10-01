from abc import ABC, abstractmethod

from py_ai_sdk.core.dimensions import Dim2D
from py_ai_sdk.core.core_utils import checkNoneValue, checkPositiveValue

class Shape2D(ABC):
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @staticmethod
    def addPosition(position):
        return position

    def addMotionPhysics(self, motionPhysics):
        self.motionPhysics = motionPhysics

    def updateMotionPhysics(self, position, newForce=Dim2D(0, 0), newMass=None, friction=None, newAcceleration=Dim2D(0, 0)):
        checkNoneValue(self.motionPhysics, "motionPhysics")
        return self.motionPhysics.update(position, newForce, newMass, friction, newAcceleration)

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
        return "upperLeftCorner = " + str(self.upperLeftCorner) \
        + "width x height: " + str(self.width) + " x " + str(self.height)

    def __repr__(self):
        return self.__str__()

    def updateMotionPhysics(self, newForce=Dim2D(0, 0), newMass=None, friction=None, newAcceleration=Dim2D(0, 0)):
        self.upperLeftCorner = super().updateMotionPhysics(self.upperLeftCorner, newForce, newMass, friction, newAcceleration)

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

    def updateMotionPhysics(self, newForce=Dim2D(0, 0), newMass=None, friction=None, newAcceleration=Dim2D(0, 0)):
        self.centre = super().updateMotionPhysics(self.centre, newForce, newMass, friction, newAcceleration)

class Point(Shape2D):
    def __init__(self, position):
        self.position = super().addPosition(position)

    def __str__(self):
        return "position: " + str(self.position)

    def __repr__(self):
        return self.__str__()

    def updateMotionPhysics(self, newForce=Dim2D(0, 0), newMass=None, friction=None, newAcceleration=Dim2D(0, 0)):
        self.position = super().updateMotionPhysics(self.position, newForce, newMass, friction, newAcceleration)
