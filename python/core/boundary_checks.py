from dimensions import Dim2D

def boundaryChecks2D_rectangle(position, map):
    if position.x < 0 or position.x >= map.width or position.y < 0 or position.y >= map.height:
        return False
    return True

def boundaryChecks2D_hexagon(position, map):
    pass

def boundaryChecks2D_circle(position, map):
    pass
