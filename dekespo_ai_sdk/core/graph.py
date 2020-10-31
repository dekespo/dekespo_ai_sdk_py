from dataclasses import dataclass
from random import shuffle
from typing import List, Tuple, Union
from collections import OrderedDict

from dekespo_ai_sdk.core.dimensions import Dim2D
from dekespo_ai_sdk.core.raw_data_handler import RawDataHandler
from dekespo_ai_sdk.core.shapes import Shape2D, Rectangle
from dekespo_ai_sdk.core.neighbour import Neighbour


class Graph:
    @dataclass
    class BlockingData:
        values: Union[Tuple, None] = ()
        positions: Union[Tuple, None] = ()

    # TODO: Possible move shape_type to raw_data_handler?
    def __init__(
        self,
        raw_data_handler: RawDataHandler,
        shape_type: Shape2D.Type,
        blocking_values: Tuple = (),
        unreachable_positions: Tuple = (),
    ):
        self.raw_data_handler = raw_data_handler
        self.shape_type = shape_type
        self._get_shape(shape_type)
        self.update_blocking_data(blocking_values)
        self._unreachable_positions = self.unreachable_positions = unreachable_positions

    def _get_shape(self, shape_type):
        get_shape_function = {Shape2D.Type.RECTANGLE: self._get_rectangle_graph}[
            shape_type
        ]
        self.graph_shape = get_shape_function()

    def _get_rectangle_graph(self):
        width, height = len(self.raw_data_handler.raw_data[0]), len(
            self.raw_data_handler.raw_data
        )
        top_left_corner = Dim2D(0, 0)
        return Rectangle(top_left_corner, width, height)

    def update_blocking_data(self, blocking_values: Tuple):
        def update_blocking_positions(blocking_values: Tuple):
            positions: List[Dim2D] = []
            if not blocking_values:
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
        self._unreachable_positions = (
            tuple(set(positions)) if positions is not None else tuple()
        )

    def _is_position_valid(
        self, candidate_position: Dim2D, should_block: bool, should_reach: bool
    ):
        def is_blocked(should_block: bool, candidate_position: Dim2D):
            return should_block and candidate_position in self.blocking_positions

        def is_unreachable(should_reach: bool, candidate_position: Dim2D):
            return (
                not should_reach and candidate_position in self._unreachable_positions
            )

        # TODO: Check if the graph is connected via boundaries
        def is_outside_of_boundaries(candidate_position: Dim2D):
            return not self.graph_shape.is_inside_boundaries(candidate_position)

        return not (
            is_outside_of_boundaries(candidate_position)
            or is_blocked(should_block, candidate_position)
            or is_unreachable(should_reach, candidate_position)
        )

    def get_available_neighbours(
        self, position: Dim2D, neighbour_data: Neighbour.Data
    ) -> "OrderedDict[Dim2D, int]":
        get_neighbours_type_function = {
            Neighbour.Data.Type.CROSS: Neighbour.get_neighbours_cross,
            Neighbour.Data.Type.SQUARE: Neighbour.get_neighbours_square,
            Neighbour.Data.Type.DIAMOND: Neighbour.get_neighbours_diamond,
            Neighbour.Data.Type.CUSTOM: neighbour_data.custom_function,
        }[neighbour_data.type_]
        neighbours_positions_ordered_dic = OrderedDict(
            get_neighbours_type_function(
                position, self._is_position_valid, neighbour_data
            )
        )

        if neighbour_data.random_output:
            items = list(neighbours_positions_ordered_dic.items())
            shuffle(items)
            neighbours_positions_ordered_dic = OrderedDict(items)
        return neighbours_positions_ordered_dic

    def __str__(self):
        return f"Shape Type: {self.shape_type}\nRaw data:\n{self.raw_data_handler}"

    def __repr__(self):  # pragma: no cover
        return self.__str__()
