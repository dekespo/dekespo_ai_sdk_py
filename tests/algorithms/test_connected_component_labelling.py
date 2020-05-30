import unittest

from templates.rectangle_world import example_wiki_ccl, example_simple_different_regions
from algorithms.connected_component_labelling import ConnectedComponentLabelling
from core.graph import Graph
from core.shapes import Shape2D
from core.dimensions import Dim2D
from core.raw_data_handler import RawDataHandler

class ConnectedComponentLabellingTest(unittest.TestCase):

    def test_wiki_example(self):
        raw_data_handler = RawDataHandler(example_wiki_ccl())
        graph = Graph(raw_data_handler, Shape2D.Type.RECTANGLE, blocking_values=[0])
        labeller = ConnectedComponentLabelling(
            graph,
            ConnectedComponentLabelling.ConnectivityType.EIGHT
        )
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
        self.assertEqual(labeller.get_labels_graph(), first_pass_data)
        labeller.second_pass()
        second_pass_data = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 4, 4, 0, 0, 4, 4, 0],
            [0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 4, 4, 4, 4, 0, 0],
            [0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 4, 4, 4, 4, 0, 0, 0],
            [0, 0, 2, 2, 2, 2, 0, 0, 0, 4, 4, 4, 0, 0, 4, 4, 0],
            [0, 2, 2, 2, 0, 0, 2, 2, 0, 0, 0, 4, 4, 4, 0, 0, 0],
            [0, 0, 2, 2, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 4, 4, 0],
            [0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 0, 0, 4, 4, 4, 4, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(labeller.get_labels_graph(), second_pass_data)
        regions = labeller.get_regions()
        self.assertEqual(len(regions), 3)
        self.assertTrue(Dim2D(0, 0) in regions[0])
        self.assertTrue(Dim2D(8, 3) in regions[0])
        self.assertTrue(Dim2D(11, 6) in regions[0])
        self.assertTrue(Dim2D(1, 2) in regions[2])
        self.assertTrue(Dim2D(4, 4) in regions[2])
        self.assertTrue(Dim2D(15, 1) in regions[4])
        self.assertTrue(Dim2D(13, 5) in regions[4])

    def test_different_regions_8_connectivity(self):
        raw_data_handler = RawDataHandler(example_simple_different_regions())
        graph = Graph(raw_data_handler, Shape2D.Type.RECTANGLE, blocking_values=[1])
        labeller = ConnectedComponentLabelling(
            graph,
            ConnectedComponentLabelling.ConnectivityType.EIGHT
        )
        labeller.first_pass()
        labeller.second_pass()
        regions = labeller.get_regions()
        self.assertEqual(len(regions), 3)
        self.assertTrue(Dim2D(0, 1) in regions[0])
        self.assertTrue(Dim2D(2, 1) in regions[0])
        self.assertTrue(Dim2D(5, 4) in regions[0])
        self.assertTrue(Dim2D(0, 0) in regions[2])
        self.assertTrue(Dim2D(0, 4) in regions[2])
        self.assertTrue(Dim2D(6, 0) in regions[2])
        self.assertTrue(Dim2D(6, 4) in regions[2])
        self.assertTrue(Dim2D(3, 0) in regions[2])
        self.assertTrue(Dim2D(3, 4) in regions[2])
        self.assertTrue(Dim2D(1, 2) in regions[2])
        self.assertTrue(Dim2D(5, 2) in regions[2])
        self.assertTrue(Dim2D(3, 2) in regions[4])

    def test_different_regions_4_connectivity(self):
        raw_data_handler = RawDataHandler(example_simple_different_regions())
        graph = Graph(raw_data_handler, Shape2D.Type.RECTANGLE, blocking_values=[1])
        labeller = ConnectedComponentLabelling(
            graph,
            ConnectedComponentLabelling.ConnectivityType.FOUR
        )
        labeller.first_pass()
        labeller.second_pass()
        regions = labeller.get_regions()
        self.assertEqual(len(regions), 10)
        self.assertTrue(Dim2D(0, 1) in regions[0])
        self.assertTrue(Dim2D(2, 1) in regions[0])
        self.assertTrue(Dim2D(5, 4) in regions[0])
        self.assertTrue(Dim2D(0, 0) in regions[1])
        self.assertTrue(Dim2D(0, 4) in regions[7])
        self.assertTrue(Dim2D(6, 0) in regions[3])
        self.assertTrue(Dim2D(6, 4) in regions[9])
        self.assertTrue(Dim2D(3, 2) in regions[6])
        self.assertTrue(Dim2D(3, 0) in regions[2])
        self.assertTrue(Dim2D(3, 4) in regions[8])
        self.assertTrue(Dim2D(1, 2) in regions[4])
        self.assertTrue(Dim2D(5, 2) in regions[5])


if __name__ == "__main__":
    unittest.main()
