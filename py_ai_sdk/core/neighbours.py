from py_ai_sdk.core.dimensions import Dim2D
from py_ai_sdk.core.boundary_checks import boundary_checks_rectangle

def getNeighbours2D_rectangle_4Sides(position):
    x, y = position.x, position.y
    candidates = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    candidates = Dim2D.convert_candiates_to_dimensions(candidates)
    return candidates

def getNeighbours2D_rectangle_8Sides(position):
    x, y = position.x, position.y
    candidates = [
        (x+1, y), (x-1, y), (x, y+1), (x, y-1),
        (x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)
        ]
    candidates = Dim2D.convert_candiates_to_dimensions(candidates)
    return candidates

def getAvailableNeighbours2D_rectangle(grid, blockingPositions, getNeighboursFunction, position):
    neighbours_positions = getNeighboursFunction(position)

    for candidate_position in reversed(neighbours_positions):
        is_inside_boundaries = boundary_checks_rectangle(grid, candidate_position)
        if not is_inside_boundaries:
            neighbours_positions.remove(candidate_position)
        elif candidate_position in blockingPositions:
            neighbours_positions.remove(candidate_position)
    return neighbours_positions
