from typing import Any, Dict

from ..factory import TypedFactory
from ..base import StrictBaseModel


class NestedBuilder:

    @classmethod
    def build(cls, data: Any):

        if isinstance(data, dict):
            return cls._build_dict(data)

        if isinstance(data, list):
            return cls._build_list(data)

        if isinstance(data, tuple):
            return cls._build_tuple(data)

        return TypedFactory.create(data)

    @classmethod
    def _build_dict(cls, data: Dict[str, Any]):

        fields = {}

        for key, value in data.items():
            fields[key] = cls.build(value)

        from pydantic import create_model

        DynamicNestedModel = create_model(
            "DynamicNestedModel",
            __base__=StrictBaseModel,
            **{k: (type(v), ...) for k, v in fields.items()}
        )

        return DynamicNestedModel(**fields)

    @classmethod
    def _build_list(cls, data):

        items = []

        for value in data:
            items.append(cls.build(value))

        return items

    @classmethod
    def _build_tuple(cls, data):

        items = []

        for value in data:
            items.append(cls.build(value))

        return tuple(items)