from abc import ABC, abstractmethod
from enum import Enum

from py_ai_sdk.core.dimensions import Dim2D
from py_ai_sdk.core.core_utils import check_positive_value

class Shape2D(ABC):

    class Type(Enum):
        RECTANGLE = 1
        CIRCLE = 2
        POINT = 3

    # TODO: Motion physics should have Shape2D instead of here
    def __init__(self):
        self.motion_physics = None

    @abstractmethod
    def __str__(self):
        pass

    def __repr__(self):
        self.__str__()

    @abstractmethod
    def check_boundaries(self, position):
        pass

    def set_motion_physics(self, motion_physics):
        self.motion_physics = motion_physics

    def update_motion_physics(self):
        return self.motion_physics.update()

class Rectangle(Shape2D):
    def __init__(self, top_left_corner, width, height):
        super().__init__()
        self.top_left_corner = top_left_corner
        check_positive_value(width)
        check_positive_value(height)
        self.width = width
        self.height = height

    def __str__(self):
        return f"top_left_corner = {self.top_left_corner}, \
                width x height: {self.width}x{self.height}"

    def update_motion_physics(self):
        self.top_left_corner = super().update_motion_physics()

    def check_boundaries(self, position):
        if position.x < self.top_left_corner.x \
        or position.x >= self.top_left_corner.x + self.width \
        or position.y < self.top_left_corner.y \
        or position.y >= self.top_left_corner.y + self.height:
            return False
        return True

class Circle(Shape2D):
    def __init__(self, centre, radius):
        super().__init__()
        self.centre = centre
        check_positive_value(radius)
        self.radius = radius

    def __str__(self):
        return f"centre: {self.centre}, radius: {self.radius}"

    def update_motion_physics(self):
        self.centre = super().update_motion_physics()

    def check_boundaries(self, position):
        pass

    @staticmethod
    def circle_vs_circle_intersection_check(circle1, circle2):
        dist = Dim2D.get_euclid_distance(circle1.centre, circle2.centre)
        total_radius = circle1.radius + circle2.radius
        return dist <= total_radius

class Point(Shape2D):
    def __init__(self, position):
        super().__init__()
        self.position = position

    def __str__(self):
        return f"position: {self.position}"

    def update_motion_physics(self):
        self.position = super().update_motion_physics()

    def check_boundaries(self, position):
        pass
