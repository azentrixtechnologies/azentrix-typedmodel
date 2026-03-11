from pydantic import BaseModel


class StrictBaseModel(BaseModel):

    model_config = {
        "extra": "forbid",
        "validate_assignment": True,
        "arbitrary_types_allowed": True
    }