from typing import Any, Dict, Tuple
from pydantic import create_model


class NestedBuilder:

    _model_cache: Dict[Tuple, type] = {}

    @classmethod
    def build(cls, data: Any):

        if isinstance(data, dict):
            return cls._build_dict(data)

        if isinstance(data, list):
            return [cls.build(v) for v in data]

        if isinstance(data, tuple):
            return tuple(cls.build(v) for v in data)

        return data


    @classmethod
    def _build_dict(cls, data: Dict[str, Any]):

        processed = {k: cls.build(v) for k, v in data.items()}

        signature = tuple(sorted((k, type(v)) for k, v in processed.items()))

        if signature not in cls._model_cache:

            model = create_model(
                "DynamicNestedModel",
                **{k: (type(v), ...) for k, v in processed.items()}
            )

            cls._model_cache[signature] = model

        Model = cls._model_cache[signature]

        return Model(**processed)