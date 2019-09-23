from py_ai_sdk.core.shapes import Rectangle
from py_ai_sdk.core.core_utils import checkType

def boundaryChecks2D_rectangle(grid, position):
    checkType(grid, Rectangle)
    if position.x < grid.upperLeftCorner.x \
    or position.x >= grid.upperLeftCorner.x + grid.width \
    or position.y < grid.upperLeftCorner.y \
    or position.y >= grid.upperLeftCorner.y + grid.height:
        return False
    return True
