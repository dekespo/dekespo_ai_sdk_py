import unittest
import random

from templates.rectangle_world import example_simple, example_blocked_in_the_middle
from algorithms.graph_search.api import GraphSearch
from core.graph import Graph
from core.dimensions import Dim2D
from core.shapes import Shape2D
from core.raw_data_handler import RawDataHandler

# TODO: Add blocked tests also
class SearchAlgorithmsTest(unittest.TestCase):
    def setUp(self):
        def generate_graph_search(example_function):
            raw_data_handler = RawDataHandler(example_function())
            blocking_values = set([1])
            graph = Graph(raw_data_handler, Shape2D.Type.RECTANGLE, blocking_values)
            start_point = Dim2D(0, 0)
            return GraphSearch(graph, start_point)

        self.simple_search_object = generate_graph_search(example_simple)
        self.blocked_search_object = generate_graph_search(example_blocked_in_the_middle)

    def test_depth_first_search(self):
        correct_path_list = Dim2D.convert_candiates_to_dimensions([
            (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
            (0, 7), (0, 8), (0, 9), (1, 9), (1, 8), (1, 7), (1, 6),
            (1, 5), (1, 4), (1, 3), (1, 2), (1, 1), (1, 0), (2, 0),
            (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
            (2, 8), (2, 9), (3, 9), (3, 8), (3, 7), (3, 6), (3, 5),
            (3, 4), (3, 3), (3, 2), (3, 1), (3, 0), (4, 5), (5, 5),
            (5, 4), (5, 3), (5, 2), (5, 1), (5, 0), (6, 0), (6, 1),
            (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8),
            (6, 9), (5, 9), (5, 8), (5, 7), (5, 6), (4, 9), (7, 9),
            (7, 8), (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2),
            (7, 1), (7, 0), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4),
            (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (9, 9), (9, 8),
            (9, 7), (9, 6), (9, 5), (9, 4), (9, 3), (9, 2), (9, 1),
            (9, 0)
        ])
        neighbour_data = Graph.NeighbourData(Graph.NeighbourData.Type.CROSS)
        dfs = self.simple_search_object.depth_first_search(neighbour_data)
        dfs.run_without_thread()
        self.assertEqual(
            dfs.get_closed_set(),
            correct_path_list
        )
        depth_size = 5
        dfs = self.simple_search_object.depth_first_search(neighbour_data, depth_size=depth_size)
        dfs.run_without_thread()
        self.assertEqual(
            dfs.get_closed_set(),
            correct_path_list[:depth_size]
        )

    def test_depth_first_search_with_thread(self):
        correct_path_list = Dim2D.convert_candiates_to_dimensions([
            (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
            (0, 7), (0, 8), (0, 9), (1, 9), (1, 8), (1, 7), (1, 6),
            (1, 5), (1, 4), (1, 3), (1, 2), (1, 1), (1, 0), (2, 0),
            (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
            (2, 8), (2, 9), (3, 9), (3, 8), (3, 7), (3, 6), (3, 5),
            (3, 4), (3, 3), (3, 2), (3, 1), (3, 0), (4, 5), (5, 5),
            (5, 4), (5, 3), (5, 2), (5, 1), (5, 0), (6, 0), (6, 1),
            (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8),
            (6, 9), (5, 9), (5, 8), (5, 7), (5, 6), (4, 9), (7, 9),
            (7, 8), (7, 7), (7, 6), (7, 5), (7, 4), (7, 3), (7, 2),
            (7, 1), (7, 0), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4),
            (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (9, 9), (9, 8),
            (9, 7), (9, 6), (9, 5), (9, 4), (9, 3), (9, 2), (9, 1),
            (9, 0)
        ])
        neighbour_data = Graph.NeighbourData(Graph.NeighbourData.Type.CROSS)
        dfs = self.simple_search_object.depth_first_search(neighbour_data, runs_with_thread=True)
        dfs.start()
        dfs.event_set()
        dfs.run()
        dfs.join()
        self.assertEqual(
            dfs.get_closed_set(),
            correct_path_list
        )

    def test_depth_first_search_with_thread_options(self):
        neighbour_data = Graph.NeighbourData(Graph.NeighbourData.Type.CROSS)
        dfs = self.simple_search_object.depth_first_search(neighbour_data)
        # TODO: Also test the stderr prints
        self.assertIsNone(dfs.run())
        dfs = self.simple_search_object.depth_first_search(neighbour_data, runs_with_thread=True)
        dfs.start()
        dfs.event_set()
        self.assertFalse(dfs.is_done())
        # Before running thread due to not having big graph enough
        dfs.kill_thread()
        dfs.event_clear()
        dfs.run()
        dfs.join()
        self.assertTrue(dfs.is_done())

    def test_breadth_first_search(self):
        correct_path_list = Dim2D.convert_candiates_to_dimensions([
            (0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2), (3, 0), (2, 1), (1, 2), (0, 3),
            (3, 1), (2, 2), (1, 3), (0, 4), (3, 2), (2, 3), (1, 4), (0, 5), (3, 3), (2, 4),
            (1, 5), (0, 6), (3, 4), (2, 5), (1, 6), (0, 7), (3, 5), (2, 6), (1, 7), (0, 8),
            (4, 5), (3, 6), (2, 7), (1, 8), (0, 9), (5, 5), (3, 7), (2, 8), (1, 9), (6, 5),
            (5, 6), (5, 4), (3, 8), (2, 9), (7, 5), (6, 6), (6, 4), (5, 7), (5, 3), (3, 9),
            (8, 5), (7, 6), (7, 4), (6, 7), (6, 3), (5, 8), (5, 2), (4, 9), (9, 5), (8, 6),
            (8, 4), (7, 7), (7, 3), (6, 8), (6, 2), (5, 9), (5, 1), (9, 6), (9, 4), (8, 7),
            (8, 3), (7, 8), (7, 2), (6, 9), (6, 1), (5, 0), (9, 7), (9, 3), (8, 8), (8, 2),
            (7, 9), (7, 1), (6, 0), (9, 8), (9, 2), (8, 9), (8, 1), (7, 0), (9, 9), (9, 1),
            (8, 0), (9, 0)
        ])
        neighbour_data = Graph.NeighbourData(Graph.NeighbourData.Type.CROSS)
        self.assertEqual(
            self.simple_search_object.breadth_first_search(neighbour_data),
            correct_path_list
        )

    def test_dijkstra_search(self):
        end_point = Dim2D(7, 6)
        weight_function = Dim2D.get_manathan_distance
        correct_path_list = Dim2D.convert_candiates_to_dimensions([
            (0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3),
            (3, 4), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (7, 6)
        ])
        neighbour_data = Graph.NeighbourData(Graph.NeighbourData.Type.CROSS)
        self.assertEqual(
            self.simple_search_object.dijkstra_search(end_point, weight_function, neighbour_data),
            correct_path_list
        )

    def test_a_star_search_simple(self):
        end_point = Dim2D(7, 6)
        a_star_functions = GraphSearch.AStarFunctions(
            heuristic_function=Dim2D.get_manathan_distance,
            weight_function=Dim2D.get_manathan_distance
        )
        correct_path_list = Dim2D.convert_candiates_to_dimensions([
            (0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2),
            (3, 3), (3, 4), (3, 5), (4, 5), (5, 5), (6, 5),
            (7, 5), (7, 6)
        ])
        neighbour_data = Graph.NeighbourData(Graph.NeighbourData.Type.CROSS)
        self.assertEqual(
            self.simple_search_object.a_star_search(end_point, a_star_functions, neighbour_data),
            correct_path_list
        )

    def test_a_star_search_with_heuristic(self):
        end_point = Dim2D(7, 6)
        def custom_heuristic_function(pos1, _):
            risk_value = 0
            if pos1 == Dim2D(4, 5):
                risk_value = 100
            return risk_value
        a_star_functions = GraphSearch.AStarFunctions(
            heuristic_function=custom_heuristic_function,
            weight_function=Dim2D.get_manathan_distance
        )
        correct_path_list = Dim2D.convert_candiates_to_dimensions([
            (0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3),
            (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (4, 9),
            (5, 9), (6, 9), (7, 9), (7, 8), (7, 7), (7, 6)
        ])
        neighbour_data = Graph.NeighbourData(Graph.NeighbourData.Type.CROSS)
        self.assertEqual(
            self.simple_search_object.a_star_search(end_point, a_star_functions, neighbour_data),
            correct_path_list
        )

    def test_a_star_search_no_path(self):
        end_point = Dim2D(7, 6)
        a_star_functions = GraphSearch.AStarFunctions(
            heuristic_function=Dim2D.get_manathan_distance,
            weight_function=Dim2D.get_manathan_distance
        )
        correct_path_list = []
        neighbour_data = Graph.NeighbourData(Graph.NeighbourData.Type.CROSS)
        self.assertEqual(
            self.blocked_search_object.a_star_search(end_point, a_star_functions, neighbour_data),
            correct_path_list
        )

    def test_randomized_depth_first_search(self):
        # Have the same seed to test randomized output
        random.seed(42)
        correct_path_list = Dim2D.convert_candiates_to_dimensions([
            (0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (2, 1), (2, 2),
            (3, 2), (3, 3), (2, 3), (1, 3), (0, 3), (0, 2), (0, 1),
            (1, 1), (1, 2), (0, 4), (1, 4), (1, 5), (2, 5), (3, 5),
            (3, 6), (2, 6), (2, 7), (2, 8), (3, 8), (3, 9), (4, 9),
            (5, 9), (6, 9), (6, 8), (5, 8), (5, 7), (5, 6), (5, 5),
            (6, 5), (7, 5), (7, 6), (7, 7), (7, 8), (8, 8), (8, 9),
            (7, 9), (9, 9), (9, 8), (9, 7), (9, 6), (8, 6), (8, 5),
            (8, 4), (8, 3), (8, 2), (9, 2), (9, 1), (8, 1), (8, 0),
            (9, 0), (7, 0), (7, 1), (7, 2), (6, 2), (6, 3), (7, 3),
            (7, 4), (6, 4), (5, 4), (5, 3), (5, 2), (5, 1), (5, 0),
            (6, 0), (6, 1), (9, 3), (9, 4), (9, 5), (8, 7), (6, 7),
            (6, 6), (4, 5), (2, 9), (1, 9), (1, 8), (1, 7), (0, 7),
            (0, 6), (1, 6), (0, 5), (0, 8), (0, 9), (3, 7), (3, 4),
            (2, 4)
        ])
        neighbour_data = Graph.NeighbourData(Graph.NeighbourData.Type.CROSS, random_output=True)
        dfs = self.simple_search_object.depth_first_search(neighbour_data)
        dfs.run_without_thread()
        self.assertEqual(
            dfs.get_closed_set(),
            correct_path_list
        )

if __name__ == "__main__":
    unittest.main()
