from dataclasses import dataclass

from draw.colour import Colour
from core.dimensions import Dim2D

@dataclass
class ButtonData:
    text: str
    callback_function: 'typing.Any'
    colour: Colour = Colour.BLACK
    # Grid
    grid_index: Dim2D = Dim2D(0, 0)
    grid_span_size: Dim2D = Dim2D(1, 1)
    sticky: str = "nsew"
    # Pack
    side: str = "left"
    fill: str = "both"
    expand: bool = True


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
