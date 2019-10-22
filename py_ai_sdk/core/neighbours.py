from py_ai_sdk.core.dimensions import Dim2D
from py_ai_sdk.core.boundary_checks import boundary_checks_rectangle

def get_neighbours2d_rectangle_4_sides(position):
    x, y = position.x, position.y
    candidates = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    candidates = Dim2D.convert_candiates_to_dimensions(candidates)
    return candidates

def get_neighbours2d_rectangle_8_sides(position):
    x, y = position.x, position.y
    candidates = [
        (x+1, y), (x-1, y), (x, y+1), (x, y-1),
        (x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)
        ]
    candidates = Dim2D.convert_candiates_to_dimensions(candidates)
    return candidates

def get_available_neighbours2d_rectangle(grid, blocking_positions, get_neighbours_function, position):
    neighbours_positions = get_neighbours_function(position)

    for candidate_position in reversed(neighbours_positions):
        is_inside_boundaries = boundary_checks_rectangle(grid, candidate_position)
        if not is_inside_boundaries:
            neighbours_positions.remove(candidate_position)
        elif candidate_position in blocking_positions:
            neighbours_positions.remove(candidate_position)
    return neighbours_positions
