from enum import Enum, auto

from draw.tkinter_singleton import TkinterSingleton
from draw.colour import Colour

from core.dimensions import Dim2D

class Status(Enum):
    ON_PAUSE = auto()
    SHOULD_RESTART = auto()
    SHOULD_GO_BACK = auto()
    SHOULD_GO_NEXT = auto()
    SHOULD_PLAY_FORWARD = auto()

class Button:

    # TODO: Have reset button
    @staticmethod
    def back(status_dictionary):
        status_dictionary[Status.SHOULD_GO_BACK] = True

    @staticmethod
    def next(status_dictionary):
        status_dictionary[Status.SHOULD_GO_NEXT] = True

    @staticmethod
    def play_forward(status_dictionary):
        status_dictionary[Status.ON_PAUSE] = False
        status_dictionary[Status.SHOULD_PLAY_FORWARD] = True

    @staticmethod
    def play_backward(status_dictionary):
        status_dictionary[Status.ON_PAUSE] = False
        status_dictionary[Status.SHOULD_PLAY_FORWARD] = False

    @staticmethod
    def stop(status_dictionary):
        status_dictionary[Status.ON_PAUSE] = True

    @staticmethod
    def restart(status_dictionary):
        status_dictionary[Status.SHOULD_RESTART] = True

def create_rectangle_canvas(tile_size: Dim2D, grid_size: Dim2D):
    raw_data = []
    for y in range(grid_size.y):
        row_raw_data = []
        for x in range(grid_size.x):
            TkinterSingleton.create_rectangle_at(Dim2D(x, y), tile_size, Colour.BLACK)
            row_raw_data.append(0)
        raw_data.append(row_raw_data)
    return raw_data
