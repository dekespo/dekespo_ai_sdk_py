from abc import ABC, abstractmethod

from py_ai_sdk.core.dimensions import Dim2D
from py_ai_sdk.core.core_utils import check_positive_value

class Shape2D(ABC):
    def __init__(self):
        self.motion_physics = None

    @abstractmethod
    def __str__(self):
        pass

    def __repr__(self):
        self.__str__()

    def set_motion_physics(self, motion_physics):
        self.motion_physics = motion_physics

    def update_motion_physics(self):
        return self.motion_physics.update()

    @staticmethod
    def circle_vs_circle_intersection_check(circle1, circle2):
        dist = Dim2D.get_euclid_distance(circle1.centre, circle2.centre)
        total_radius = circle1.radius + circle2.radius
        return dist <= total_radius

class Rectangle(Shape2D):
    def __init__(self, top_left_corner, width, height):
        super().__init__()
        self.top_left_corner = top_left_corner
        check_positive_value(width)
        check_positive_value(height)
        self.width = width
        self.height = height

    def __str__(self):
        return "top_left_corner = " + str(self.top_left_corner) \
        + "width x height: " + str(self.width) + " x " + str(self.height)

    def update_motion_physics(self):
        self.top_left_corner = super().update_motion_physics()

class Circle(Shape2D):
    def __init__(self, centre, radius):
        super().__init__()
        self.centre = centre
        check_positive_value(radius)
        self.radius = radius

    def __str__(self):
        return "centre: " + str(self.centre) + ", radius: " + str(self.radius)

    def update_motion_physics(self):
        self.centre = super().update_motion_physics()

class Point(Shape2D):
    def __init__(self, position):
        super().__init__()
        self.position = position

    def __str__(self):
        return "position: " + str(self.position)

    def update_motion_physics(self):
        self.position = super().update_motion_physics()
