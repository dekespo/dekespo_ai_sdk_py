from enum import Enum, auto
from dataclasses import dataclass

from py_ai_sdk.core.dimensions import Dim2D
from py_ai_sdk.core.shapes import Shape2D, Rectangle

class Graph:

    @dataclass
    class NeighbourData:
        class Type(Enum):
            NONE = auto()
            CROSS = auto()
            DIAMOND = auto()
            SQUARE = auto()
            CUSTOM = auto()

        type_: Type = Type.NONE
        length: int = 1
        custom_function: 'typing.Any' = None

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
    def get_neighbours_cross(position, neighbour_data: NeighbourData = NeighbourData()):
        x, y = position.x, position.y
        candidates = []
        for distance in range(1, neighbour_data.length + 1):
            candidates.append((x + distance, y))
            candidates.append((x - distance, y))
            candidates.append((x, y + distance))
            candidates.append((x, y - distance))
        candidates = Dim2D.convert_candiates_to_dimensions(candidates)
        return candidates

    # TODO: Remove the duplication for direction check with diamond
    @staticmethod
    def get_neighbours_square(position, neighbour_data: NeighbourData = NeighbourData()):
        x, y = position.x, position.y
        candidates = []
        for y_distance in range(-neighbour_data.length, neighbour_data.length + 1):
            for x_distance in range(-neighbour_data.length, neighbour_data.length + 1):
                candidates.append((x + x_distance, y + y_distance))
        candidates.remove((x, y))
        candidates = Dim2D.convert_candiates_to_dimensions(candidates)
        return candidates

    @staticmethod
    def get_neighbours_diamond(position, neighbour_data: NeighbourData = NeighbourData()):
        x, y = position.x, position.y
        candidates = []
        for y_distance in range(-neighbour_data.length, neighbour_data.length + 1):
            for x_distance in range(-neighbour_data.length, neighbour_data.length + 1):
                if abs(x_distance) + abs(y_distance) <= neighbour_data.length:
                    candidates.append((x + x_distance, y + y_distance))
        candidates.remove((x, y))
        candidates = Dim2D.convert_candiates_to_dimensions(candidates)
        return candidates

    def get_available_neighbours(self, position, neighbour_data: NeighbourData, unreachable_positions=None, should_block=True):
        get_neighbours_type_function = {
            Graph.NeighbourData.Type.CROSS: Graph.get_neighbours_cross,
            Graph.NeighbourData.Type.SQUARE: Graph.get_neighbours_square,
            Graph.NeighbourData.Type.DIAMOND: Graph.get_neighbours_diamond,
            Graph.NeighbourData.Type.CUSTOM: neighbour_data.custom_function
        }[neighbour_data.type_]
        neighbours_positions = get_neighbours_type_function(position, neighbour_data)
        if not unreachable_positions:
            unreachable_positions = []

        for candidate_position in reversed(neighbours_positions):
            is_inside_boundaries = self.graph_shape.check_boundaries(candidate_position)
            if not is_inside_boundaries:
                neighbours_positions.remove(candidate_position)
            elif should_block and candidate_position in self.blocking_positions:
                neighbours_positions.remove(candidate_position)
            elif candidate_position in unreachable_positions:
                neighbours_positions.remove(candidate_position)
        return neighbours_positions
