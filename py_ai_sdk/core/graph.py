from enum import Enum, auto
from dataclasses import dataclass

from py_ai_sdk.core.dimensions import Dim2D
from py_ai_sdk.core.shapes import Shape2D, Rectangle

class Graph:

    @dataclass
    class NeighbourData:
        class Type(Enum):
            CROSS = auto()
            DIAMOND = auto()
            SQUARE = auto()
            DIAGONAL = auto()

        type_: Type
        length: int = 1

    def __init__(self, raw_data, shape_type, blocking_values=None):
        self.raw_data = raw_data
        self.shape_type = shape_type
        self._get_shape(shape_type)
        self.update_blocking_values(blocking_values)

    def _get_shape(self, shape_type):
        get_shape_function = {
            Shape2D.Type.RECTANGLE: self._get_rectangle_graph
        }[shape_type]
        self.graph_shape = get_shape_function()

    def _get_rectangle_graph(self):
        width, height = len(self.raw_data[0]), len(self.raw_data)
        top_left_corner = Dim2D(0, 0)
        return Rectangle(top_left_corner, width, height)

    def _update_blocking_positions(self):
        positions = []
        if not self.blocking_values:
            return positions
        for y, row in enumerate(self.raw_data):
            for x, value in enumerate(row):
                if value in self.blocking_values:
                    positions.append(Dim2D(x, y))
        return positions

    def update_blocking_values(self, blocking_values):
        self.blocking_values = blocking_values
        self.blocking_positions = self._update_blocking_positions()

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

    @staticmethod
    def get_neighbours_diamond(position, length=1):
        x, y = position.x, position.y
        candidates = []
        for y_distance in range(-length, length + 1):
            for x_distance in range(-length, length + 1):
                if abs(x_distance) + abs(y_distance) <= length:
                    candidates.append((x + x_distance, y + y_distance))
        candidates.remove((x, y))
        candidates = Dim2D.convert_candiates_to_dimensions(candidates)
        return candidates

    def get_available_neighbours(self, position, neighbour_data, unreachable_positions=None):
        get_neighbours_type_function = {
            Graph.NeighbourData.Type.CROSS: Graph.get_neighbours_cross,
            Graph.NeighbourData.Type.SQUARE: Graph.get_neighbours_square,
            Graph.NeighbourData.Type.DIAMOND: Graph.get_neighbours_diamond
        }[neighbour_data.type_]
        neighbours_positions = get_neighbours_type_function(position, neighbour_data.length)
        if not unreachable_positions:
            unreachable_positions = []

        for candidate_position in reversed(neighbours_positions):
            is_inside_boundaries = self.graph_shape.check_boundaries(candidate_position)
            if not is_inside_boundaries:
                neighbours_positions.remove(candidate_position)
            elif candidate_position in self.blocking_positions:
                neighbours_positions.remove(candidate_position)
            elif candidate_position in unreachable_positions:
                neighbours_positions.remove(candidate_position)
        return neighbours_positions
