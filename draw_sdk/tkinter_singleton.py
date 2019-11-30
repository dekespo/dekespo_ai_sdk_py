import tkinter as tk

from py_ai_sdk.core.dimensions import Dim2D
from py_ai_sdk.core.core_utils import error_print

from draw_sdk.colour import Colour

class TkinterSingleton:
    root = None

    @staticmethod
    def start():
        if TkinterSingleton.root is None:
            TkinterSingleton.root = tk.Tk()
            TkinterSingleton.root.resizable(width=False, height=False)
        else:
            error_print("Tk root is already initialised")

    @staticmethod
    def set_geometry(size: Dim2D):
        TkinterSingleton.root.geometry(f"{size.x}x{size.y}")

    @staticmethod
    def create_frame_at(grid_index: Dim2D, frame_size: Dim2D, colour: Colour):
        frame = tk.Frame(
            TkinterSingleton.root,
            width=frame_size.x,
            height=frame_size.y,
            background=colour.name
        )
        frame.grid(column=grid_index.x, row=grid_index.y)

    @staticmethod
    def update(callback_function, in_milliseconds=1000):
        TkinterSingleton.root.after(in_milliseconds, callback_function)

    @staticmethod
    def loop():
        TkinterSingleton.root.mainloop()
