from collections import OrderedDict
from dataclasses import dataclass
from typing import Callable, List

from dekespo_ai_sdk.core.dimensions import Dim2D
from dekespo_ai_sdk.core.neighbour import NeighbourData


@dataclass
class SearchData:
    start_point: Dim2D
    # bug in mypy: https://github.com/python/mypy/issues/5485
    get_available_neighbours: Callable[[Dim2D, NeighbourData], OrderedDict]  # type: ignore
    neighbour_data: NeighbourData


def update_sets(
    closed_set: List, open_set: List, current_point: Dim2D, input_data: SearchData
):
    if current_point not in closed_set:
        closed_set.append(current_point)
        for new_candidate_point, _ in input_data.get_available_neighbours(  # type: ignore
            current_point, input_data.neighbour_data  # type: ignore
        ).items():
            open_set.append(new_candidate_point)
