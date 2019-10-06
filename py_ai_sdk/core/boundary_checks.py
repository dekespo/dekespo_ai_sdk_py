def boundary_checks_rectangle(grid, position):
    if position.x < grid.top_left_corner.x \
    or position.x >= grid.top_left_corner.x + grid.width \
    or position.y < grid.top_left_corner.y \
    or position.y >= grid.top_left_corner.y + grid.height:
        return False
    return True
