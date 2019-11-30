from draw_sdk.tkinter_singleton import TkinterSingleton
from draw_sdk.colour import Colour

from py_ai_sdk.core.dimensions import Dim2D

def main():
    TkinterSingleton.start()
    tile_size = Dim2D(25, 25)
    grid_size = Dim2D(10, 10)
    for y in range(grid_size.y):
        for x in range(grid_size.x):
            col = Colour.RED
            if x == y:
                col = Colour.BLUE
            TkinterSingleton.create_frame_at(Dim2D(x, y), tile_size, col)

    TkinterSingleton.create_frame_at(Dim2D(2, 3), tile_size, Colour.GREEN)
    TkinterSingleton.create_frame_at(Dim2D(1, 3), tile_size, Colour.BLACK)

    TkinterSingleton.loop()

if __name__ == "__main__":
    main()
