from enum import Enum, auto
from dataclasses import dataclass

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
        custom_function: 'typing.Any' = None
        random_output: bool = False

    @staticmethod
    def get_neighbours_square(position: Dim2D, neighbour_data: Data = Data()):
        x, y = position.x, position.y
        for y_distance in range(-neighbour_data.radius, neighbour_data.radius + 1):
            for x_distance in range(-neighbour_data.radius, neighbour_data.radius + 1):
                if not (x_distance == 0 and y_distance == 0):
                    yield Dim2D(x + x_distance, y + y_distance)

    @staticmethod
    def get_neighbours_diamond(position: Dim2D, neighbour_data: Data = Data()):
        x, y = position.x, position.y
        for y_distance in range(-neighbour_data.radius, neighbour_data.radius + 1):
            for x_distance in range(-neighbour_data.radius, neighbour_data.radius + 1):
                if not (x_distance == 0 and y_distance == 0) and \
                   abs(x_distance) + abs(y_distance) <= neighbour_data.radius:
                    yield Dim2D(x + x_distance, y + y_distance)

    @staticmethod
    def get_neighbours_cross(position: Dim2D, neighbour_data: Data = Data()):
        x, y = position.x, position.y
        for distance in range(1, neighbour_data.radius + 1):
            yield Dim2D(x + distance, y)
            yield Dim2D(x - distance, y)
            yield Dim2D(x, y + distance)
            yield Dim2D(x, y - distance)
