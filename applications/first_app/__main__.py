import tkinter as tk
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


class TkinterSingleton:
    root = None

    @staticmethod
    def start():
        if TkinterSingleton.root is None:
            TkinterSingleton.root = tk.Tk()
        else:
            print("Tk root is already initialised")

    @staticmethod
    def loop():
        TkinterSingleton.root.mainloop()

class Canvas:

    def __init__(self, size: Dim2D):
        self.size = size
        self._canvas = tk.Canvas(TkinterSingleton.root, width=self.size.x, height=self.size.y)

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
        self._canvas.pack()

    def create_tile(self, rectangle: Rectangle, colour: Colours):
        self._canvas.create_rectangle(
            rectangle.top_left_corner.x,
            rectangle.top_left_corner.y,
            rectangle.width,
            rectangle.height,
            fill=colour.name
        )


def main():
    TkinterSingleton.start()
    main_window_size = Dim2D(300, 300)

    canvas1 = Canvas(main_window_size)
    canvas1.pack()

    def hello():
        label1 = Canvas.get_label(
            'Hello World!',
            Colours.GREEN.value,
            ('helvetica', 12, 'bold') # TODO: Should use enum with dataclass instead?
        )
        start_point = Dim2D(150, 200)
        canvas1.add_window(start_point, window=label1)

    button1 = Canvas.get_button(
        'Click Me',
        Colours.WHITE.value,
        Colours.BROWN.value,
        hello
    )
    start_point = Dim2D(150, 150)
    canvas1.add_window(start_point, window=button1)

    tile = Rectangle(Dim2D(0, 0), 50, 50)
    canvas1.create_tile(tile, Colours.GREEN)

    TkinterSingleton.loop()

if __name__ == "__main__":
    main()
