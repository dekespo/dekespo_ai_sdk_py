import unittest

from py_ai_sdk.core.dimensions import Dim2D
from py_ai_sdk.core.graph import Graph
from py_ai_sdk.templates.rectangle_world import example_raw_data
from py_ai_sdk.core.shapes import Shape2D

# TODO: Add non-blocking graph
class GraphTest(unittest.TestCase):
    def test_graph_data_with_blocking(self):
        raw_data = example_raw_data()
        blocking_values = set([1])
        graph = Graph(raw_data, Shape2D.Type.RECTANGLE, blocking_values)
        self.assertTrue(graph.raw_data, example_raw_data())
        self.assertTrue(graph.get_blocking_positions(), [Dim2D(1, 0), Dim2D(3, 0), Dim2D(1, 1)])
        self.assertTrue(graph.graph_shape.check_boundaries(Dim2D(1, 1)))
        self.assertFalse(graph.graph_shape.check_boundaries(Dim2D(-1, 1)))
        pos = Dim2D(1, 1)
        available_poses = graph.get_available_neighbours(Graph.NeighbourType.DIAMOND, pos, 2)
        self.assertEqual(len(available_poses), 7)
        self.assertTrue(Dim2D(0, 0) in available_poses)
        self.assertTrue(Dim2D(0, 2) in available_poses)
        self.assertTrue(Dim2D(1, 2) in available_poses)
        self.assertTrue(Dim2D(2, 0) in available_poses)
        self.assertTrue(Dim2D(2, 1) in available_poses)
        self.assertTrue(Dim2D(2, 2) in available_poses)
        self.assertTrue(Dim2D(3, 1) in available_poses)

    def test_get_neighbours_cross(self):
        pos = Dim2D(1, 1)
        poses = Graph.get_neighbours_cross(pos)
        self.assertEqual(len(poses), 4)
        self.assertTrue(Dim2D(0, 1) in poses)
        self.assertTrue(Dim2D(1, 2) in poses)
        self.assertTrue(Dim2D(2, 1) in poses)
        self.assertTrue(Dim2D(1, 0) in poses)

    def test_get_neighbours_square(self):
        pos = Dim2D(1, 1)
        poses = Graph.get_neighbours_square(pos)
        self.assertEqual(len(poses), 8)
        self.assertTrue(Dim2D(0, 1) in poses)
        self.assertTrue(Dim2D(1, 2) in poses)
        self.assertTrue(Dim2D(2, 1) in poses)
        self.assertTrue(Dim2D(1, 0) in poses)
        self.assertTrue(Dim2D(0, 0) in poses)
        self.assertTrue(Dim2D(2, 2) in poses)
        self.assertTrue(Dim2D(0, 2) in poses)
        self.assertTrue(Dim2D(2, 0) in poses)

    def test_get_neighbours_diamond(self):
        pos = Dim2D(1, 1)
        poses = Graph.get_neighbours_diamond(pos, 2)
        self.assertEqual(len(poses), 12)
        self.assertTrue(Dim2D(0, 1) in poses)
        self.assertTrue(Dim2D(-1, 1) in poses)
        self.assertTrue(Dim2D(1, 2) in poses)
        self.assertTrue(Dim2D(1, 3) in poses)
        self.assertTrue(Dim2D(2, 1) in poses)
        self.assertTrue(Dim2D(3, 1) in poses)
        self.assertTrue(Dim2D(1, 0) in poses)
        self.assertTrue(Dim2D(1, -1) in poses)
        self.assertTrue(Dim2D(0, 0) in poses)
        self.assertTrue(Dim2D(2, 2) in poses)
        self.assertTrue(Dim2D(0, 2) in poses)
        self.assertTrue(Dim2D(2, 0) in poses)


    # TODO: Move some of them into the one with blocking
    # def test_available_rectangle_two_blocks(self):
    #     grid = Rectangle(Dim2D(0, 0), 3, 3)
    #     blocking_positions = Dim2D.convert_candiates_to_dimensions([(1, 1), (0, 1)])
    #     pos1 = Dim2D(0, 2)
    #     available_poses = grid.get_available_neighbours(blocking_positions, Graph.NeighbourType.CROSS, pos1)
    #     self.assertEqual(len(available_poses), 1)
    #     self.assertEqual(available_poses[0], Dim2D(1, 2))
    #     pos2 = Dim2D(1, 2)
    #     available_poses = grid.get_available_neighbours(blocking_positions, Graph.NeighbourType.CROSS, pos2)
    #     self.assertEqual(len(available_poses), 2)
    #     self.assertTrue(Dim2D(0, 2) in available_poses)
    #     self.assertTrue(Dim2D(2, 2) in available_poses)
    #     pos3 = Dim2D(2, 1)
    #     available_poses = grid.get_available_neighbours(blocking_positions, Graph.NeighbourType.SQUARE, pos3)
    #     self.assertEqual(len(available_poses), 4)
    #     self.assertTrue(Dim2D(2, 0) in available_poses)
    #     self.assertTrue(Dim2D(2, 2) in available_poses)
    #     self.assertTrue(Dim2D(1, 0) in available_poses)
    #     self.assertTrue(Dim2D(1, 2) in available_poses)
    #     available_poses = grid.get_available_neighbours(blocking_positions, Graph.NeighbourType.DIAMOND, pos3, 2)
    #     self.assertEqual(len(available_poses), 4)
    #     self.assertTrue(Dim2D(2, 0) in available_poses)
    #     self.assertTrue(Dim2D(2, 2) in available_poses)
    #     self.assertTrue(Dim2D(1, 0) in available_poses)
    #     self.assertTrue(Dim2D(1, 2) in available_poses)

if __name__ == "__main__":
    unittest.main()
