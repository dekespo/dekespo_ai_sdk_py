import tkinter as tk

from core.dimensions import Dim2D
from core.utils import error_print

from draw.colour import Colour

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
    def set_weight_of_grid_element(element, grid_index: Dim2D, weight=1):
        element.rowconfigure(grid_index.y, weight=weight)
        element.columnconfigure(grid_index.x, weight=weight)

    @staticmethod
    def create_frame_at(grid_index: Dim2D, frame_size: Dim2D, colour: Colour):
        frame = tk.Frame(
            TkinterSingleton.root,
            width=frame_size.x,
            height=frame_size.y,
            background=colour.value
        )
        frame.grid(column=grid_index.x, row=grid_index.y)
        TkinterSingleton.set_weight_of_grid_element(frame, grid_index)

    @staticmethod
    def create_button_at(
            grid_index: Dim2D, text: str, colour: Colour,
            sticky="nsew", grid_span_size=Dim2D(1, 1)):
        button = tk.Button(
            TkinterSingleton.root,
            text=text,
            fg=colour.value
        )
        button.grid(
            column=grid_index.x,
            row=grid_index.y,
            columnspan=grid_span_size.x,
            rowspan=grid_span_size.y,
            sticky=sticky
        )
        TkinterSingleton.set_weight_of_grid_element(button, grid_index)


    @staticmethod
    def update(callback_function, *args, in_milliseconds=1000):
        def function_to_call():
            return callback_function(args)
        TkinterSingleton.root.after(in_milliseconds, function_to_call)

    @staticmethod
    def loop():
        TkinterSingleton.root.mainloop()
