from datetime import datetime
from enum import Enum
from typing import Any, Type
from pydantic import BaseModel
from .registry import registry
from .exceptions import InvalidInputType

from .typing.primitives import (
    StringModel,
    IntegerModel,
    FloatModel,
    BooleanModel,
    DateTimeModel,
    EnumModel,
    NoneModel,
)


class TypedFactory:

    @classmethod
    def create(cls, value: Any):

        if value is None:
            return NoneModel(value=None)

        if isinstance(value, BaseModel):
            return value

        if isinstance(value, bool):
            return BooleanModel(value=value)

        if isinstance(value, int) and not isinstance(value, bool):
            return IntegerModel(value=value)

        if isinstance(value, float):
            return FloatModel(value=value)

        if isinstance(value, datetime):
            return DateTimeModel(value=value)

        if isinstance(value, Enum):
            return EnumModel(value=value)

        if isinstance(value, str):
            try:
                parsed = datetime.fromisoformat(value)
                return DateTimeModel(value=parsed)
            except ValueError:
                return StringModel(value=value)

        if isinstance(value, list):
            return cls._handle_list(value)

        if isinstance(value, tuple):
            return cls._handle_tuple(value)

        if isinstance(value, dict):
            return cls._handle_dict(value)

        return value
        

    @classmethod
    def _handle_list(cls, values):

        if not values:
            return []

        if all(isinstance(v, int) and not isinstance(v, bool) for v in values):
            from .typing.primitives import IntegerListModel
            return IntegerListModel(value=values)

        if all(isinstance(v, float) for v in values):
            from .typing.primitives import FloatListModel
            return FloatListModel(value=values)

        return [cls.create(v) for v in values]

    @classmethod
    def _handle_tuple(cls, values):

        if not values:
            return ()

        if all(isinstance(v, int) and not isinstance(v, bool) for v in values):
            from .typing.primitives import IntegerTupleModel
            return IntegerTupleModel(value=values)

        if all(isinstance(v, float) for v in values):
            from .typing.primitives import FloatTupleModel
            return FloatTupleModel(value=values)

        return tuple(cls.create(v) for v in values)

    @classmethod
    def _handle_dict(cls, value: dict):

        if "model" not in value:
            from .nested.builder import NestedBuilder
            return NestedBuilder.build(value)

        model_name = value["model"]

        if not registry.exists(model_name):
            raise InvalidInputType(
                f"Model '{model_name}' is not registered"
            )

        model_class: Type[BaseModel] = registry.get(model_name)

        payload = {
            k: cls.create(v)
            for k, v in value.items()
            if k != "model"
        }

        return model_class(**payload)