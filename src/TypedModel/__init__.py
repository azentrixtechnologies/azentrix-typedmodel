from .version import __version__

from .base import StrictBaseModel
from .factory import TypedFactory
from .registry import registry
from .validators import TypedValidator

from .nested.builder import NestedBuilder
from .nested.composer import NestedComposer

def typed_model(data):
    if isinstance(data, dict):
        return NestedBuilder.build(data)
    return TypedFactory.create(data)

__all__ = [
    "__version__",
    "StrictBaseModel",
    "TypedFactory",
    "TypedValidator",
    "NestedBuilder",
    "NestedComposer",
    "registry",
]