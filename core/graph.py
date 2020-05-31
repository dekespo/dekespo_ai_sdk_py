from enum import Enum, auto
from dataclasses import dataclass
import random

from core.dimensions import Dim2D
from core.raw_data_handler import RawDataHandler
from core.shapes import Shape2D, Rectangle

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
        random_output: bool = False

    # TODO: Possible move shape_type to raw_data_handler?
    def __init__(self,
                 raw_data_handler: RawDataHandler,
                 shape_type: Shape2D.Type,
                 blocking_values=None
                ):
        self.raw_data_handler = raw_data_handler
        self.shape_type = shape_type
        self._get_shape(shape_type)
        self.update_blocking_values(blocking_values)

    def _get_shape(self, shape_type):
        get_shape_function = {
            Shape2D.Type.RECTANGLE: self._get_rectangle_graph
        }[shape_type]
        self.graph_shape = get_shape_function()

    def _get_rectangle_graph(self):
        width, height = len(self.raw_data_handler.raw_data[0]), len(self.raw_data_handler.raw_data)
        top_left_corner = Dim2D(0, 0)
        return Rectangle(top_left_corner, width, height)

    def _update_blocking_positions(self):
        positions = []
        if not self.blocking_values:
            return positions
        for y, row in enumerate(self.raw_data_handler.raw_data):
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
        for distance in range(1, neighbour_data.length + 1):
            yield Dim2D(x + distance, y)
            yield Dim2D(x - distance, y)
            yield Dim2D(x, y + distance)
            yield Dim2D(x, y - distance)

    @staticmethod
    def get_neighbours_square(position, neighbour_data: NeighbourData = NeighbourData()):
        x, y = position.x, position.y
        for y_distance in range(-neighbour_data.length, neighbour_data.length + 1):
            for x_distance in range(-neighbour_data.length, neighbour_data.length + 1):
                if not (x_distance == 0 and y_distance == 0):
                    yield Dim2D(x + x_distance, y + y_distance)

    @staticmethod
    def get_neighbours_diamond(position, neighbour_data: NeighbourData = NeighbourData()):
        x, y = position.x, position.y
        for y_distance in range(-neighbour_data.length, neighbour_data.length + 1):
            for x_distance in range(-neighbour_data.length, neighbour_data.length + 1):
                if not (x_distance == 0 and y_distance == 0) and \
                   abs(x_distance) + abs(y_distance) <= neighbour_data.length:
                    yield Dim2D(x + x_distance, y + y_distance)

    def _is_blocked(self, should_block: bool, candidate_position: Dim2D):
        return should_block and candidate_position in self.blocking_positions

    def get_available_neighbours(
            self,
            position,
            neighbour_data: NeighbourData,
            unreachable_positions=None,
            should_block=True
        ):
        if not unreachable_positions:
            unreachable_positions = []
        get_neighbours_type_function = {
            Graph.NeighbourData.Type.CROSS: Graph.get_neighbours_cross,
            Graph.NeighbourData.Type.SQUARE: Graph.get_neighbours_square,
            Graph.NeighbourData.Type.DIAMOND: Graph.get_neighbours_diamond,
            Graph.NeighbourData.Type.CUSTOM: neighbour_data.custom_function
        }[neighbour_data.type_]
        neighbours_positions = get_neighbours_type_function(position, neighbour_data)

        new_candidates = list()
        for candidate_position in neighbours_positions:
            if not self.graph_shape.is_inside_boundaries(candidate_position):
                continue
            if self._is_blocked(should_block, candidate_position):
                continue
            if candidate_position in unreachable_positions:
                continue
            new_candidates.append(candidate_position)
        if neighbour_data.random_output:
            random.shuffle(new_candidates)
        return new_candidates

    def __str__(self):
        return f"Shape Type: {self.shape_type}\nRaw data:\n{self.raw_data_handler}"

    def __repr__(self): # pragma: no cover
        return self.__str__()
