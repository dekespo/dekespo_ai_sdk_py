from draw_sdk.tkinter_singleton import TkinterSingleton
from draw_sdk.colour import Colour

from py_ai_sdk.core.dimensions import Dim2D

def main():
    TkinterSingleton.start()
    main_window_size = Dim2D(300, 300)
    TkinterSingleton.set_geometry(main_window_size)

    tile_size = main_window_size.constant_divide(6)
    number_of_columns = int(main_window_size.x // tile_size.x)
    number_of_rows = int(main_window_size.y // tile_size.y)
    for y in range(number_of_rows):
        for x in range(number_of_columns):
            col = Colour.RED
            if x == y:
                col = Colour.BLUE
            TkinterSingleton.create_frame_at(Dim2D(x, y), tile_size, col)

    TkinterSingleton.create_frame_at(Dim2D(2, 3), tile_size, Colour.GREEN)
    TkinterSingleton.create_frame_at(Dim2D(1, 3), tile_size, Colour.BLACK)

    TkinterSingleton.loop()

if __name__ == "__main__":
    main()
