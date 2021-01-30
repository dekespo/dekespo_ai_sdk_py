from typing import List
from dataclasses import dataclass

from dekespo_ai_sdk.core.dimensions import Dim2D
from dekespo_ai_sdk.algorithms.graph_search.utils import SearchData, update_sets


@dataclass
class BreadthFirstSearchData(SearchData):
    breadth_size: int


class BreadthFirstSearch:
    def __init__(self, input_data: BreadthFirstSearchData):
        self.input_data = input_data
        self._closed_set: List[Dim2D] = []

    def run_without_thread(self):
        self._breadth_first_search()

    def _breadth_first_search(self):
        open_set = [self.input_data.start_point]
        while open_set:
            current_point = open_set.pop(0)
            update_sets(self._closed_set, open_set, current_point, self.input_data)

    # TODO: Use property instead
    def get_closed_set(self) -> List[Dim2D]:
        return self._closed_set
