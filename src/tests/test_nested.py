from datetime import datetime
from enum import Enum
from TypedModel.typing.primitives import IntegerModel
from TypedModel.nested.builder import NestedBuilder
from TypedModel.typing.primitives import (
    StringModel,
    IntegerModel,
    BooleanModel,
    DateTimeModel,
    EnumModel,
    NoneModel,
    IntegerListModel
)


class Status(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


def test_simple_nested_dict():

    data = {
        "name": "John",
        "age": 20
    }

    model = NestedBuilder.build(data)

    assert isinstance(model.name, StringModel)
    assert isinstance(model.age, IntegerModel)


def test_deep_nested_dict():

    data = {
        "user": {
            "name": "John",
            "age": 20
        }
    }

    model = NestedBuilder.build(data)

    assert isinstance(model.user.name, StringModel)
    assert isinstance(model.user.age, IntegerModel)


def test_nested_numeric_list():

    data = {
        "numbers": [1, 2, 3]
    }

    model = NestedBuilder.build(data)


    assert isinstance(model.numbers, IntegerListModel)


def test_nested_string_list():

    data = {
        "skills": ["python", "ml"]
    }

    model = NestedBuilder.build(data)

    assert isinstance(model.skills[0], StringModel)


def test_nested_datetime():

    data = {
        "created_at": datetime.now()
    }

    model = NestedBuilder.build(data)

    assert isinstance(model.created_at, DateTimeModel)


def test_nested_iso_datetime():

    data = {
        "created_at": "2026-03-11T10:30:00"
    }

    model = NestedBuilder.build(data)

    assert isinstance(model.created_at, DateTimeModel)


def test_nested_enum():

    data = {
        "status": Status.ACTIVE
    }

    model = NestedBuilder.build(data)

    assert isinstance(model.status, EnumModel)


def test_nested_none():

    data = {
        "name": "John",
        "age": None
    }

    model = NestedBuilder.build(data)

    assert isinstance(model.age, NoneModel)


def test_nested_mixed_structure():

    data = {
        "user": {
            "name": "John",
            "scores": [10, 20, 30]
        },
        "active": True
    }

    model = NestedBuilder.build(data)

    assert isinstance(model.user.name, StringModel)
    assert isinstance(model.user.scores, IntegerListModel)
    assert isinstance(model.active, BooleanModel)