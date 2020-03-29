import random

from draw.button import ButtonData, GridData, PackData
from draw.tkinter_singleton import TkinterSingleton
from draw.colour import Colour

from core.dimensions import Dim2D
from core.shapes import Shape2D
from core.graph import Graph

from algorithms.graph_search.api import GraphSearch

from .utils import Status, Button

def create_grid(tile_size: Dim2D, grid_size: Dim2D):
    raw_data = []
    for y in range(grid_size.y):
        row_raw_data = []
        for x in range(grid_size.x):
            TkinterSingleton.create_frame_at(Dim2D(x, y), tile_size, Colour.BLACK)
            row_raw_data.append(0)
        raw_data.append(row_raw_data)
    return raw_data

def create_rectangles(tile_size: Dim2D, grid_size: Dim2D):
    raw_data = []
    for y in range(grid_size.y):
        row_raw_data = []
        for x in range(grid_size.x):
            TkinterSingleton.create_rectangle_at(Dim2D(x, y), tile_size, Colour.BLACK)
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
        # This was with grid rectangle
        grid_data = GridData()
        grid_data.index = Dim2D(idx * (grid_size.x // number_of_buttons), grid_size.y)
        grid_data.span_size = Dim2D(grid_size.x // number_of_buttons, None)
        button.grid_data = grid_data

        TkinterSingleton.create_button_at(button)

def create_buttons_layer_canvas(status_dictionary):
    button_data = [
        ButtonData("back", Button.back, status_dictionary),
        ButtonData("play", Button.play, status_dictionary),
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

def main():
    TkinterSingleton.start(title="Graph Search Program")

    # TODO: Set the tile size and grid size with arguments (argparse)
    tile_size = Dim2D(10, 10)
    grid_size = Dim2D(60, 60)

    # TODO: put all first UI element creation into the same place
    # Canvas with pack
    TkinterSingleton.create_canvas(tile_size.vectoral_multiply(grid_size))
    TkinterSingleton.canvas.configure(background=Colour.GREEN.value)
    TkinterSingleton.canvas.pack(fill="both", expand=True)
    status_dictionary = {
        Status.ON_PAUSE: True,
        Status.SHOULD_RESTART: False,
        Status.SHOULD_GO_BACK: False
    }
    create_buttons_layer_canvas(status_dictionary)

    # Create rectangles on the canvas
    raw_data = create_rectangles(tile_size, grid_size)

    # Draw the elements before starting
    TkinterSingleton.refresh()

    # DFS functionality
    graph = Graph(raw_data, Shape2D.Type.RECTANGLE)
    start_point = get_random_edge_point(grid_size)
    neighbour_data = Graph.NeighbourData(Graph.NeighbourData.Type.CROSS, random_output=True)
    dfs = GraphSearch(graph, start_point).depth_first_search(neighbour_data, runs_with_thread=True)
    dfs.event_set()
    dfs.start()

    # TODO: Add slider for the speed (between 1 and 1000)
    update_time_in_ms = 16 # for 60 fps

    start_index = 0
    closed_set = dfs.get_closed_set()
    def update_path(args):
        current_path_index = args[0]
        if status_dictionary[Status.SHOULD_RESTART]:
            create_rectangles(tile_size, grid_size)
            current_path_index = start_index
            status_dictionary[Status.SHOULD_RESTART] = False
        if status_dictionary[Status.SHOULD_GO_BACK]:
            if current_path_index > start_index + 1:
                current_path_index -= 1
                previous_point = closed_set[current_path_index-1]
                TkinterSingleton.create_rectangle_at(previous_point, tile_size, Colour.RED)
                current_point = closed_set[current_path_index]
                TkinterSingleton.create_rectangle_at(current_point, tile_size, Colour.BLACK)
            status_dictionary[Status.SHOULD_GO_BACK] = False
            status_dictionary[Status.ON_PAUSE] = True
        if status_dictionary[Status.ON_PAUSE]:
            TkinterSingleton.update(
                update_path,
                current_path_index,
                in_milliseconds=update_time_in_ms
            )
            return
        if current_path_index > start_index:
            previous_point = closed_set[current_path_index-1]
            TkinterSingleton.create_rectangle_at(previous_point, tile_size, Colour.WHITE)
        if current_path_index < len(closed_set):
            # TODO: This part goes up to some 33 ms until dfs thread is done, find what causes this?
            current = closed_set[current_path_index]
            TkinterSingleton.create_rectangle_at(current, tile_size, Colour.RED)
            current_path_index += 1
            TkinterSingleton.update(
                update_path,
                current_path_index,
                in_milliseconds=update_time_in_ms
            )
            return
        if current_path_index == len(closed_set):
            previous = closed_set[current_path_index-1]
            TkinterSingleton.create_rectangle_at(previous, tile_size, Colour.RED)

    TkinterSingleton.update(update_path, start_index, in_milliseconds=update_time_in_ms)

    TkinterSingleton.loop()
    dfs.kill_thread()
    dfs.join()

if __name__ == "__main__":
    main()
