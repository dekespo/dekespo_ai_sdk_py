from draw.tkinter_singleton import TkinterSingleton
from draw.colour import Colour

from .utils import Status, Utils, GraphData

class PathProcessor:

    @property
    def depth_first_search(self):
        return self._depth_first_search

    def __init__(self, status_dictionary, update_frame_in_milliseconds, graph_data: GraphData):
        self.status_dictionary = status_dictionary
        self.update_frame_in_milliseconds = update_frame_in_milliseconds
        self.graph_data = graph_data
        self._start_path_index = 0
        self._current_path_index = self._start_path_index
        self._run_dfs()

    def _run_dfs(self):
        self._depth_first_search = Utils.initialize_depth_first_search(self.graph_data)
        self.graph_search_closed_set = self._depth_first_search.get_closed_set()

    def process(self):
        if self.status_dictionary[Status.SHOULD_RESET]:
            self._reset()
        elif self.status_dictionary[Status.SHOULD_RESTART]:
            self._restart()
        elif self.status_dictionary[Status.SHOULD_GO_BACK]:
            self._go_back()
        elif self.status_dictionary[Status.SHOULD_GO_NEXT]:
            self._go_next()
        elif self.status_dictionary[Status.ON_PAUSE]:
            self._on_pause()
        elif self._is_last_step():
            self._on_last_step()
        elif self.status_dictionary[Status.SHOULD_PLAY_FORWARD]:
            self._on_play_forward()
        else:
            self._on_play_backward()


    def _update_path(self):
        TkinterSingleton.update(
            self.process,
            in_milliseconds=self.update_frame_in_milliseconds
        )

    def _reset(self):
        self._depth_first_search.kill_thread()
        self._depth_first_search.join()
        Utils.create_rectangle_canvas(self.graph_data)
        self._current_path_index = self._start_path_index
        self._run_dfs()
        self.status_dictionary[Status.SHOULD_RESET] = False
        self._update_path()

    def _restart(self):
        Utils.create_rectangle_canvas(self.graph_data)
        self._current_path_index = self._start_path_index
        self.status_dictionary[Status.SHOULD_RESTART] = False
        self._update_path()

    def _go_back(self):
        self._back_red_colouring()
        self._back_black_colouring()
        self.status_dictionary[Status.SHOULD_GO_BACK] = False
        self.status_dictionary[Status.ON_PAUSE] = True
        self._on_pause()

    def _go_next(self):
        self._next_white_colouring()
        self._next_red_colouring()
        self.status_dictionary[Status.SHOULD_GO_NEXT] = False
        self.status_dictionary[Status.ON_PAUSE] = True
        self._on_pause()

    def _on_pause(self):
        self._update_path()

    def _is_last_step(self):
        return self._current_path_index == len(self.graph_search_closed_set)

    def _on_last_step(self):
        previous = self.graph_search_closed_set[self._current_path_index-1]
        TkinterSingleton.create_rectangle_at(previous, self.graph_data.tile_size, Colour.RED)
        self.status_dictionary[Status.ON_PAUSE] = True
        self._update_path()

    def _on_play_forward(self):
        self._next_white_colouring()
        self._next_red_colouring()
        self._update_path()

    def _on_play_backward(self):
        self._back_red_colouring()
        self._back_black_colouring()
        self._update_path()

    def _next_white_colouring(self):
        if self._current_path_index > self._start_path_index:
            previous_point = self.graph_search_closed_set[self._current_path_index-1]
            self._create_rectangle_at(previous_point, Colour.WHITE)

    def _next_red_colouring(self):
        if self._current_path_index < len(self.graph_search_closed_set):
            # TODO: This part goes up to some 33 ms until dfs thread is done, find what causes this?
            current_point = self.graph_search_closed_set[self._current_path_index]
            self._create_rectangle_at(current_point, Colour.RED)
            self._current_path_index += 1

    def _back_red_colouring(self):
        if self._current_path_index > self._start_path_index + 1:
            self._current_path_index -= 1
            previous_point = self.graph_search_closed_set[self._current_path_index-1]
            self._create_rectangle_at(previous_point, Colour.RED)

    def _back_black_colouring(self):
        current_point = self.graph_search_closed_set[self._current_path_index]
        self._create_rectangle_at(current_point, Colour.BLACK)

    def _create_rectangle_at(self, point, colour: Colour):
        TkinterSingleton.create_rectangle_at(point, self.graph_data.tile_size, colour)
