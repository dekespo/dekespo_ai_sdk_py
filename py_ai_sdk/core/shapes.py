from abc import ABC, abstractmethod
from enum import Enum

from py_ai_sdk.core.dimensions import Dim2D
from py_ai_sdk.core.core_utils import check_positive_value

class Shape2D(ABC):

    class NeighbourType(Enum):
        CROSS = 1
        DIAMOND = 2
        SQUARE = 3
        DIAGONAL = 4

    def __init__(self, data):
        self.motion_physics = None
        self.data = data

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
    def __init__(self, top_left_corner, width, height, data=None):
        super().__init__(data)
        self.top_left_corner = top_left_corner
        check_positive_value(width)
        check_positive_value(height)
        self.width = width
        self.height = height

    def __str__(self):
        return f"top_left_corner = {self.top_left_corner}, width x height: {self.width}x{self.height}"

    def update_motion_physics(self):
        self.top_left_corner = super().update_motion_physics()

    def check_boundaries(self, position):
        if position.x < self.top_left_corner.x \
        or position.x >= self.top_left_corner.x + self.width \
        or position.y < self.top_left_corner.y \
        or position.y >= self.top_left_corner.y + self.height:
            return False
        return True

    @staticmethod
    def get_neighbours_cross(position, length=1):
        x, y = position.x, position.y
        candidates = []
        for distance in range(1, length+1):
            candidates.append((x + distance, y))
            candidates.append((x - distance, y))
            candidates.append((x, y + distance))
            candidates.append((x, y - distance))
        candidates = Dim2D.convert_candiates_to_dimensions(candidates)
        return candidates

    @staticmethod
    def get_neighbours_square(position, length=1):
        x, y = position.x, position.y
        candidates = []
        top_left_corner_x, top_left_corner_y = (x - length, y - length)
        edge_size = 2 * length + 1
        for y_distance in range(edge_size):
            for x_distance in range(edge_size):
                candidates.append((top_left_corner_x + x_distance, top_left_corner_y + y_distance))
        candidates.remove((x, y))
        candidates = Dim2D.convert_candiates_to_dimensions(candidates)
        return candidates

    def get_available_neighbours(self, blocking_positions, neighbour_type, position, length=1):
        if neighbour_type == Rectangle.NeighbourType.CROSS:
            neighbours_positions = Rectangle.get_neighbours_cross(position, length)
        elif neighbour_type == Rectangle.NeighbourType.SQUARE:
            neighbours_positions = Rectangle.get_neighbours_square(position, length)

        for candidate_position in reversed(neighbours_positions):
            is_inside_boundaries = self.check_boundaries(candidate_position)
            if not is_inside_boundaries:
                neighbours_positions.remove(candidate_position)
            elif candidate_position in blocking_positions:
                neighbours_positions.remove(candidate_position)
        return neighbours_positions

class Circle(Shape2D):
    def __init__(self, centre, radius, data=None):
        super().__init__(data)
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
    def __init__(self, position, data=None):
        super().__init__(data)
        self.position = position

    def __str__(self):
        return f"position: {self.position}"

    def update_motion_physics(self):
        self.position = super().update_motion_physics()

    def check_boundaries(self, position):
        pass
