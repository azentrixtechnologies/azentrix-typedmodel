from TypedModel import typed_model
from pydantic import BaseModel
from typing import Dict

def test_simple_dict():

    data = {"a": 1, "b": 2}

    model = typed_model(data)

    assert isinstance(model, BaseModel)
    assert model.a == 1
    assert model.b == 2


def test_nested_dict():

    data = {"user": {"name": "Alice", "age": 20}}

    model = typed_model(data)

    assert isinstance(model.user, BaseModel)
    assert model.user.name == "Alice"
    assert model.user.age == 20


def test_list_inside_dict():

    data = {"numbers": [1,2,3]}

    model = typed_model(data)

    assert isinstance(model.numbers, list)
    assert model.numbers == [1,2,3]


def test_tuple_inside_dict():

    data = {"coords": (10,20)}

    model = typed_model(data)

    assert isinstance(model.coords, tuple)
    assert model.coords == (10,20)


def test_list_of_dicts():

    data = [
        {"a":1},
        {"a":2}
    ]

    result = typed_model(data)

    assert isinstance(result, list)
    assert isinstance(result[0], BaseModel)
    assert result[0].a == 1


def test_deep_nested_structure():

    data = {
        "user": {
            "scores": [
                {"math": 90},
                {"science": 85}
            ]
        }
    }

    model = typed_model(data)

    assert isinstance(model.user, BaseModel)
    assert isinstance(model.user.scores, list)
    assert isinstance(model.user.scores[0], BaseModel)


def test_tuple_of_dicts():

    data = (
        {"x":1},
        {"x":2}
    )

    result = typed_model(data)

    assert isinstance(result, tuple)
    assert isinstance(result[0], BaseModel)
    assert result[0].x == 1


def test_primitives():

    assert typed_model(10) == 10
    assert typed_model("hello") == "hello"
    assert typed_model(3.14) == 3.14