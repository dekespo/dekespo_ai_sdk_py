from py_ai_sdk.core.dimensions import Dim2D
from py_ai_sdk.core.graph import Graph
from py_ai_sdk.core.disjoint_set import DisjointSet
from py_ai_sdk.core.core_utils import error_print

class ConnectedComponentLabeling:

    @property
    def labels(self):
        return self._labels 

    def __init__(self, graph: Graph, different_labels: list):
        self.graph = graph
        self._labels = None
        # TODO: different_labels can be a part of Graph
        self._set_labels(different_labels)
        self.linked = []
        self._labels_disjoint_set = DisjointSet()
        # self._labels = "TODO: structure with dimensions of data, initialized with the value of Background"
        self.second_pass()

    def _set_labels(self, different_labels: list):
        self._labels = {}
        for y, row in enumerate(self.graph.raw_data):
            for x, value in enumerate(row):
                self._labels[Dim2D(x, y)] = different_labels.index(value)

    def print_labels(self):
        new_grid = []
        for y, row in enumerate(self.graph.raw_data):
            row_list = []
            for x, _ in enumerate(row):
                row_list.append(self._labels[Dim2D(x, y)])
            new_grid.append(row_list)
            error_print(row_list)
        return new_grid

    def first_pass(self):
        current_label = 0
        for y, row in enumerate(self.graph.raw_data):
            for x, value in enumerate(row):
                current_pos = Dim2D(x, y)
                if value == 1: # TODO: Background check for now
                    # neighbour_data = Graph.NeighbourData(Graph.NeighbourData.Type.CROSS) # Should be NW 4
                    # new_neighbours = self.graph.get_available_neighbours(Dim2D(x, y), neighbour_data)
                    new_neighbours = Graph.get_neighbours_half_north_west_cross(current_pos)
                    new_labels = []
                    for neighbour in new_neighbours:
                        neighbour_value = self._labels[neighbour]
                        if  neighbour_value > 0: # Labelled
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
        pass

        # algorithm TwoPass(data)
        # linked = []
        # labels = structure with dimensions of data, initialized with the value of Background

        # First pass

        # for row in data:
        #     for column in row:
        #         if data[row][column] is not Background

        #             neighbors = connected elements with the current element's value

        #             if neighbors is empty
        #                 linked[NextLabel] = set containing NextLabel
        #                 labels[row][column] = NextLabel
        #                 NextLabel += 1

        #             else

        #                 Find the smallest label

        #                 L = neighbors labels
        #                 labels[row][column] = min(L)
        #                 for label in L
        #                     linked[label] = union(linked[label], L)

        # Second pass

        # for row in data
        #     for column in row
        #         if data[row][column] is not Background
        #             labels[row][column] = find(labels[row][column])

        # return labels
