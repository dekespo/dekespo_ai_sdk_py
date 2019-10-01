from py_ai_sdk.core.dimensions import Dim2D
from py_ai_sdk.core.boundary_checks import boundaryChecks2D_rectangle

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
    candidates = getNeighboursFunction(position)

    for candi in reversed(candidates):
        isInsideBoundary = boundaryChecks2D_rectangle(grid, candi)
        if not isInsideBoundary:
            candidates.remove(candi)
        elif candi in blockingPositions:
            candidates.remove(candi)
    return candidates
