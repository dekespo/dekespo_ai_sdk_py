def boundaryChecks2D_rectangle(grid, position):
    if position.x < grid.upperLeftCorner.x \
    or position.x >= grid.upperLeftCorner.x + grid.width \
    or position.y < grid.upperLeftCorner.y \
    or position.y >= grid.upperLeftCorner.y + grid.height:
        return False
    return True
