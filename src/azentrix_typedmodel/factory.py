from typing import Any, List, Tuple, Type
from datetime import datetime
from pydantic import BaseModel

from .registry import registry
from .exceptions import InvalidInputType
from .typing.primitives import (
    StringModel,
    IntegerModel,
    FloatModel,
    BooleanModel,
    DateTimeModel,
    AnyModel,
)


class TypedFactory:

    @classmethod
    def create(cls, value: Any):

        if isinstance(value, BaseModel):
            return value

        if isinstance(value, str):
            return StringModel(value=value)

        if isinstance(value, bool):
            return BooleanModel(value=value)

        if isinstance(value, int):
            return IntegerModel(value=value)

        if isinstance(value, float):
            return FloatModel(value=value)

        if isinstance(value, datetime):
            return DateTimeModel(value=value)

        if isinstance(value, list):
            return cls._handle_list(value)

        if isinstance(value, tuple):
            return cls._handle_tuple(value)

        if isinstance(value, dict):
            return cls._handle_dict(value)

        return AnyModel(value=value)

    @classmethod
    def _handle_list(cls, values: List[Any]):

        models = []

        for v in values:
            models.append(cls.create(v))

        return models

    @classmethod
    def _handle_tuple(cls, values: Tuple[Any]):

        models = []

        for v in values:
            models.append(cls.create(v))

        return tuple(models)

    @classmethod
    def _handle_dict(cls, value: dict):

        if "model" not in value:
            raise InvalidInputType(
                "Dictionary inputs must specify a 'model' key"
            )

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