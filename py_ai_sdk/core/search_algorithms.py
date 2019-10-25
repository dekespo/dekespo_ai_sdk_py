from py_ai_sdk.core.core_utils import error_print

def depth_first_search(graph, start_point, get_neighbours_function):
    closed_set = []
    open_set = [start_point]
    while open_set:
        current_point = open_set.pop()
        if current_point not in closed_set:
            closed_set.append(current_point)
            for new_candidate_point in get_neighbours_function(graph, current_point):
                open_set.append(new_candidate_point)
    return closed_set

def breadth_first_search(graph, start_point, get_neighbours_function):
    closed_set = []
    open_set = [start_point]
    while open_set:
        current_point = open_set.pop(0)
        if current_point not in closed_set:
            closed_set.append(current_point)
            for new_candidate_point in get_neighbours_function(graph, current_point):
                open_set.append(new_candidate_point)
    return closed_set

# Might be combined in to AStar search
def dijkstra_search():
    pass

# Simplify this algorithm
# pylint: disable=too-many-locals
def a_star_search(graph, start_point, goal_point, heuristic_function, get_neighbours_function):
    def reconstruct_path(came_from, current_point):
        total_path = [current_point]
        while current_point in came_from:
            current_point = came_from[current_point]
            total_path.append(current_point)
        total_path.reverse()
        return total_path

    def initialize_a_star(start_point, goal_point, heuristic_function):
        closed_set = []
        open_set = [start_point]
        came_from = {}
        g_score = {}
        f_score = {}
        g_score[start_point] = 0
        f_score[start_point] = g_score[start_point] + heuristic_function(start_point, goal_point)
        return closed_set, open_set, came_from, f_score, g_score

    def get_minimum_f_score_index(open_set, f_score):
        minimum = float("inf")
        current = None
        for point in open_set:
            if f_score[point] < minimum:
                minimum = f_score[point]
                current = point
        return current

    closed_set, open_set, came_from, f_score, g_score = initialize_a_star(start_point, goal_point, heuristic_function)

    while open_set:

        current_point = get_minimum_f_score_index(open_set, f_score)
        if current_point == goal_point:
            return reconstruct_path(came_from, current_point)

        open_set.remove(current_point)
        closed_set.append(current_point)

        for new_candidate_point in get_neighbours_function(graph, current_point):
            if new_candidate_point not in closed_set:
                tentative_g_score = g_score[current_point] + heuristic_function(new_candidate_point, current_point)
                if new_candidate_point not in open_set:
                    open_set.append(new_candidate_point)
                    came_from[new_candidate_point] = current_point
                    g_score[new_candidate_point] = tentative_g_score
                    f_score[new_candidate_point] = g_score[new_candidate_point] + heuristic_function(new_candidate_point, goal_point)
                else:
                    if tentative_g_score < g_score[new_candidate_point]:
                        came_from[new_candidate_point] = current_point
                        g_score[new_candidate_point] = tentative_g_score
                        f_score[new_candidate_point] = g_score[new_candidate_point] + heuristic_function(new_candidate_point, goal_point)
    error_print("A start cannot find the path, returning None")
    return []
