from dataclasses import dataclass

from core.dimensions import Dim2D

@dataclass
class GridData:
    index: Dim2D = Dim2D(0, 0)
    span_size: Dim2D = Dim2D(1, 1)
    sticky: str = "nsew"

@dataclass
class PackData:
    side: str = "left"
    fill: str = "both"
    expand: bool = True

@dataclass
class WidgetData:
    text: str

@dataclass
class _WidgetDataDefaults:
    id: str = -1
    grid_data: GridData = None
    pack_data: PackData = None

@dataclass
class _ButtonDataBase:
    callback_function: 'typing.Any'
    parameters: 'typing.Any'

@dataclass
class _TextDataBase:
    number_of_characters: int
    number_of_lines: int

@dataclass
class ButtonData(_WidgetDataDefaults, _ButtonDataBase, WidgetData):
    pass

@dataclass
class TextData(_WidgetDataDefaults, _TextDataBase, WidgetData):
    pass

@dataclass
class LabelData(_WidgetDataDefaults, WidgetData):
    pass
