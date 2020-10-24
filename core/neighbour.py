from enum import Enum, auto
from dataclasses import dataclass
from typing import Any

from core.dimensions import Dim2D

class Neighbour:

    @dataclass
    class Data:
        class Type(Enum):
            NONE = auto()
            CROSS = auto()
            DIAMOND = auto()
            SQUARE = auto()
            BFS = auto()
            CUSTOM = auto()

        type_: Type = Type.NONE
        radius: int = 1
        custom_function: Any = None
        random_output: bool = False
        should_reach: bool = False
        should_block: bool = True

    @staticmethod
    def get_neighbours_square(
            position: Dim2D,
            is_position_valid_function,
            neighbour_data: Data = Data()
        ):
        x, y = position.x, position.y
        for y_distance in range(-neighbour_data.radius, neighbour_data.radius + 1):
            for x_distance in range(-neighbour_data.radius, neighbour_data.radius + 1):
                new_position = Dim2D(x + x_distance, y + y_distance)
                if not(x_distance == 0 and y_distance == 0) \
                   and is_position_valid_function(
                           new_position,
                           neighbour_data.should_block,
                           neighbour_data.should_reach):
                    yield new_position, abs(x_distance) + abs(y_distance)

    @staticmethod
    def get_neighbours_diamond(
            position: Dim2D,
            is_position_valid_function,
            neighbour_data: Data = Data()
        ):
        x, y = position.x, position.y
        for y_distance in range(-neighbour_data.radius, neighbour_data.radius + 1):
            for x_distance in range(-neighbour_data.radius, neighbour_data.radius + 1):
                new_position = Dim2D(x + x_distance, y + y_distance)
                if not (x_distance == 0 and y_distance == 0) \
                   and abs(x_distance) + abs(y_distance) <= neighbour_data.radius \
                   and is_position_valid_function(
                           new_position,
                           neighbour_data.should_block,
                           neighbour_data.should_reach):
                    yield new_position, abs(x_distance) + abs(y_distance)

    @staticmethod
    def get_neighbours_cross(
            position: Dim2D,
            is_position_valid_function,
            neighbour_data: Data = Data()
        ):
        x, y = position.x, position.y
        for distance in range(1, neighbour_data.radius + 1):
            for new_position in (
                    Dim2D(x + distance, y),
                    Dim2D(x - distance, y),
                    Dim2D(x, y + distance),
                    Dim2D(x, y - distance)):
                if is_position_valid_function(
                        new_position,
                        neighbour_data.should_block,
                        neighbour_data.should_reach):
                    yield new_position, distance

    @staticmethod
    def get_neighbour_function_8_connectivity(
            position: Dim2D,
            is_position_valid_function,
            neighbour_data: Data = Data()
        ):
        x, y = position.x, position.y
        for new_position in (
                Dim2D(x - 1, y),
                Dim2D(x - 1, y - 1),
                Dim2D(x, y - 1),
                Dim2D(x + 1, y - 1)):
            if is_position_valid_function(
                    new_position,
                    neighbour_data.should_block,
                    neighbour_data.should_reach):
                yield new_position, -1

    @staticmethod
    def get_neighbour_function_4_connectivity(
            position: Dim2D,
            is_position_valid_function,
            neighbour_data: Data = Data()
        ):
        x, y = position.x, position.y
        for new_position in (
                Dim2D(x - 1, y),
                Dim2D(x, y - 1)):
            if is_position_valid_function(
                    new_position,
                    neighbour_data.should_block,
                    neighbour_data.should_reach):
                yield new_position, -1
