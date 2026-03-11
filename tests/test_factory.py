from datetime import datetime
from enum import Enum

from azentrix_typedmodel.factory import TypedFactory
from azentrix_typedmodel.typing.primitives import (
    StringModel,
    IntegerModel,
    FloatModel,
    BooleanModel,
    DateTimeModel,
    EnumModel,
    NoneModel,
    IntegerListModel,
    FloatListModel,
    IntegerTupleModel,
    FloatTupleModel
)
from pydantic import BaseModel
from azentrix_typedmodel.factory import TypedFactory
from azentrix_typedmodel.registry import registry
from azentrix_typedmodel.typing.primitives import StringModel, IntegerModel


class Color(Enum):
    RED = "red"
    BLUE = "blue"


def test_string_model():
    result = TypedFactory.create("hello")
    assert isinstance(result, StringModel)


def test_integer_model():
    result = TypedFactory.create(10)
    assert isinstance(result, IntegerModel)


def test_float_model():
    result = TypedFactory.create(3.14)
    assert isinstance(result, FloatModel)


def test_boolean_model():
    result = TypedFactory.create(True)
    assert isinstance(result, BooleanModel)


def test_datetime_model():
    result = TypedFactory.create(datetime.now())
    assert isinstance(result, DateTimeModel)


def test_iso_datetime_string():
    result = TypedFactory.create("2026-03-11T10:30:00")
    assert isinstance(result, DateTimeModel)


def test_enum_model():
    result = TypedFactory.create(Color.RED)
    assert isinstance(result, EnumModel)


def test_none_model():
    result = TypedFactory.create(None)
    assert isinstance(result, NoneModel)


def test_integer_list_model():
    result = TypedFactory.create([1, 2, 3])
    assert isinstance(result, IntegerListModel)


def test_float_list_model():
    result = TypedFactory.create([1.1, 2.2])
    assert isinstance(result, FloatListModel)


def test_string_list_individual_models():
    result = TypedFactory.create(["a", "b"])
    assert isinstance(result[0], StringModel)


def test_integer_tuple_model():
    result = TypedFactory.create((1, 2, 3))
    assert isinstance(result, IntegerTupleModel)


def test_float_tuple_model():
    result = TypedFactory.create((1.1, 2.2))
    assert isinstance(result, FloatTupleModel)


def test_string_tuple_individual_models():
    result = TypedFactory.create(("a", "b"))
    assert isinstance(result[0], StringModel)


def test_mixed_list_models():
    result = TypedFactory.create([1, "hello"])

    assert isinstance(result[0], IntegerModel)
    assert isinstance(result[1], StringModel)


def test_mixed_tuple_models():
    result = TypedFactory.create((1, "hello"))

    assert isinstance(result[0], IntegerModel)
    assert isinstance(result[1], StringModel)


def test_empty_list():
    result = TypedFactory.create([])
    assert result == []


def test_empty_tuple():
    result = TypedFactory.create(())
    assert result == ()



class UserModel(BaseModel):
    name: StringModel
    age: IntegerModel


def test_handle_dict_registered_model():

    if not registry.exists("UserModel"):
        registry.register(UserModel)

    data = {
        "model": "UserModel",
        "name": "example",
        "age": 30
    }

    result = TypedFactory.create(data)

    assert isinstance(result, UserModel)
    assert isinstance(result.name, StringModel)
    assert isinstance(result.age, IntegerModel)


def test_handle_dict_missing_model_key():

    data = {
        "name": "example",
        "age": 30
    }


    result = TypedFactory.create(data)
    assert result is not None


def test_handle_dict_unregistered_model():

    data = {
        "model": "UnknownModel",
        "name": "example"
    }

    import pytest
    from azentrix_typedmodel.exceptions import InvalidInputType

    with pytest.raises(InvalidInputType):
        TypedFactory.create(data)
        


def test_handle_dict_nested_values():

    if not registry.exists("UserModel"):
        registry.register(UserModel)

    data = {
        "model": "UserModel",
        "name": "example",
        "age": 40
    }

    result = TypedFactory.create(data)

    assert isinstance(result.name, StringModel)
    assert isinstance(result.age, IntegerModel)