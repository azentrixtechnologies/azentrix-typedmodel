from TypedModel import typed_model
from pydantic import BaseModel
from typing import Dict


def test_dict_to_model():

    data = {"a": 1, "b": 2}

    model = typed_model(data)

    assert isinstance(model, BaseModel)
    assert model.a == 1
    assert model.b == 2


def test_list_processing():

    data = [1, 2, 3]

    result = typed_model(data)

    assert isinstance(result, list)
    assert result == [1, 2, 3]


def test_tuple_processing():

    data = (1, 2, 3)

    result = typed_model(data)

    assert isinstance(result, tuple)
    assert result == (1, 2, 3)


def test_list_of_dicts():

    data = [{"x": 1}, {"x": 2}]

    result = typed_model(data)

    assert isinstance(result, list)
    assert isinstance(result[0], BaseModel)
    assert result[0].x == 1


def test_tuple_of_dicts():

    data = ({"x": 1}, {"x": 2})

    result = typed_model(data)

    assert isinstance(result, tuple)
    assert isinstance(result[0], BaseModel)
    assert result[0].x == 1