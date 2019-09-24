import types

from py_ai_sdk.core.dimensions import Dim2D
from py_ai_sdk.core.shapes import Rectangle
from py_ai_sdk.core.boundary_checks import boundaryChecks2D_rectangle
from py_ai_sdk.core.core_utils import checkType

def getNeighbours2D_rectangle_4Sides(position):
    checkType(position, Dim2D)
    x, y = position.x, position.y
    candidates = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    candidates = Dim2D.listToDim2Ds(candidates)
    return candidates

def getNeighbours2D_rectangle_8Sides(position):
    checkType(position, Dim2D)
    x, y = position.x, position.y
    candidates = [
        (x+1, y), (x-1, y), (x, y+1), (x, y-1),
        (x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)
        ]
    candidates = Dim2D.listToDim2Ds(candidates)
    return candidates

def getAvailableNeighbours2D_rectangle(grid, blockingPositions, getNeighboursFunction, position):
    checkType(grid, Rectangle)
    checkType(blockingPositions, list)
    if blockingPositions:
        checkType(blockingPositions[0], Dim2D)
    checkType(position, Dim2D)
    checkType(getNeighboursFunction, types.FunctionType)
    candidates = getNeighboursFunction(position)

    for candi in reversed(candidates):
        isInsideBoundary = boundaryChecks2D_rectangle(grid, candi)
        if not isInsideBoundary:
            candidates.remove(candi)
        elif candi in blockingPositions:
            candidates.remove(candi)
    
    return candidates
