from typing import Any
from .nested.builder import NestedBuilder


class TypedFactory:

    @classmethod
    def create(cls, data: Any):

        if isinstance(data, dict):
            return NestedBuilder.build(data)

        if isinstance(data, list):
            return [cls.create(v) for v in data]

        if isinstance(data, tuple):
            return tuple(cls.create(v) for v in data)

        return data