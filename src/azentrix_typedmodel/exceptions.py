class TypedModelError(Exception):
    pass


class InvalidInputType(TypedModelError):
    pass


class ModelRegistrationError(TypedModelError):
    pass


class ValidationPolicyError(TypedModelError):
    pass