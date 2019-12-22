import threading

from core.dimensions import Dim2D
from core.utils import error_print

class DepthFirstSearch(threading.Thread):
    def __init__(self, start_point: Dim2D, get_available_neighbours, neighbour_data, depth_size):
        threading.Thread.__init__(self)
        self._thread_name = "DFS_thread"
        self.start_point = start_point
        self.get_available_neighbours = get_available_neighbours
        self.neighbour_data = neighbour_data
        self.depth_size = depth_size
        self._closed_set = []

    def run(self):
        error_print(f"Running {self._thread_name}")
        self._closed_set = self.depth_first_search()
        error_print(f"Finised running {self._thread_name}")

    def depth_first_search(self):
        closed_set = []
        open_set = [self.start_point]
        while open_set and self.depth_size > len(closed_set):
            current_point = open_set.pop()
            if current_point not in closed_set:
                closed_set.append(current_point)
                for new_candidate_point in self.get_available_neighbours(
                        current_point,
                        self.neighbour_data
                    ):
                    open_set.append(new_candidate_point)
        return closed_set

    def get_closed_set(self):
        return self._closed_set
