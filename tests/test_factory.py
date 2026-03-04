from azentrix_typedmodel.factory import TypedFactory
from azentrix_typedmodel.typing.primitives import (
    StringModel,
    IntegerModel,
    BooleanModel
)


def test_string_model():
    result = TypedFactory.create("hello")
    assert isinstance(result, StringModel)


def test_integer_model():
    result = TypedFactory.create(10)
    assert isinstance(result, IntegerModel)


def test_boolean_model():
    result = TypedFactory.create(True)
    assert isinstance(result, BooleanModel)