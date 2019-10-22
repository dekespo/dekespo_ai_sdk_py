import unittest
from py_ai_sdk.templates.rectangle_world import example_1
from py_ai_sdk.core.search_algorithms import a_star_search
from py_ai_sdk.core.dimensions import Dim2D
from py_ai_sdk.core.neighbours import get_available_neighbours2d_rectangle, get_neighbours2d_rectangle_4_sides
from py_ai_sdk.core.shapes import Rectangle

class SearchAlgorithmsTest(unittest.TestCase):
    def test_depth_first_search(self):
        pass

    def test_breadth_first_search(self):
        pass

    def test_dijkstra_search(self):
        pass

    def test_a_star_search(self):
        graph, blocking_points = example_1()
        top_left_corner = Dim2D(0, 0)
        blocking_points = Dim2D.convert_candiates_to_dimensions(blocking_points)
        graph = Rectangle(top_left_corner, len(graph[0]), len(graph))
        start_point = Dim2D(0, 0)
        end_point = Dim2D(7, 6)
        heuristic_function = Dim2D.get_manathan_distance
        def get_neighbours_function(graph, current_position):
            return get_available_neighbours2d_rectangle(graph, blocking_points, get_neighbours2d_rectangle_4_sides, current_position)
        correct_path_list = Dim2D.convert_candiates_to_dimensions([
            (0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (7, 6)
        ])
        self.assertEqual(a_star_search(graph, start_point, end_point, heuristic_function, get_neighbours_function), correct_path_list)

if __name__ == "__main__":
    unittest.main()
