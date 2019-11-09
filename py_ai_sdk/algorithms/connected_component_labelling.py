from py_ai_sdk.core.dimensions import Dim2D
from py_ai_sdk.core.graph import Graph
from py_ai_sdk.core.disjoint_set import DisjointSet

class ConnectedComponentLabeling:

    def __init__(self, graph: Graph, different_labels: list):
        self.graph = graph
        self._labels = None
        # TODO: different_labels can be a part of Graph
        self._set_labels(different_labels)
        self._labels_disjoint_set = DisjointSet()

    def _set_labels(self, different_labels: list):
        self._labels = {}
        for y, row in enumerate(self.graph.raw_data):
            for x, value in enumerate(row):
                self._labels[Dim2D(x, y)] = different_labels.index(value)

    # TODO: Should return a graph?
    def get_labels_graph(self):
        new_grid = []
        for y, row in enumerate(self.graph.raw_data):
            row_list = []
            for x, _ in enumerate(row):
                row_list.append(self._labels[Dim2D(x, y)])
            new_grid.append(row_list)
        return new_grid

    def first_pass(self):
        current_label = 0
        for y, row in enumerate(self.graph.raw_data):
            for x, value in enumerate(row):
                current_pos = Dim2D(x, y)
                if value == 1: # TODO: Background check for now
                    new_labels = []
                    for neighbour in self.graph.get_available_neighbours(current_pos, Graph.NeighbourData(Graph.NeighbourData.Type.CONNECTIVITY_8)):
                        neighbour_value = self._labels[neighbour]
                        if neighbour_value > 0: # Labelled
                            new_labels.append(neighbour_value)

                    if not new_labels:
                        current_label += 1
                        self._labels[current_pos] = current_label
                        self._labels_disjoint_set.make_set(DisjointSet.Element(current_label))
                    else:
                        minimum_label = min(new_labels)
                        self._labels[current_pos] = minimum_label
                        for label in new_labels:
                            self._labels_disjoint_set.union(label, minimum_label)

    def second_pass(self):
        for y, row in enumerate(self.graph.raw_data):
            for x, _ in enumerate(row):
                current_pos = Dim2D(x, y)
                label_value = self._labels[current_pos]
                if label_value != 0: #not background
                    current_element = self._labels_disjoint_set.find(label_value)
                    self._labels[current_pos] = current_element.id_

    def get_regions(self):
        regions = {}
        for y, row in enumerate(self.graph.raw_data):
            for x, _ in enumerate(row):
                current_pos = Dim2D(x, y)
                label_value = self._labels[current_pos]
                try:
                    regions[label_value].append(current_pos)
                except KeyError:
                    regions[label_value] = [current_pos]
        return regions
