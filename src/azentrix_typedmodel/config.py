from dataclasses import dataclass


@dataclass
class TypedModelConfig:

    strict_mode: bool = True
    allow_optional: bool = True
    allow_union: bool = True
    immutable_models: bool = False