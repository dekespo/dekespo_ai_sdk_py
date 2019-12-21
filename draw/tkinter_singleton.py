import tkinter as tk

from core.dimensions import Dim2D
from core.utils import error_print

from draw.button import ButtonData
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
    def create_button_at(button_data: ButtonData):
        button = tk.Button(
            TkinterSingleton.root,
            text=button_data.text,
            fg=button_data.colour.value,
            command=button_data.callback_function
        )
        button.grid(
            column=button_data.grid_index.x,
            row=button_data.grid_index.y,
            columnspan=button_data.grid_span_size.x,
            rowspan=button_data.grid_span_size.y,
            sticky=button_data.sticky
        )
        TkinterSingleton.set_weight_of_grid_element(button, button_data.grid_index)


    @staticmethod
    def update(callback_function, *args, in_milliseconds=1000):
        def function_to_call():
            return callback_function(args)
        TkinterSingleton.root.after(in_milliseconds, function_to_call)

    @staticmethod
    def loop():
        TkinterSingleton.root.mainloop()
