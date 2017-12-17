from dimensions import Dim2D
from shapes import *
from utils import *

def boundaryChecks2D_rectangle(map, position):
    checkType(map, Rectangle)
    if position.x < map.upLeftCorner.x \
    or position.x >= map.upLeftCorner.x + map.width \
    or position.y < map.upLeftCorner.y \
    or position.y >= map.upLeftCorner.y + map.height:
        return False
    return True

def boundaryChecks2D_hexagon(map, position):
    pass

def boundaryChecks2D_circle(map, position):
    pass
