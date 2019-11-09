import unittest

from py_ai_sdk.templates.rectangle_world import example_different_regions
from py_ai_sdk.algorithms.connected_component_labelling import ConnectedComponentLabeling
from py_ai_sdk.core.graph import Graph
from py_ai_sdk.core.shapes import Shape2D

class ConnectedComponentLabellingTest(unittest.TestCase):

    def test_simple(self):
        raw_data = example_different_regions()
        graph = Graph(raw_data, Shape2D.Type.RECTANGLE)
        labeller = ConnectedComponentLabeling(graph, [0, 1])
        labeller.first_pass()
        first_pass_data = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 2, 2, 0, 0, 3, 3, 0, 0, 4, 4, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 3, 3, 3, 3, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0],
            [0, 0, 1, 1, 1, 1, 0, 0, 0, 3, 3, 3, 0, 0, 3, 3, 0],
            [0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 3, 3, 3, 0, 0, 0],
            [0, 0, 1, 1, 0, 0, 0, 0, 0, 5, 3, 0, 0, 0, 3, 3, 0],
            [0, 0, 0, 0, 0, 0, 6, 6, 5, 3, 0, 0, 7, 3, 3, 3, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(labeller.print_labels(), first_pass_data)

if __name__ == "__main__":
    unittest.main()
