from typing import Any, Dict

from ..base import StrictBaseModel
from .builder import NestedBuilder


class NestedComposer:

    @classmethod
    def compose(cls, data: Dict[str, Any]):

        built_data = {}

        for key, value in data.items():
            built_data[key] = NestedBuilder.build(value)

        class ComposedModel(StrictBaseModel):
            pass

        return ComposedModel(**built_data)

    @classmethod
    def merge(cls, *models):

        merged_fields = {}

        for model in models:

            if isinstance(model, StrictBaseModel):
                for key, value in model.model_dump().items():
                    merged_fields[key] = value

        class MergedModel(StrictBaseModel):
            pass

        return MergedModel(**merged_fields)