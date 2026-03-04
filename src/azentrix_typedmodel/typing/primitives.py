from datetime import datetime
from typing import Any

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


class AnyModel(StrictBaseModel):
    value: Any