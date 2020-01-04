from dataclasses import dataclass

from draw.colour import Colour
from core.dimensions import Dim2D

@dataclass
class GridData:
    index: Dim2D = Dim2D(0, 0)
    span_size: Dim2D = Dim2D(1, 1)
    sticky: str = "nsew"

@dataclass
class PackData:
    side: str = "left"
    fill: str = "both"
    expand: bool = True

@dataclass
class ButtonData:
    text: str
    callback_function: 'typing.Any'
    colour: Colour = Colour.BLACK
    grid_data: GridData = None
    pack_data: PackData = None

class Button:

    @staticmethod
    def back():
        print("Pressed back")

    @staticmethod
    def play():
        print("Pressed play")

    @staticmethod
    def stop():
        print("Pressed stop")

    @staticmethod
    def restart():
        print("Pressed restart")
