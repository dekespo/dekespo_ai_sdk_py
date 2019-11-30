from dataclasses import dataclass

from py_ai_sdk.core.shapes import Rectangle

from draw_sdk.colour import Colour

@dataclass
class Tile:
    rectangle: Rectangle
    colour: Colour
