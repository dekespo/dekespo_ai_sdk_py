from dataclasses import dataclass

from draw.colour import Colour
from core.dimensions import Dim2D

@dataclass
class ButtonData:
    text: str
    callback_function: 'typing.Any'
    grid_index: Dim2D = Dim2D(0, 0)
    grid_span_size: Dim2D = Dim2D(1, 1)
    colour: Colour = Colour.BLACK
    sticky: str = "nsew"

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
