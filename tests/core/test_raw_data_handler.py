import unittest

from core.raw_data_handler import RawDataHandler
from core.dimensions import Dim2D

from templates.rectangle_world import example_simple


class RawDataHandlerTest(unittest.TestCase):
    def test_simple_raw_data(self):
        def stringfy_data(data):
            for idx, row in enumerate(data):
                data[idx] = [str(value) for value in row]
            return data

        raw_data = example_simple()
        raw_data_handler = RawDataHandler(raw_data)
        self.assertTrue(raw_data_handler.raw_data, example_simple())
        self.assertTrue(str(raw_data_handler), stringfy_data(example_simple()))
        chosen_position = Dim2D(4, 0)
        self.assertTrue(raw_data_handler.get_value(chosen_position), "1")
        raw_data_handler.set_value(chosen_position, "5")
        self.assertTrue(raw_data_handler.get_value(chosen_position), "5")
