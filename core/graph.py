from enum import Enum, auto
from dataclasses import dataclass
import random
from typing import Tuple

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

    @dataclass
    class BlockingData:
        values = tuple()
        positions = tuple()

    # TODO: Possible move shape_type to raw_data_handler?
    def __init__(self,
                 raw_data_handler: RawDataHandler,
                 shape_type: Shape2D.Type,
                 blocking_values: tuple = None,
                 unreachable_positions: Tuple[Dim2D] = None
                ):
        self.raw_data_handler = raw_data_handler
        self.shape_type = shape_type
        self._get_shape(shape_type)
        self.update_blocking_data(blocking_values)
        self._unreachable_positions = self.unreachable_positions = unreachable_positions

    def _get_shape(self, shape_type):
        get_shape_function = {
            Shape2D.Type.RECTANGLE: self._get_rectangle_graph
        }[shape_type]
        self.graph_shape = get_shape_function()

    def _get_rectangle_graph(self):
        width, height = len(self.raw_data_handler.raw_data[0]), len(self.raw_data_handler.raw_data)
        top_left_corner = Dim2D(0, 0)
        return Rectangle(top_left_corner, width, height)

    def update_blocking_data(self, blocking_values: tuple):
        def update_blocking_positions(blocking_values: tuple):
            positions = []
            if blocking_values is None:
                return positions
            for y, row in enumerate(self.raw_data_handler.raw_data):
                for x, value in enumerate(row):
                    if value in blocking_values:
                        positions.append(Dim2D(x, y))
            return tuple(positions)
        self._blocking_data = Graph.BlockingData()
        self._blocking_data.values = blocking_values
        self._blocking_data.positions = update_blocking_positions(blocking_values)

    @property
    def blocking_values(self):
        return self._blocking_data.values

    @property
    def blocking_positions(self):
        return self._blocking_data.positions

    @property
    def unreachable_positions(self):
        return self._unreachable_positions

    @unreachable_positions.setter
    def unreachable_positions(self, positions: Tuple[Dim2D]):
        self._unreachable_positions = tuple(set(positions)) \
                                      if positions is not None else tuple()

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

    def _is_unreachable(self, should_reach: bool, candidate_position: Dim2D):
        return not should_reach and candidate_position in self._unreachable_positions

    # TODO: Check if the graph is connected via boundaries
    def _is_outside_of_boundaries(self, candidate_position: Dim2D):
        return not self.graph_shape.is_inside_boundaries(candidate_position)

    def get_available_neighbours(
            self,
            position: Dim2D,
            neighbour_data: NeighbourData,
            should_reach=False,
            should_block=True
        ):
        get_neighbours_type_function = {
            Graph.NeighbourData.Type.CROSS: Graph.get_neighbours_cross,
            Graph.NeighbourData.Type.SQUARE: Graph.get_neighbours_square,
            Graph.NeighbourData.Type.DIAMOND: Graph.get_neighbours_diamond,
            Graph.NeighbourData.Type.CUSTOM: neighbour_data.custom_function
        }[neighbour_data.type_]
        neighbours_positions = get_neighbours_type_function(position, neighbour_data)

        new_candidates = list()
        for candidate_position in neighbours_positions:
            if self._is_outside_of_boundaries(candidate_position):
                continue
            if self._is_blocked(should_block, candidate_position):
                continue
            if self._is_unreachable(should_reach, candidate_position):
                continue
            new_candidates.append(candidate_position)
        if neighbour_data.random_output:
            random.shuffle(new_candidates)
        return new_candidates

    def __str__(self):
        return f"Shape Type: {self.shape_type}\nRaw data:\n{self.raw_data_handler}"

    def __repr__(self): # pragma: no cover
        return self.__str__()
