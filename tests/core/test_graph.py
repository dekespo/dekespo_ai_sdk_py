import unittest

from core.dimensions import Dim2D
from core.graph import Graph
from core.shapes import Shape2D
from core.raw_data_handler import RawDataHandler
from core.neighbour import Neighbour

from templates.rectangle_world import (
    example_small_random,
    example_unreachable_positions,
)

# TODO: Add non-blocking (empty) graph
# TODO: Separate test_graph_data_with_blocking into small unittests with setup
class GraphTest(unittest.TestCase):
    def test_graph_data_with_blocking(self):
        raw_data_handler = RawDataHandler(example_small_random())
        graph = Graph(raw_data_handler, Shape2D.Type.RECTANGLE)
        self.assertTrue(
            str(graph),
            """
                                    Shape Type: Type.RECTANGLE
                                    Raw data:
                                    0 |1 |0 |1
                                    1 |0 |0 |0
                                    0 |0 |0 |0
                                    """,
        )
        self.assertTrue(graph.raw_data_handler, example_small_random())
        self.assertIsNone(graph.blocking_values)
        self.assertListEqual(graph.blocking_positions, [])
        new_blocking_values = set([1])
        graph.update_blocking_data(new_blocking_values)
        self.assertTrue(graph.blocking_values, set([1]))
        self.assertTrue(
            graph.blocking_positions, [Dim2D(1, 0), Dim2D(3, 0), Dim2D(1, 1)]
        )
        self.assertTrue(graph.graph_shape.is_inside_boundaries(Dim2D(1, 1)))
        self.assertFalse(graph.graph_shape.is_inside_boundaries(Dim2D(-1, 1)))
        pos = Dim2D(1, 1)
        neighbour_data = Neighbour.Data(Neighbour.Data.Type.DIAMOND, 2)
        available_poses_dic = graph.get_available_neighbours(pos, neighbour_data)
        self.assertEqual(len(available_poses_dic), 7)
        self.assertIn(Dim2D(0, 0), available_poses_dic)
        self.assertEqual(available_poses_dic[Dim2D(0, 0)], 2)
        self.assertIn(Dim2D(0, 2), available_poses_dic)
        self.assertEqual(available_poses_dic[Dim2D(0, 2)], 2)
        self.assertIn(Dim2D(1, 2), available_poses_dic)
        self.assertEqual(available_poses_dic[Dim2D(1, 2)], 1)
        self.assertIn(Dim2D(2, 0), available_poses_dic)
        self.assertEqual(available_poses_dic[Dim2D(2, 0)], 2)
        self.assertIn(Dim2D(2, 1), available_poses_dic)
        self.assertEqual(available_poses_dic[Dim2D(2, 1)], 1)
        self.assertIn(Dim2D(2, 2), available_poses_dic)
        self.assertEqual(available_poses_dic[Dim2D(2, 2)], 2)
        self.assertIn(Dim2D(3, 1), available_poses_dic)
        self.assertEqual(available_poses_dic[Dim2D(3, 1)], 2)
        pos1 = Dim2D(0, 2)
        neighbour_data = Neighbour.Data(Neighbour.Data.Type.CROSS, 1)
        available_poses_dic = graph.get_available_neighbours(pos1, neighbour_data)
        self.assertEqual(len(available_poses_dic), 1)
        self.assertEqual(tuple(available_poses_dic.keys())[0], Dim2D(1, 2))
        pos2 = Dim2D(2, 1)
        neighbour_data = Neighbour.Data(Neighbour.Data.Type.SQUARE)
        available_poses_dic = graph.get_available_neighbours(pos2, neighbour_data)
        self.assertEqual(len(available_poses_dic), 6)
        self.assertIn(Dim2D(2, 0), available_poses_dic)
        self.assertEqual(available_poses_dic[Dim2D(2, 0)], 1)
        self.assertIn(Dim2D(2, 2), available_poses_dic)
        self.assertEqual(available_poses_dic[Dim2D(2, 2)], 1)
        self.assertIn(Dim2D(1, 1), available_poses_dic)
        self.assertEqual(available_poses_dic[Dim2D(1, 1)], 1)
        self.assertIn(Dim2D(1, 2), available_poses_dic)
        self.assertEqual(available_poses_dic[Dim2D(1, 2)], 2)
        self.assertIn(Dim2D(3, 1), available_poses_dic)
        self.assertEqual(available_poses_dic[Dim2D(3, 1)], 1)

    def test_unreachable_graph_data(self):
        raw_data_handler = RawDataHandler(example_unreachable_positions())
        blocking_set = set([1])
        unreachable_positions_set = set([Dim2D(3, 2)])
        graph = Graph(
            raw_data_handler,
            Shape2D.Type.RECTANGLE,
            blocking_set,
            unreachable_positions_set,
        )
        self.assertTrue(graph.blocking_values, tuple(blocking_set))
        self.assertTrue(
            graph.blocking_positions, [Dim2D(2, 1), Dim2D(3, 1), Dim2D(2, 2)]
        )
        self.assertTrue(graph.unreachable_positions, tuple(unreachable_positions_set))
        pos = Dim2D(1, 2)
        neighbour_data = Neighbour.Data(Neighbour.Data.Type.CROSS, 2)
        available_poses_dic = graph.get_available_neighbours(pos, neighbour_data)
        self.assertEqual(len(available_poses_dic), 3)
        self.assertIn(Dim2D(1, 0), available_poses_dic)
        self.assertEqual(available_poses_dic[Dim2D(1, 0)], 2)
        self.assertIn(Dim2D(1, 1), available_poses_dic)
        self.assertEqual(available_poses_dic[Dim2D(1, 1)], 1)
        self.assertIn(Dim2D(0, 2), available_poses_dic)
        self.assertEqual(available_poses_dic[Dim2D(0, 2)], 1)


if __name__ == "__main__":
    unittest.main()
