import threading
from dataclasses import dataclass
from typing import Any, List

from dekespo_ai_sdk.core.dimensions import Dim2D
from dekespo_ai_sdk.core.utils import error_print
from dekespo_ai_sdk.core.neighbour import NeighbourData


@dataclass
class DepthFirstSearchData:
    start_point: Dim2D
    get_available_neighbours: Any
    neighbour_data: NeighbourData
    depth_size: int


class DepthFirstSearch(threading.Thread):
    def __init__(self, input_data: DepthFirstSearchData, runs_with_thread: bool):
        self.input_data = input_data
        self.runs_with_thread = runs_with_thread
        self._closed_set: List[Dim2D] = []

        if self.runs_with_thread:
            threading.Thread.__init__(self)
            self._thread_name = "DFS_thread"
            self._is_done = False
            self._event = threading.Event()
            self._kill = False

    def run(self):
        if not self.runs_with_thread:
            error_print(
                "You should set runs_with_thread as true in order to run this one"
            )
            return
        error_print(f"Running {self._thread_name}")
        self._is_done = False
        self.depth_first_search()
        self._is_done = True
        error_print(f"Finished running {self._thread_name}")

    def run_without_thread(self):
        self.depth_first_search()

    def depth_first_search(self):
        open_set = [self.input_data.start_point]
        while open_set and self.input_data.depth_size > len(self._closed_set):
            if self.runs_with_thread:
                if self._kill:
                    error_print(f"Killed the {self._thread_name} thread")
                    break
                self._event.wait()
            current_point = open_set.pop()
            if current_point not in self._closed_set:
                self._closed_set.append(current_point)
                for new_candidate_point, _ in self.input_data.get_available_neighbours(
                    current_point, self.input_data.neighbour_data
                ).items():
                    open_set.append(new_candidate_point)

    def event_set(self):
        self._event.set()

    def event_clear(self):
        self._event.clear()

    # TODO: Use property instead
    def get_closed_set(self):
        return self._closed_set

    def is_done(self):
        return self._is_done

    def kill_thread(self):
        self._kill = True
