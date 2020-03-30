from draw.tkinter_singleton import TkinterSingleton
from draw.colour import Colour

from .utils import Status, create_rectangle_canvas

class PathProcessor:

    # pylint: disable=too-many-arguments
    def __init__(self,
                 status_dictionary,
                 start_path_index,
                 update_frame_in_milliseconds,
                 graph_search_closed_set,
                 tile_size,
                 grid_size):
        self.status_dictionary = status_dictionary
        self.start_path_index = start_path_index
        self._current_path_index = self.start_path_index
        self.update_frame_in_milliseconds = update_frame_in_milliseconds
        self.graph_search_closed_set = graph_search_closed_set
        self.tile_size = tile_size
        self.grid_size = grid_size

    def process(self):
        if self.status_dictionary[Status.SHOULD_RESTART]:
            self.restart()
        elif self.status_dictionary[Status.SHOULD_GO_BACK]:
            self.go_back()
        elif self.status_dictionary[Status.SHOULD_GO_NEXT]:
            self.go_next()
        elif self.status_dictionary[Status.ON_PAUSE]:
            self.on_pause()
        elif self._is_last_step():
            self.on_last_step()
        else:
            self.on_play()


    def _update_path(self):
        TkinterSingleton.update(
            self.process,
            in_milliseconds=self.update_frame_in_milliseconds
        )

    def restart(self):
        create_rectangle_canvas(self.tile_size, self.grid_size)
        self._current_path_index = self.start_path_index
        self.status_dictionary[Status.SHOULD_RESTART] = False
        self._update_path()

    def go_back(self):
        if self._current_path_index > self.start_path_index + 1:
            self._current_path_index -= 1
            previous_point = self.graph_search_closed_set[self._current_path_index-1]
            TkinterSingleton.create_rectangle_at(previous_point, self.tile_size, Colour.RED)
            current_point = self.graph_search_closed_set[self._current_path_index]
            TkinterSingleton.create_rectangle_at(current_point, self.tile_size, Colour.BLACK)
        self.status_dictionary[Status.SHOULD_GO_BACK] = False
        self.status_dictionary[Status.ON_PAUSE] = True
        self.on_pause()

    def go_next(self):
        if self._current_path_index > self.start_path_index:
            previous_point = self.graph_search_closed_set[self._current_path_index-1]
            TkinterSingleton.create_rectangle_at(previous_point, self.tile_size, Colour.WHITE)
        if self._current_path_index < len(self.graph_search_closed_set):
            current_point = self.graph_search_closed_set[self._current_path_index]
            TkinterSingleton.create_rectangle_at(current_point, self.tile_size, Colour.RED)
            self._current_path_index += 1
        self.status_dictionary[Status.SHOULD_GO_NEXT] = False
        self.status_dictionary[Status.ON_PAUSE] = True
        self.on_pause()

    def on_pause(self):
        self._update_path()

    def _is_last_step(self):
        return self._current_path_index == len(self.graph_search_closed_set)

    def on_last_step(self):
        previous = self.graph_search_closed_set[self._current_path_index-1]
        TkinterSingleton.create_rectangle_at(previous, self.tile_size, Colour.RED)
        self.status_dictionary[Status.ON_PAUSE] = True
        self._update_path()

    def on_play(self):
        if self._current_path_index > self.start_path_index:
            previous_point = self.graph_search_closed_set[self._current_path_index-1]
            TkinterSingleton.create_rectangle_at(previous_point, self.tile_size, Colour.WHITE)
        if self._current_path_index < len(self.graph_search_closed_set):
            # TODO: This part goes up to some 33 ms until dfs thread is done, find what causes this?
            current_point = self.graph_search_closed_set[self._current_path_index]
            TkinterSingleton.create_rectangle_at(current_point, self.tile_size, Colour.RED)
            self._current_path_index += 1
            self._update_path()
