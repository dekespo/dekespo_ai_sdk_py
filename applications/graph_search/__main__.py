import random

from draw.button import ButtonData, Button
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
    button_data = [
        ButtonData("back", Button.back),
        ButtonData("play", Button.play),
        ButtonData("stop", Button.stop),
        ButtonData("restart", Button.restart)
    ]

    number_of_buttons = len(button_data)
    for idx, button in enumerate(button_data):
        # TODO: Should not use division to put them in order, find another way
        # TODO: nsew stickty can make use of rowconfigure and columnconfigure
        # to expand correct all elements in the grid should need it. When it needs
        # to "acquire" another grid element, then it should use rowspan or columnspan
        button.grid_index = Dim2D(idx * (grid_size.x // number_of_buttons), grid_size.y)
        button.grid_span_size = Dim2D(grid_size.x // number_of_buttons, None)

        TkinterSingleton.create_button_at(button)

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
    TkinterSingleton.start(title="Graph Search Program")
    TkinterSingleton.set_weight_of_grid_element(TkinterSingleton.root, Dim2D(0, 0))

    # TODO: Set the tile size and grid size with arguments (argparse)
    tile_size = Dim2D(20, 20)
    grid_size = Dim2D(30, 30)
    raw_data = create_grid(tile_size, grid_size)
    create_buttons_layer(grid_size)

    graph = Graph(raw_data, Shape2D.Type.RECTANGLE)
    start_point = get_random_edge_point(grid_size)
    neighbour_data = Graph.NeighbourData(Graph.NeighbourData.Type.CROSS, random_output=True)
    # TODO: Add slider for the speed
    update_time_in_ms = 30

    def update_path(args=None):
        if args:
            previous = args[0]
            TkinterSingleton.create_frame_at(previous, tile_size, Colour.WHITE)
            current_point = previous
        else:
            current_point = start_point
        x, y = current_point
        graph.raw_data[y][x] = 1
        graph.update_blocking_values([1])
        graph_search = GraphSearch(graph, current_point)
        next_points = graph_search.depth_first_search(neighbour_data, depth_size=2)
        if len(next_points) == 2:
            next_point = next_points[1]
            TkinterSingleton.create_frame_at(next_point, tile_size, Colour.RED)
            TkinterSingleton.update(update_path, next_point, in_milliseconds=update_time_in_ms)

    TkinterSingleton.update(update_path, in_milliseconds=update_time_in_ms)

    TkinterSingleton.loop()

if __name__ == "__main__":
    main()
