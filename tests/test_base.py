from TypedModel import typed_model
from typing import Dict

def test_string():
    result = typed_model("hello")
    assert result == "hello"
    assert isinstance(result, str)


def test_integer():
    result = typed_model(10)
    assert result == 10
    assert isinstance(result, int)


def test_float():
    result = typed_model(3.14)
    assert result == 3.14
    assert isinstance(result, float)


def test_boolean():
    result = typed_model(True)
    assert result is True
    assert isinstance(result, bool)


def test_none():
    result = typed_model(None)
    assert result is None