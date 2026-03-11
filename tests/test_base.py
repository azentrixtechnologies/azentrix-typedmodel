import pytest
from datetime import datetime
from enum import Enum

from azentrix_typedmodel.base import StrictBaseModel


class Status(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"


class AllTypesModel(StrictBaseModel):

    name: str
    age: int
    score: float
    active: bool
    created_at: datetime
    status: Status
    numbers: list[int]
    values: tuple[int, ...]
    optional_value: int | None


def test_model_with_all_types():

    data = AllTypesModel(
        name="John",
        age=20,
        score=95.5,
        active=True,
        created_at=datetime.now(),
        status=Status.ACTIVE,
        numbers=[1, 2, 3],
        values=(10, 20, 30),
        optional_value=None
    )

    assert data.name == "John"
    assert data.age == 20
    assert data.score == 95.5
    assert data.active is True
    assert isinstance(data.created_at, datetime)
    assert data.status == Status.ACTIVE
    assert data.numbers == [1, 2, 3]
    assert data.values == (10, 20, 30)
    assert data.optional_value is None


def test_extra_field_forbidden():

    with pytest.raises(Exception):

        AllTypesModel(
            name="John",
            age=20,
            score=95.5,
            active=True,
            created_at=datetime.now(),
            status=Status.ACTIVE,
            numbers=[1,2,3],
            values=(1,2,3),
            optional_value=None,
            city="Delhi"
        )


def test_assignment_validation():

    model = AllTypesModel(
        name="John",
        age=20,
        score=95.5,
        active=True,
        created_at=datetime.now(),
        status=Status.ACTIVE,
        numbers=[1,2,3],
        values=(1,2,3),
        optional_value=None
    )

    with pytest.raises(Exception):
        model.age = "twenty"


def test_optional_value_allowed():

    model = AllTypesModel(
        name="John",
        age=20,
        score=95.5,
        active=True,
        created_at=datetime.now(),
        status=Status.ACTIVE,
        numbers=[1,2,3],
        values=(1,2,3),
        optional_value=None
    )

    assert model.optional_value is None