import random
from dataclasses import dataclass

from draw.tkinter_singleton import TkinterSingleton
from draw.colour import Colour

from core.dimensions import Dim2D
from core.shapes import Shape2D
from core.graph import Graph

from algorithms.graph_search import GraphSearch

def create_grid(tile_size: Dim2D, grid_size: Dim2D):
    raw_data = []
    for y in range(grid_size.y):
        row_raw_data = []
        for x in range(grid_size.x):
            TkinterSingleton.create_frame_at(Dim2D(x, y), tile_size, Colour.BLACK)
            row_raw_data.append(0)
        raw_data.append(row_raw_data)
    return raw_data

def create_buttons_layer(grid_size: Dim2D):
    @dataclass
    class ButtonData:
        text: str
        position: Dim2D = Dim2D(0, 0)
        span_size: Dim2D = Dim2D(1, 1)
        colour: Colour = Colour.BLACK

    button_data = [
        ButtonData("back"),
        ButtonData("play"),
        ButtonData("stop"),
        ButtonData("restart")
    ]

    number_of_buttons = len(button_data)
    for idx, button in enumerate(button_data):
        # TODO: Should not use division to put them in order, find another way
        # TODO: nsew stickty can make use of rowconfigure and columnconfigure
        # to expand correct all elements in the grid should need it. When it needs
        # to "acquire" another grid element, then it should use rowspan or columnspan
        button.position = Dim2D(idx * (grid_size.x // number_of_buttons), grid_size.y)
        button.span_size = Dim2D(grid_size.x // number_of_buttons, None)
        # TODO: Should use a dataclass to transfer the values for TkInter functions
        TkinterSingleton.create_button_at(
            button.position,
            button.text,
            button.colour,
            grid_span_size=button.span_size
        )

def get_random_edge_point(grid_size):
    four_sides = ["top", "bottom", "left", "right"]
    chosen_side = four_sides[random.randint(0, len(four_sides) - 1)]
    return {
        "top": Dim2D(random.randint(0, grid_size.x - 1), 0),
        "bottom": Dim2D(random.randint(0, grid_size.x - 1), grid_size.y - 1),
        "left": Dim2D(0, random.randint(0, grid_size.y - 1)),
        "right": Dim2D(grid_size.x - 1, random.randint(0, grid_size.y - 1))
    }[chosen_side]

def main():
    TkinterSingleton.start()
    TkinterSingleton.set_weight_of_grid_element(TkinterSingleton.root, Dim2D(0, 0))

    tile_size = Dim2D(20, 20)
    grid_size = Dim2D(30, 30)
    raw_data = create_grid(tile_size, grid_size)
    create_buttons_layer(grid_size)

    graph = Graph(raw_data, Shape2D.Type.RECTANGLE)
    start_point = get_random_edge_point(grid_size)
    graph_search = GraphSearch(graph, start_point)
    neighbour_data = Graph.NeighbourData(Graph.NeighbourData.Type.CROSS, random_output=True)
    paths = graph_search.depth_first_search(neighbour_data)
    update_time_in_ms = 30

    def pop_path(args=None):
        current = paths.pop(0)
        TkinterSingleton.create_frame_at(current, tile_size, Colour.RED)
        if args:
            previous = args[0]
            TkinterSingleton.create_frame_at(previous, tile_size, Colour.WHITE)
        if paths:
            TkinterSingleton.update(pop_path, current, in_milliseconds=update_time_in_ms)

    TkinterSingleton.update(pop_path, in_milliseconds=update_time_in_ms)

    TkinterSingleton.loop()

if __name__ == "__main__":
    main()
