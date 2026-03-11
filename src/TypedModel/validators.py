from typing import Any, Union, get_origin, get_args

from .exceptions import ValidationPolicyError


class TypedValidator:

    @classmethod
    def validate(cls, value: Any, expected_type):

        origin = get_origin(expected_type)

        if origin is Union:
            return cls._validate_union(value, expected_type)

        if value is None:
            return cls._validate_optional(value, expected_type)

        if not isinstance(value, expected_type):
            raise ValidationPolicyError(
                f"Expected type {expected_type}, got {type(value)}"
            )

        return value

    @classmethod
    def _validate_union(cls, value: Any, union_type):

        possible_types = get_args(union_type)

        for t in possible_types:
            if isinstance(value, t):
                return value

        raise ValidationPolicyError(
            f"Value {value} does not match any type in {possible_types}"
        )

    @classmethod
    def _validate_optional(cls, value: Any, expected_type):

        origin = get_origin(expected_type)

        if origin is Union:
            args = get_args(expected_type)

            if type(None) in args:
                return value

        raise ValidationPolicyError(
            f"None value not allowed for type {expected_type}"
        )