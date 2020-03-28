import tkinter as tk

from core.dimensions import Dim2D
from core.utils import error_print

from draw.button import ButtonData
from draw.colour import Colour

# TODO: Should not use singleton but inherit an abstract class with fundamental methods
class TkinterSingleton:
    root = None
    canvas = None

    frames = {}
    rectangles = {}

    @staticmethod
    def start(title, resizeable=(False, False)):
        if TkinterSingleton.root is None:
            TkinterSingleton.root = tk.Tk()
            TkinterSingleton.root.title(title)
            TkinterSingleton.root.resizable(width=resizeable[0], height=resizeable[1])
        else:
            error_print("Tk root is already initialised")

    @staticmethod
    def set_geometry(size: Dim2D):
        TkinterSingleton.root.geometry(f"{size.x}x{size.y}")

    @staticmethod
    def create_canvas(size: Dim2D):
        TkinterSingleton.canvas = tk.Canvas(TkinterSingleton.root, width=size.x, height=size.y)

    @staticmethod
    def set_weight_of_grid_element(element, grid_index: Dim2D, weight=1):
        element.rowconfigure(grid_index.y, weight=weight)
        element.columnconfigure(grid_index.x, weight=weight)

    @staticmethod
    def create_frame_at(grid_index: Dim2D, frame_size: Dim2D, colour: Colour):
        if grid_index in TkinterSingleton.frames:
            frame = TkinterSingleton.frames[grid_index]
            frame.configure(background=colour.value)
        else:
            frame = tk.Frame(
                TkinterSingleton.root,
                width=frame_size.x,
                height=frame_size.y,
                background=colour.value
            )
            TkinterSingleton.frames[grid_index] = frame
            frame.grid(column=grid_index.x, row=grid_index.y)
            TkinterSingleton.set_weight_of_grid_element(frame, grid_index)

    @staticmethod
    def create_rectangle_at(grid_index: Dim2D, tile_size: Dim2D, colour: Colour):
        if grid_index in TkinterSingleton.rectangles:
            rectangle = TkinterSingleton.rectangles[grid_index]
            TkinterSingleton.canvas.itemconfig(rectangle, fill=colour.value, outline=colour.value)
        else:
            coordinates = (
                grid_index.x * tile_size.x + 1,
                grid_index.y * tile_size.y + 1,
                (grid_index.x + 1) * tile_size.x + 1,
                (grid_index.y + 1) * tile_size.y + 1,
            )
            rectangle = TkinterSingleton.canvas.create_rectangle(
                coordinates,
                fill=colour.value,
                outline=colour.value
            )
            TkinterSingleton.rectangles[grid_index] = rectangle

    @staticmethod
    def create_button_at(button_data: ButtonData):
        button = tk.Button(
            TkinterSingleton.root,
            text=button_data.text,
            fg=button_data.colour.value,
            command=lambda: button_data.callback_function(button_data.parameters)
        )
        button.grid(
            column=button_data.grid_data.index.x,
            row=button_data.grid_data.index.y,
            columnspan=button_data.grid_data.span_size.x,
            rowspan=button_data.grid_data.span_size.y,
            sticky=button_data.grid_data.sticky
        )
        TkinterSingleton.set_weight_of_grid_element(button, button_data.grid_index)

    @staticmethod
    def create_button_with_pack(button_data: ButtonData):
        button = tk.Button(
            TkinterSingleton.root,
            text=button_data.text,
            fg=button_data.colour.value,
            command=lambda: button_data.callback_function(button_data.parameters)
        )
        button.pack(
            side=button_data.pack_data.side,
            fill=button_data.pack_data.fill,
            expand=button_data.pack_data.expand
        )

    @staticmethod
    def update(callback_function, *args, in_milliseconds=1000):
        def function_to_call():
            return callback_function(args)
        TkinterSingleton.root.after(in_milliseconds, function_to_call)

    @staticmethod
    def refresh():
        TkinterSingleton.root.update()

    @staticmethod
    def loop():
        TkinterSingleton.root.mainloop()
