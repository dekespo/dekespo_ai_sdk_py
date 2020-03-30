import random

from draw.button import ButtonData, PackData
from draw.tkinter_singleton import TkinterSingleton
from draw.colour import Colour

from core.dimensions import Dim2D
from core.shapes import Shape2D
from core.graph import Graph

from algorithms.graph_search.api import GraphSearch

from .utils import Status, Button, create_rectangle_canvas
from .path_processor import PathProcessor

def create_buttons_layer_canvas(status_dictionary):
    button_data = [
        ButtonData("back", Button.back, status_dictionary),
        ButtonData("next", Button.next, status_dictionary),
        ButtonData("play_forward", Button.play_forward, status_dictionary),
        ButtonData("play_backward", Button.play_backward, status_dictionary),
        ButtonData("stop", Button.stop, status_dictionary),
        ButtonData("restart", Button.restart, status_dictionary)
    ]

    for data in button_data:
        pack_data = PackData()
        data.pack_data = pack_data
        TkinterSingleton.create_button_with_pack(data)

def get_random_edge_point(grid_size):
    four_sides = ["top", "bottom", "left", "right"]
    chosen_side = four_sides[random.randint(0, len(four_sides) - 1)]
    return {
        "top": Dim2D(random.randint(0, grid_size.x - 1), 0),
        "bottom": Dim2D(random.randint(0, grid_size.x - 1), grid_size.y - 1),
        "left": Dim2D(0, random.randint(0, grid_size.y - 1)),
        "right": Dim2D(grid_size.x - 1, random.randint(0, grid_size.y - 1))
    }[chosen_side]

def initialize_gui(tile_size, grid_size, status_dictionary):
    TkinterSingleton.create_canvas(tile_size.vectoral_multiply(grid_size))
    TkinterSingleton.canvas.configure(background=Colour.GREEN.value)
    TkinterSingleton.canvas.pack(fill="both", expand=True)
    create_buttons_layer_canvas(status_dictionary)
    raw_grid_data = create_rectangle_canvas(tile_size, grid_size)
    TkinterSingleton.refresh()
    return raw_grid_data

def initialize_depth_first_search(raw_grid_data, grid_size):
    graph = Graph(raw_grid_data, Shape2D.Type.RECTANGLE)
    start_point = get_random_edge_point(grid_size)
    neighbour_data = Graph.NeighbourData(Graph.NeighbourData.Type.CROSS, random_output=True)
    depth_first_search = GraphSearch(graph, start_point) \
                        .depth_first_search(neighbour_data, runs_with_thread=True)
    depth_first_search.event_set()
    depth_first_search.start()
    return depth_first_search

def main():
    TkinterSingleton.start(title="Graph Search Program")

    # TODO: Set the tile size and grid size with arguments (argparse)
    tile_size = Dim2D(10, 10)
    grid_size = Dim2D(60, 60)
    status_dictionary = {
        Status.ON_PAUSE: True,
        Status.SHOULD_RESTART: False,
        Status.SHOULD_GO_BACK: False,
        Status.SHOULD_GO_NEXT: False,
        Status.SHOULD_PLAY_FORWARD: True
    }

    raw_grid_data = initialize_gui(tile_size, grid_size, status_dictionary)
    depth_first_search = initialize_depth_first_search(raw_grid_data, grid_size)

    path_processor = PathProcessor(
        status_dictionary,
        # TODO: Add slider for the speed (between 1 and 1000)
        update_frame_in_milliseconds=16,
        graph_search_closed_set=depth_first_search.get_closed_set())
    path_processor.set_tile_and_grid_size(tile_size, grid_size)
    path_processor.process()

    TkinterSingleton.loop()
    depth_first_search.kill_thread()
    depth_first_search.join()

if __name__ == "__main__":
    main()
