import tkinter as tk
from dataclasses import dataclass
from enum import Enum

from py_ai_sdk.core.dimensions import Dim2D
from py_ai_sdk.core.shapes import Rectangle

# Run python -m applications.first_app to run an exeutable program
# Command to run "pyinstaller applications\first_app\__main__.py -n trial --onefile"
# The executable file should be at "dist" folder with trial.exe

class Colours(Enum):
    RED = "red"
    BLUE = "blue"
    WHITE = "white"
    BROWN = "brown"
    GREEN = "green"
    BLACK = "black"

class TkinterSingleton:
    root = None

    @staticmethod
    def start():
        if TkinterSingleton.root is None:
            TkinterSingleton.root = tk.Tk()
            TkinterSingleton.root.resizable(width=False, height=False)
        else:
            print("Tk root is already initialised")

    @staticmethod
    def set_geometry(size: Dim2D):
        TkinterSingleton.root.geometry(f"{size.x}x{size.y}")

    @staticmethod
    def loop():
        TkinterSingleton.root.mainloop()

@dataclass
class Tile:
    rectangle: Rectangle
    colour: Colours

class Canvas:

    def __init__(self):
        self._canvas = tk.Canvas(TkinterSingleton.root)
        self._draw_map = dict()

    # TODO: Does not seem to belong to Canvas class
    # TODO: Parameters can have defaut values with data class
    @staticmethod
    def get_label(text, text_colour, font_style):
        return tk.Label(
            TkinterSingleton.root,
            text=text,
            fg=text_colour,
            font=font_style
        )

    # TODO: Does not seem to belong to Canvas class
    # TODO: Parameters can have defaut values with data class
    @staticmethod
    def get_button(text, text_colour, background_colour, callback_function):
        return tk.Button(
            TkinterSingleton.root,
            text=text,
            fg=text_colour,
            bg=background_colour,
            command=callback_function
        )

    def add_window(self, size: Dim2D, window):
        self._canvas.create_window(size.x, size.y, window=window)

    def pack(self):
        self._canvas.pack(fill=tk.BOTH, expand=1)

    def create_tile(self, rectangle: Rectangle, colour: Colours):
        self._canvas.create_rectangle(
            rectangle.top_left_corner.x,
            rectangle.top_left_corner.y,
            rectangle.width,
            rectangle.height,
            fill=colour.name,
        )
    
    def create_frame(self, size: Dim2D, colour: Colours):
        return tk.Frame(TkinterSingleton.root, width=size.x, height=size.y, background=colour.name)
    
    def attach_grid(self, row, column, frame):
        frame.grid(row=row, column=column)

    # def draw_tiles(self, tile_size: Dim2D, colour):
    #     tile_size = Dim2D(int(tile_size.x), int(tile_size.y))
    #     number_of_columns = self.size.x // tile_size.x
    #     number_of_rows = self.size.y // tile_size.y
    #     print("number_of_colums", number_of_columns, " number_of_rows", number_of_rows)
    #     for y in range(number_of_rows):
    #         for x in range(number_of_columns):
    #             print("top left", Dim2D(x * tile_size.x, y * tile_size.y))
    #             new_rectangle = Rectangle(
    #                 Dim2D(x * tile_size.x, y * tile_size.y),
    #                 tile_size.x,
    #                 tile_size.y
    #             )
    #             self.create_tile(new_rectangle, colour)
    #             self._draw_map[Dim2D(x, y)] = Tile(new_rectangle, colour)
    #     print("size of draw map", len(self._draw_map))

    def get_size_information(self):
        print(f"Canvas size info {self._canvas.winfo_width()}x{self._canvas.winfo_height()}")

def main():
    TkinterSingleton.start()
    main_window_size = Dim2D(300, 300)
    TkinterSingleton.set_geometry(main_window_size)

    main_canvas = Canvas()
    # main_canvas.pack()

    tile_size = main_window_size.constant_divide(6)
    number_of_columns = int(main_window_size.x // tile_size.x)
    number_of_rows = int(main_window_size.y // tile_size.y)
    for y in range(number_of_rows):
        for x in range(number_of_columns):
            new_rectangle = Rectangle(
                Dim2D(x * tile_size.x, y * tile_size.y),
                tile_size.x,
                tile_size.y
            )
            # main_canvas.create_tile(new_rectangle, Colours.GREEN)
            # main_canvas.attach_grid(y, x)
            col = Colours.RED
            if x == y:
                col = Colours.BLUE
            frame = main_canvas.create_frame(tile_size, col)
            main_canvas.attach_grid(y, x, frame)


    # tile_size = Dim2D(10, 10)
    # tile_size = Dim2D(300, 300)
    # tile_size = Dim2D(150, 150)
    # main_canvas.draw_tiles(tile_size, Colours.GREEN) # TODO: Not sure why it shows two black lines
    main_canvas.create_tile(Rectangle(Dim2D(199, 199), 100, 100), Colours.RED)
    # main_canvas.create_tile(Rectangle(Dim2D(1, 1), 30, 30), Colours.BLUE)
    # main_canvas.get_size_information()

    # main_canvas.pack()

    TkinterSingleton.loop()

if __name__ == "__main__":
    main()
