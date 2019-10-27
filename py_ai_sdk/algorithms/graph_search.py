from py_ai_sdk.core.core_utils import error_print

class GraphSearch:
    # pylint: disable=too-many-arguments
    def __init__(self, graph, start_point, neighbour_type, blocking_points=None, neighbour_length=1):
        self.graph = graph
        self.start_point = start_point
        self.neighbour_type = neighbour_type
        self.blocking_points = blocking_points
        self.neighbour_length = neighbour_length

    def _get_available_neighbours(self, point):
        return self.graph.get_available_neighbours(self.blocking_points, self.neighbour_type, point, self.neighbour_length)

    def depth_first_search(self):
        closed_set = []
        open_set = [self.start_point]
        while open_set:
            current_point = open_set.pop()
            if current_point not in closed_set:
                closed_set.append(current_point)
                for new_candidate_point in self._get_available_neighbours(current_point):
                    open_set.append(new_candidate_point)
        return closed_set

    def breadth_first_search(self):
        closed_set = []
        open_set = [self.start_point]
        while open_set:
            current_point = open_set.pop(0)
            if current_point not in closed_set:
                closed_set.append(current_point)
                for new_candidate_point in self._get_available_neighbours(current_point):
                    open_set.append(new_candidate_point)
        return closed_set

    def dijkstra_search(self, end_point):
        # TODO: heuristic_function should use any number of parameters
        # pylint: disable=unused-argument
        def heuristic_function(not_used1, not_used2):
            return 0
        return self.a_star_search(end_point, heuristic_function)

    def a_star_search(self, end_point, heuristic_function):
        def _reconstruct_path(came_from, current_point):
            total_path = [current_point]
            while current_point in came_from:
                current_point = came_from[current_point]
                total_path.append(current_point)
            total_path.reverse()
            return total_path

        def initialize_a_star(end_point, heuristic_function):
            closed_set = []
            open_set = [self.start_point]
            came_from = {}
            g_score = {}
            f_score = {}
            g_score[self.start_point] = 0
            f_score[self.start_point] = g_score[self.start_point] + heuristic_function(self.start_point, end_point)
            return closed_set, open_set, came_from, f_score, g_score

        def get_minimum_f_score_index(open_set, f_score):
            minimum = float("inf")
            current = None
            for point in open_set:
                if f_score[point] < minimum:
                    minimum = f_score[point]
                    current = point
            return current

        closed_set, open_set, came_from, f_score, g_score = initialize_a_star(end_point, heuristic_function)

        while open_set:

            current_point = get_minimum_f_score_index(open_set, f_score)
            if current_point == end_point:
                return _reconstruct_path(came_from, current_point)

            open_set.remove(current_point)
            closed_set.append(current_point)

            for new_candidate_point in self._get_available_neighbours(current_point):
                if new_candidate_point not in closed_set:
                    tentative_g_score = g_score[current_point] + heuristic_function(new_candidate_point, current_point)
                    if new_candidate_point not in open_set:
                        open_set.append(new_candidate_point)
                        came_from[new_candidate_point] = current_point
                        g_score[new_candidate_point] = tentative_g_score
                        f_score[new_candidate_point] = g_score[new_candidate_point] + heuristic_function(new_candidate_point, end_point)
                    else:
                        if tentative_g_score < g_score[new_candidate_point]:
                            came_from[new_candidate_point] = current_point
                            g_score[new_candidate_point] = tentative_g_score
                            f_score[new_candidate_point] = g_score[new_candidate_point] + heuristic_function(new_candidate_point, end_point)
        error_print("A start cannot find the path, returning None")
        return []
