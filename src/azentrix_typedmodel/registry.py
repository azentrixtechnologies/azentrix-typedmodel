from typing import Dict, Type
from pydantic import BaseModel

from .exceptions import ModelRegistrationError


class ModelRegistry:

    def __init__(self):
        self._models: Dict[str, Type[BaseModel]] = {}

    def register(self, model: Type[BaseModel]) -> None:

        name = model.__name__

        if name not in self._models:
            self._models[name] = model

    def get(self, name: str) -> Type[BaseModel]:

        model = self._models.get(name)

        if model is None:
            raise ModelRegistrationError(
                f"Model '{name}' is not registered"
            )

        return model

    def exists(self, name: str) -> bool:
        return name in self._models

    def list_models(self):
        return list(self._models.keys())

    def clear(self):
        self._models.clear()


registry = ModelRegistry()