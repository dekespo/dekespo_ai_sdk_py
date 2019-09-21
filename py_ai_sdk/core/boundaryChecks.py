from py_ai_sdk.core.dimensions import Dim2D
from py_ai_sdk.core.shapes import Rectangle
from py_ai_sdk.core.core_utils import checkType

def boundaryChecks2D_rectangle(map, position):
    checkType(map, Rectangle)
    if position.x < map.upperLeftCorner.x \
    or position.x >= map.upperLeftCorner.x + map.width \
    or position.y < map.upperLeftCorner.y \
    or position.y >= map.upperLeftCorner.y + map.height:
        return False
    return True

def boundaryChecks2D_hexagon(map, position):
    pass

def boundaryChecks2D_circle(map, position):
    pass
