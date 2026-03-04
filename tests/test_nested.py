from azentrix_typedmodel.nested.builder import NestedBuilder
from azentrix_typedmodel.typing.primitives import StringModel, IntegerModel


def test_nested_dict():

    data = {
        "name": "John",
        "age": 20
    }

    model = NestedBuilder.build(data)

    assert isinstance(model.name, StringModel)
    assert isinstance(model.age, IntegerModel)