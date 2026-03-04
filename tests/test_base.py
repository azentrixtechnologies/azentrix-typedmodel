import pytest
from azentrix_typedmodel.base import StrictBaseModel


class UserModel(StrictBaseModel):
    name: str


def test_valid_model():
    user = UserModel(name="John")
    assert user.name == "John"


def test_extra_field_rejected():
    with pytest.raises(Exception):
        UserModel(name="John", age=20)