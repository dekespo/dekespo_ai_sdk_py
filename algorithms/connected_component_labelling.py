from dataclasses import dataclass
from enum import Enum, auto

from core.dimensions import Dim2D
from core.graph import Graph
from core.disjoint_set import DisjointSet

class ConnectedComponentLabelling:
    '''
    Works in only binary format data
    '''

    @dataclass
    class _Node:
        position: Dim2D
        graph_binary_value: bool
        label_value: int = 0

    class ConnectivityType(Enum):
        FOUR = auto()
        EIGHT = auto()

    def __init__(self, graph: Graph, connectivity_type: ConnectivityType):
        self.graph = graph
        self._get_neighbour_function = {
            ConnectedComponentLabelling.ConnectivityType.FOUR : \
                self._get_neighbour_function_4_connectivity,
            ConnectedComponentLabelling.ConnectivityType.EIGHT : \
                self._get_neighbour_function_8_connectivity
        }[connectivity_type]
        self._nodes = None
        self._set_nodes()
        self._labels_disjoint_set = DisjointSet()

    def _set_nodes(self):
        self._nodes = {}
        for y, row in enumerate(self.graph.raw_data_handler.raw_data):
            for x, graph_value in enumerate(row):
                self._nodes[Dim2D(x, y)] = ConnectedComponentLabelling._Node(
                    Dim2D(x, y),
                    graph_value not in self.graph.blocking_values
                )

    # TODO: Should return a graph?
    def get_labels_graph(self):
        new_grid = []
        for y, row in enumerate(self.graph.raw_data_handler.raw_data):
            row_list = []
            for x, _ in enumerate(row):
                row_list.append(self._nodes[Dim2D(x, y)].label_value)
            new_grid.append(row_list)
        return new_grid

    # TODO: Maybe move them to grpah class with better function names
    @staticmethod
    def _get_neighbour_function_8_connectivity(position, _):
        x, y = position.x, position.y
        candidates = [
            (x - 1, y),
            (x - 1, y - 1),
            (x, y - 1),
            (x + 1, y - 1)
        ]
        candidates = Dim2D.convert_candiates_to_dimensions(candidates)
        return candidates

    @staticmethod
    def _get_neighbour_function_4_connectivity(position, _):
        x, y = position.x, position.y
        candidates = [
            (x - 1, y),
            (x, y - 1)
        ]
        candidates = Dim2D.convert_candiates_to_dimensions(candidates)
        return candidates


    def first_pass(self):

        def is_already_labelled(node):
            return node.label_value > 0

        current_label = 0
        for current_node in self._nodes.values():
            if current_node.graph_binary_value:
                new_labels = []
                for neighbour_position in self.graph.get_available_neighbours(
                        current_node.position,
                        Graph.NeighbourData(
                            Graph.NeighbourData.Type.CUSTOM,
                            custom_function=self._get_neighbour_function
                        ),
                        should_block=False
                    ):
                    neighbour_node = self._nodes[neighbour_position]
                    if is_already_labelled(neighbour_node):
                        new_labels.append(neighbour_node.label_value)

                if not new_labels:
                    current_label += 1
                    current_node.label_value = current_label
                    self._labels_disjoint_set.make_set(DisjointSet.Element(current_label))
                else:
                    minimum_label = min(new_labels)
                    current_node.label_value = minimum_label
                    for label in new_labels:
                        self._labels_disjoint_set.union(label, minimum_label)

    def second_pass(self):
        for current_node in self._nodes.values():
            if current_node.graph_binary_value:
                current_node.label_value = self._labels_disjoint_set \
                                            .find(current_node.label_value) \
                                            .id_

    def get_regions(self):
        regions = {}
        for current_node in self._nodes.values():
            try:
                regions[current_node.label_value].append(current_node.position)
            except KeyError:
                regions[current_node.label_value] = [current_node.position]
        return regions
