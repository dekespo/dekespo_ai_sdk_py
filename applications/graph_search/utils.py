import random
from enum import Enum, auto
from dataclasses import dataclass

from draw.tkinter_singleton import TkinterSingleton
from draw.colour import Colour

from core.dimensions import Dim2D
from core.graph import Graph

from algorithms.graph_search.api import GraphSearch

class Status(Enum):
    ON_PAUSE = auto()
    SHOULD_RESTART = auto()
    SHOULD_GO_BACK = auto()
    SHOULD_GO_NEXT = auto()
    SHOULD_PLAY_FORWARD = auto()
    SHOULD_RESET = auto()

@dataclass
class GraphData:
    tile_size: Dim2D
    grid_size: Dim2D
    graph: Graph

class Button:

    # TODO: Have reset button
    @staticmethod
    def back(status_dictionary):
        status_dictionary[Status.SHOULD_GO_BACK] = True

    @staticmethod
    def next(status_dictionary):
        status_dictionary[Status.SHOULD_GO_NEXT] = True

    @staticmethod
    def play_forward(status_dictionary):
        status_dictionary[Status.ON_PAUSE] = False
        status_dictionary[Status.SHOULD_PLAY_FORWARD] = True

    @staticmethod
    def play_backward(status_dictionary):
        status_dictionary[Status.ON_PAUSE] = False
        status_dictionary[Status.SHOULD_PLAY_FORWARD] = False

    @staticmethod
    def pause(status_dictionary):
        status_dictionary[Status.ON_PAUSE] = True

    @staticmethod
    def restart(status_dictionary):
        status_dictionary[Status.SHOULD_RESTART] = True

    @staticmethod
    def reset(status_dictionary):
        status_dictionary[Status.SHOULD_RESET] = True

class Utils:

    @staticmethod
    def create_rectangle_canvas(graph_data: GraphData):
        raw_data = []
        for y in range(graph_data.grid_size.y):
            row_raw_data = []
            for x in range(graph_data.grid_size.x):
                TkinterSingleton.create_rectangle_at(
                    Dim2D(x, y),
                    graph_data.tile_size,
                    Colour.BLACK
                )
                row_raw_data.append(0)
            raw_data.append(row_raw_data)
        return raw_data

    @staticmethod
    def get_random_edge_point(grid_size):
        four_sides = ["top", "bottom", "left", "right"]
        chosen_side = four_sides[random.randint(0, len(four_sides) - 1)]
        return {
            "top": Dim2D(random.randint(0, grid_size.x - 1), 0),
            "bottom": Dim2D(random.randint(0, grid_size.x - 1), grid_size.y - 1),
            "left": Dim2D(0, random.randint(0, grid_size.y - 1)),
            "right": Dim2D(grid_size.x - 1, random.randint(0, grid_size.y - 1))
        }[chosen_side]

    @staticmethod
    def initialize_depth_first_search(graph_data: GraphData):
        start_point = Utils.get_random_edge_point(graph_data.grid_size)
        neighbour_data = Graph.NeighbourData(Graph.NeighbourData.Type.CROSS, random_output=True)
        depth_first_search = GraphSearch(graph_data.graph, start_point) \
                            .depth_first_search(neighbour_data, runs_with_thread=True)
        depth_first_search.event_set()
        depth_first_search.start()
        return depth_first_search
