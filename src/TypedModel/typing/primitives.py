from datetime import datetime
from typing import Any
from typing import Tuple,List
from enum import Enum
from ..base import StrictBaseModel


class StringModel(StrictBaseModel):
    value: str


class IntegerModel(StrictBaseModel):
    value: int


class FloatModel(StrictBaseModel):
    value: float


class BooleanModel(StrictBaseModel):
    value: bool


class DateTimeModel(StrictBaseModel):
    value: datetime

class EnumModel(StrictBaseModel):
    value: Enum


class AnyModel(StrictBaseModel):
    value: Any


class IntegerListModel(StrictBaseModel):
    value: List[int]


class FloatListModel(StrictBaseModel):
    value: List[float]


class StringListModel(StrictBaseModel):
    value: List[str]


class IntegerTupleModel(StrictBaseModel):
    value: Tuple[int, ...]


class IntegerTupleModel(StrictBaseModel):
    value: Tuple[int, ...]


class FloatTupleModel(StrictBaseModel):
    value: Tuple[float, ...]


class StringTupleModel(StrictBaseModel):
    value: Tuple[str, ...]


class NoneModel(StrictBaseModel):
    value: None